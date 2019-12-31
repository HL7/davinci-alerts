
'''
simple flask app to fetch data build a bundle and send as $process-message operation
'''

from flask import Flask, render_template, redirect, url_for, session
from werkzeug.contrib.cache import SimpleCache
import sys, datetime, uuid
from json import load, dumps, loads
from requests import get, post, put
from commonmark import commonmark
import fhirtemplates # local templates
from importlib import import_module
#from pathlib import path
from copy import deepcopy
import fhirclient.r4models.meta as M
import fhirclient.r4models.fhirdate as FD
import fhirclient.r4models.bundle as B
from utils import write_val

app = Flask(__name__)
app.secret_key = 'my secret key'
cache = SimpleCache()

####### Globals #############
validate_me = False

profile_list = dict(
Bundle = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/notifications-bundle",
MessageHeader = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/notifications-messageheader",
MessageHeader_admit = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/admit-notification-messageheader",
MessageHeader_discharge ="http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/dsicharge-notification-messageheader",
Condition = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/admit-discharge-notification-condition",
Coverage = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/admit-discharge-notification-coverage",
Encounter = "http://hl7.org/fhir/us/davinci-alerts/StructureDefinition/admit-discharge-notification-encounter",
Patient = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient",
Practitioner = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner",
Location = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-location",
Organization = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization",
)

# admit if encounter in progess and type if class =
admit_types = dict(
            EMER = 'notification-admit-er',
            IMP = 'notification-admit-inpatient',
            OBSENC = 'notification-admit-forobservation',
            AMB = 'notification-admit-ambulatory',
        )
# discharge if encounter completed

enc_list = [i for i in range(905,911)] # test R4 Server encounters

get_ids = [# [{name:name, Type:Type, args=(args), is_req=bool}]
    dict(
    name = 'patient',
    Type = 'Patient',
    args = ('subject','reference'),
    is_req=True,
    ),
    dict(
    name = 'location',
    Type = 'Location',
    args = ('location','location','reference'),
    is_req=True,
    ),
    dict(
    name = 'practitioner',
    Type = 'Practitioner',
    args = ('participant','individual','reference'),
    is_req=False,
    ),
    dict(
    name = 'service_provider',
    Type = 'Organization',
    args = ('serviceProvider','reference'),
    is_req=False,
    ),
]

ref_server =  {  # base_url for reference server - no trailing forward slash
    'FHIR R4': 'http://test.fhir.org/r4',
    'HAPI UHN R4': 'http://hapi.fhir.org/baseR4',
    'WildFHIR': 'http://wildfhir4.aegis.net/fhir4-0-0',
    }
ref_server_name = "FHIR R4"
alerts_server = { # base_url for alerts server
    "Alerts-RI": 'https://davinci-alerts-receiver.logicahealth.org/fhir',
    'Cigna': 'https://ttbfdsk0pc.execute-api.us-east-1.amazonaws.com/dev',
    'WildFHIR': "http://wildfhir4.aegis.net/fhir4-0-0",
    }

# some timestamp formats
now = f'{str(datetime.datetime.utcnow().isoformat())}Z' # get url freindly time stamp
id_safe_now = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S.%f')
FD.FHIRDate(now)
############################

#  ************************** add profiles ************************
def add_profile(r):
    try:
        r.meta.profile.append(profile_list[r.resource_type])# add profile if meta.profile already there
        r.meta.profile = list(set(r.meta.profile))# remove duplicate
    except AttributeError: # no profile
        #r.meta = M.Meta()
        try:
            r.meta.profile = [(profile_list[r.resource_type])]
        except AttributeError: # no meta
            r.meta = M.Meta()
            r.meta.profile = [(profile_list[r.resource_type])]

# *************************** check and append **************

def append_resource(resource, resources, Type, id=None, is_req=False):
        if resource:
            r_pyfhir = pyfhir(r_dict=resource)
            add_profile(r_pyfhir)
            resources.append(r_pyfhir)
            app.logger.info(f'******resources={resources}***')
        elif is_req:
            return redirect(url_for('resource_not_found', type=Type, id=my_id))
        else:
            app.logger.info(f'no {Type}/{id} resource found')

#  ************************** get id ************************
def get_r_id(Type,*args):
    app.logger.info(f'****** args = {args}***')
    my_id = atterror_filter(Type, *args)
    app.logger.info(f'****** my_id = {my_id}***')
    if my_id.startswith("urn:uuid:"):
        app.logger.info(f'****** my_id = {my_id[9:]}***')
        return my_id[9:]
    if my_id.endswith(":-("):
        app.logger.info('****** my_id = "[no id]"***')
        return '[no id]'
    else:  # assume is Regular FHIR endpoint # ID
        app.logger.info(f'****** my_id = {my_id.split("/")[-1]}***')
        return my_id.split('/')[-1]

# *********************** Fetch Resource ********************
def fetch(Type,**kwargs):
    '''
    fetch resource by search parameters e.g. _id
    return resource as fhirclient model
    '''
    headers = {
    'Accept':'application/fhir+json',
    'Content-Type':'application/fhir+json'
    }

    r_url = f'{ref_server[ref_server_name]}/{Type.capitalize()}'
    app.logger.info(f'****** r_url = {ref_server[ref_server_name]}/{Type.capitalize()}***')
    app.logger.info(f'****** params = {kwargs}*****')
    with get(r_url, headers=headers, params=kwargs) as r:
        # return r.status_code
        # view  output
        # return (r.json()["text"]["div"])
        if r.status_code <300 and r.json()["total"] > 0: # >0
            return r.json()["entry"][0]["resource"] # just the first for now
        else:
            return None

def pyfhir(r_dict, Type=None):
    '''
    input is resource instance as r_dict
    output is fhirclient class instance
    '''
    type = Type if Type else r_dict['resourceType']
    MyClass = getattr(import_module(f"fhirclient.r4models.{type.lower()}"),type)
    # Instantiate the class (pass arguments to the constructor, if needed)
    instance = MyClass(r_dict, strict=False)
    return(instance)

def bundler(resources, save_me=False):  # input list of fhirclient objects return a json copy message Bundle
    resources_copy = deepcopy(resources)
    app.logger.info("starting bundler...")
    bundle = pyfhir({'resourceType': 'Bundle'})
    bundle.id = f'davinci-notifications-bundle-{id_safe_now}'
    if save_me: #add meta profiles
        bundle.meta = M.Meta()
        bundle.meta.profile = [profile_list["Bundle"]]
    bundle.type = 'message'
    bundle.timestamp = FD.FHIRDate(now)
    bundle.entry = []
    ref_map = {}
    for r in resources_copy:  #  append list of resources create replace id with uuids.
        app.logger.info(f'res = {r}')
        entry = B.BundleEntry()
        new_urn = uuid.uuid1().urn # TODO get new uuid
        old_ref = f'{r.resource_type}/{r.id}'
        ref_map[old_ref] = new_urn
        entry.fullUrl = new_urn
        if not save_me: #remove meta profiles
             r.meta.profile = None
             if r.meta: #remove meta
                r.meta = None
        r.id = None #remove old_ids
        r.text = None #remove textB
        entry.resource = r
        bundle.entry.append(entry)
    app.logger.info(f'ref_map = {dumps(ref_map, indent = 4)}')
    b_json = dumps(bundle.as_json(), indent=4)
    for old_ref, new_urn in ref_map.items():
        b_json = b_json.replace(old_ref, new_urn)
    return(b_json)


@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

@app.template_filter()
def markdown(text, *args, **kwargs):
    return commonmark(text, *args, **kwargs)

"""
@app.template_filter()  # to handle KeyError exception in Jinja for dicts
def keyerror_filter(value, *args):
    app.logger.info(f'****** args ={args}***')
    try:
        app.logger.info(f'****** value type value={type(value)}***')
        for arg in args:
            app.logger.info(f'****** arg = {arg}***')
            app.logger.info(f'****** value[{arg}] = ***')
            value = value[arg][0] if isinstance(value[arg], list) else value[arg]
        return (value)
    except KeyError:
        return (f"Resource has no <code>{'.'.join(args)}</code> element :-(")
"""


@app.template_filter()  # to handle AttributeError exception in Jinja for classes
def atterror_filter(value, *args):
    app.logger.info(f'****** args={args}***')
    try:
        app.logger.info(f'****** value type value={type(value)}***')
        for arg in args:
            app.logger.info(f'****** arg = {arg}***')
            app.logger.info(f'****** getattr({value},{arg}) = {getattr(value,arg)}***')
            value = getattr(value, arg)[0] if isinstance(getattr(value,arg), list) else getattr(value,arg)
            app.logger.info(f'****** value = {value} , type = {type(value)}***')
        return (value)
    except AttributeError:
        return (f"Resource has no <code>{'.'.join(args)}</code> element :-(")

app.jinja_env.filters['datetimefilter'] = datetimefilter
app.jinja_env.filters['markdown'] = markdown
# app.jinja_env.filters['keyerror_filter'] = keyerror_filter
app.jinja_env.filters['atterror_filter'] = atterror_filter

@app.route("/")
def template_test():
    my_string='''This is a simple Flask App FHIR Facade which:

 - Fetches *Admit* and *Discharge* Encoounters from the {ref_server} Reference Server
 - Build the Da Vinci Notifications Message
 - Submit the Message to the nominated endpoint using the $process-message operation
'''.format(ref_server=ref_server_name)

    return render_template(
        'template.html',
         my_string=my_string,
         enc_list=enc_list,
         title="Index",
         current_time=datetime.datetime.now(),
         )

@app.route("/home")  # reroute to "/"
def home():
    return redirect('/')

@app.route("/about")
def about():
    my_string='''This is a simple Flask App FHIR Facade which:

 - Fetches *Admit* and *Discharge* Encounters from the {ref_server} Reference Servers
 - Build the Da Vinci Notifications Message
 - Submit the Message to the nominated endpoint using the $process-message operation
 '''.format(ref_server=ref_server_name)
    return render_template('sub_template1.html',
                           my_string=my_string,
                           title="About",
                           current_time=datetime.datetime.now(),
                           )

@app.route("/contact")
def contact():
    return render_template('sub_template2.html'
                           , my_string="Contact Information",
                           title="Contact Us", current_time=datetime.datetime.now(),
                            )

@app.route("/not_found/<type>/<r_id>")
def resource_not_found(type, r_id=''):
    my_string='''
>Woops, that resource `{type}/{r_id}` doesn't exist! (0 search results)

-  Click on the home button in the nav bar and try a different id
'''.format(type= type,r_id=r_id)
    return render_template('sub_template1.html',
                           my_string=my_string,
                           title="Resource not found error",
                           current_time=datetime.datetime.now(),
                           )


@app.route("/<string:r_type>/<string:r_id>")  # get the encounter and fetch the others and bundle em together!
def r_id(r_type, r_id):
    '''
    General approach
    fetch encounter,
    create messageheader, coverage, orgs 1 and 2
    fetch graph of resources as list
    create bundle
    '''
    app.logger.info(f'************r_id={r_id}*************')
    if r_type == "Encounter":
        resource = fetch(r_type, _id=r_id) # fetch encounter resource by id as dict
        if resource:
            resource = pyfhir(r_dict=resource) # convert encounter to pyfhir instance
            add_profile(resource) # add profile if not already there
            ##### check to see if status and class present #####
            try:
                r_status = resource.status
            except:
                resource.status = "completed" # temp to validate examples
            try:
                r_class = resource.class_fhir
            except:
                resource.class_fhir = pyfhir({"code":"AMB"}, "Coding")

            #session['encounter'] = resource.as_json()  # save encounter class as dict for this session

            cache.set('encounter', resource, timeout=60*15 )
            '''set cache to use during the session.
            assuming single user for now to keep it simple
            keep data for 15 minutes
            '''
        else:
            return redirect(url_for('resource_not_found', type='Encounter', r_id=r_id))

        app.logger.info(f'******resource id={resource.id}***')
        app.logger.info(f'******estimated file size ={str(sys.getsizeof(resource.as_json())/1024)} "KB"***')
        app.logger.info(f'******see what is in cache = {cache.get("encounter")}***')

        return render_template('sub_template4.html',
               my_string=f"Getting Resource...for pr_id={r_id}",
               title=f"{r_type}: {r_id}", current_time=datetime.datetime.now(),
               r_type = r_type,
               r_id=r_id,
               r_pyfhir=resource,
               )
    else:
        ################### Assemble Bundle ################################
        app.logger.info(f'******see what is in cache = {cache.get("encounter")}***')
        encounter = cache.get("encounter") # get resources from cache
        resources= [encounter]

        #+++ create messageheader

        mh = getattr(fhirtemplates,'messageheader') # resources as dict
        mh = pyfhir(mh) #convert to fhirclient
        mh.id = f'messageheader-{id_safe_now}'
        mh.focus[0].reference = f"Encounter/{encounter.id}"
        if encounter.status == "in-progress":
            try:
                mh.eventCoding.code =  admit_types[encounter.class_fhir.code]
                mh.eventCoding.display = mh.eventCoding.code.replace('-', ' ').title()
                mh.focus[0].display = f'{mh.eventCoding.display}({encounter.type[0].text})'
            except KeyError:
                pass
        elif encounter.status == "completed":
            mh.eventCoding.code =  'notification-discharge'
            mh.eventCoding.display = 'Notification Discharge'
            mh.meta.profile = profile_list['MessageHeader_discharge']
        # TODO add discharge subtypes and handle other statuses

        mh.destination[0].name = list(alerts_server.keys())[0]
        mh.destination[0].endpoint = list(alerts_server.values())[0]
        # TODO make a selection for the destination

        mh.sender.reference = 'Organization/sending_organization'  # hardcoded for now
        mh.sender.display = "Acme Message Sender"  # hardcoded for now

        mh.author.reference = encounter.participant[0].individual.reference
        mh.author.display = encounter.participant[0].individual.display

        mh.responsible.reference = encounter.serviceProvider.reference
        mh.responsible.display = encounter.serviceProvider.display

        resources.insert(0, mh)

        for i in get_ids:  # [{Type:Type, args=(args)}]
            Type = i['Type']
            args = i['args']
            is_req = i['is_req']
            my_id = get_r_id(encounter,*args)
            resource = fetch(Type, _id=my_id)
            append_resource(resource, resources, Type=Type, id=my_id, is_req = is_req)



        resource = fetch('Condition',
                         patient=get_r_id(encounter,'subject','reference'), encounter=encounter.id,
                         ) # fetch condition
        append_resource(resource, resources, Type='Condition')

        resource = fetch('Coverage',
                         patient=get_r_id(encounter,'subject','reference'),
                          ) # fetch coverage
        coverage = pyfhir(r_dict=resource)
        append_resource(resource, resources, Type='Coverage')

        if coverage:
            my_id = get_r_id(coverage,'payor','reference')
            resource = fetch('Organization',
                            _id=my_id,
                         ) # fetch coverage
            append_resource(resource, resources, Type='Organization', id=my_id)

        sender = getattr(fhirtemplates,'sender') # hardcode org for now
        resource = pyfhir(sender) #convert to fhirclient
        add_profile(resource)
        resources.append(resource)

        message_bundle = bundler(resources) # returns as json string!
        # validate by writing to ig examples file and running the IG Build:
        if validate_me:
            message_bundle = bundler(resources, save_me=True) # returns as json string!
            write_val(message_bundle, id_safe_now)
        else:
            message_bundle = bundler(resources, save_me=False) # returns as json string!

        cache.set('message_bundle', message_bundle, timeout=60*15 )
        '''set cache to use during the session.
        assuming single user for now to keep it simple
        keep data for 15 minutes
        '''
        ################### End Assemble Bundle ################################

        return render_template('sub_template5.html',
               my_string=f"Getting Resources ready for Bundler...for encounter pr_id={encounter.id}",
               title=f"Bundle Prep", current_time=datetime.datetime.now(),
               resources=resources,
               endpoints = alerts_server,
               message_bundle = message_bundle, # returns as json string!
               )
@app.route("/<path:target_url>/$process-message")
def process_message(target_url):
        '''
        upload message to process-message endpoint
        return operation outcome
        '''
        headers = {
        'Accept':'application/fhir+json',
        'Content-Type':'application/fhir+json'
        }

        data = cache.get("message_bundle")
        app.logger.info(f'data = {data}')
        with post(f'{target_url}/$process-message', headers=headers, data=data) as r:
            try:
                oo = r.json()
            except:
                oo = {}
            app.logger.info(f'url= {target_url}\n\
                            r.status_code ={r.status_code}\n\
                            r.reason={r.reason}\n\
                            r.headers=\n\
                            {r.headers}\n')

        return render_template('sub_template6.html',
                           my_string=f"Send Message Bundle to {target_url}/$process-message with response = **{r.status_code}**",
                           title="$process-message Response",
                           current_time=datetime.datetime.now(),
                            headers = dict(r.headers),
                            oo = oo
                            )

if __name__ == '__main__':
    app.run(debug=True)
