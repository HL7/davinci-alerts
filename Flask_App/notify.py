
'''
simple flask app to fetch data build a bundle and send as $process-message operation
'''

from flask import Flask, render_template, redirect, url_for
import datetime
from json import load, dumps, loads
from requests import get, post, put
from commonmark import commonmark
import fhirtemplates # local templates
from importlib import import_module
#from pathlib import path

app = Flask(__name__)

####### Globals #############

my_list = ["10", "11", "35",'foo']
ref_server =  ("HAPI UHN R4","http://hapi.fhir.org/baseR4/") # base_url for ref server
alerts_server = 'https://ttbfdsk0pc.execute-api.us-east-1.amazonaws.com/dev' # base_url for alrts server also the WildFHIR server
now = str(datetime.datetime.utcnow().isoformat()) # get url freindly time stamp

############################

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
    r_url = f'{ref_server[1]}/{Type.capitalize()}'
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


def process_message(data):
    '''
    upload message to process-message endpoint
    return operation outcome
    '''
    with post(f'{alerts_server}/$process_message', headers=headers, data = json.dumps(data)) as r:
    #logging.info('url= {}\nr.status_code ={}\nr.reason={}\nr.headers=\nr.json()={}'.format(ref_server,r.status_code, r.reason, r.headers, r.json()))
        return (r)

def bundler(resources):  # input list of fhirclient objects return as fhirclient message Bundle
    logging.info("starting bundler...")
    new_bundle = pyfhir({'resourceType': 'Bundle'})
    new_bundle.id = 'davinci-notifications-bundle-{timestamp()}'
    new_bundle.type = 'message'
    new_bundle.timestamp = now
    new_bundle.entry = []
    entry_id_map = {}
    for res in resources:  #  append list of resources create replace id with uuids.
        logging.info('res ={}'.format(res))
        entry = Bundle.BundleEntry()
        new_id = 'some UUID'# TODO get new uuid
        entry_id_map[res.id]= new_id
        entry.fullUrl = f'urn:uuid:{new_id}'
        entry.resource = res
        new_bundle.entry.append(entry)
    logging.info('new_bundle={}'.format(new_bundle.as_json()))
    return(new_bundle)


@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

@app.template_filter()
def markdown(text, *args, **kwargs):
    return commonmark(text, *args, **kwargs)

@app.template_filter()  # to handle KeyError exception in Jinja
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


app.jinja_env.filters['datetimefilter'] = datetimefilter
app.jinja_env.filters['markdown'] = markdown
app.jinja_env.filters['keyerror_filter'] = keyerror_filter

@app.route("/")
def template_test():
    my_string='''This is a simple Flask App FHIR Facade which:

 - Fetches *Admit* and *Discharge* Encoounters from the {ref_server} Reference Servers
 - Build the Da Vinci Notifications Message
 - Submit the Message to the nominated endpoint using the $process-message operation
'''.format(ref_server=ref_server[0])

    return render_template(
        'template.html',
         my_string=my_string,
         my_list=my_list,
         title="Index",
         current_time=datetime.datetime.now(),
         ref_server= ref_server[0],
         )

@app.route("/home")  # reroute to "/"
def home():
    return redirect('/')

@app.route("/about")
def about():
    my_string='''This is a simple Flask App FHIR Facade which:

 - Fetches *Admit* and *Discharge* Encoounters from the {ref_server} Reference Servers
 - Build the Da Vinci Notifications Message
 - Submit the Message to the nominated endpoint using the $process-message operation
 '''.format(ref_server=ref_server[0])
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
def resource_not_found(type, r_id):
    my_string='''
>Woops, that resource {type}/{r_id} doesn't exist! (0 search results)

-  Click on the home button in the nav bar and try a different id
'''.format(type= type,r_id=r_id)
    return render_template('sub_template1.html',
                           my_string=my_string,
                           title="Resource not found error",
                           current_time=datetime.datetime.now(),
                           )


@app.route("/<string:r_id>")  # get the encounter and fetch the others and bundle em together!
def r_id(r_id):
    '''
    General approach
    fetch encounter,
    create messageheader, coverage, orgs 1 and 2
    fetch graph of resources as list
    create bundle
    '''
    app.logger.info(f'************r_id={r_id}*************')
    resources=[]
    Type="Encounter"
    encounter_id = r_id
    resource = fetch(Type, _id=encounter_id) # fetch encounter resource by id as dict
    if resource:
        encounter = pyfhir(r_dict=resource) # convert encounter to pyfhir instance

        ##### temp to validate examples until load better examples #####
        encounter.status = "completed" # temp to validate examples
        encounter.class_fhir = pyfhir({"code":"amb"}, "Coding")
        ##### end temp to validate examples#####

        resources.append(resource)
    else:
        return redirect(url_for('resource_not_found', type='Encounter', r_id=r_id))

    app.logger.info(f'******resources={resources}***')
    app.logger.info(f'******resource id={encounter.id}***')
    '''
    For k,v in bundle_graph.items():  # k = Type, v = tuple of sps
        resource = fetch(k, kwargs???)
        resources.append(resource)
    '''
    ################### Assemble Bundle ################################

    patient_id = encounter.subject.reference[8]
    resource = fetch('Patient', _id=patient_id) # fetch patient
    if resource:
        resources.append(resource)
        app.logger.info(f'******resources={resources}***')
    else:
        return redirect(url_for('resource_not_found', type="Patient", r_id=patient_id))

    location_id = encounter.location[0].location.reference[9]
    resource = fetch('Location', _id=location_id) # fetch location
    if resource:
        resources.append(resource)
        app.logger.info(f'******resources={resources}***')
    else:
        return redirect(url_for('resource_not_found', type="Location", r_id=location_id))

    try:
        practitioner_id = encounter.participant[0].individual.reference[10]
        resource = fetch('Practitioner', _id=practitioner_id) # fetch practitioner
        if resource:
            resources.append(resource)
        else:
            app.logger.info(f'no Practitioner/{practitioner_id} resource found in {ref_server[0]} Server')
    except TypeError as e:
        app.logger.info(f'TypeError: {str(e)} - i.e,  no Practitioner in represented in This Encounter')

    try:
        organization1_id = _id=encounter.serviceProvider.reference[13]
        resource = fetch('Organization', _id=organization1_id) # fetch org
        if resource:
            resources.append(resource)
        else:
            app.logger.info('no Organization resource found')
    except (TypeError, AttributeError) as e:
        app.logger.info(f'{str(e)} - i.e,  no Organization is represented in This Encounter')

    resource = fetch('Condition', patient=patient_id, encounter=encounter.id) # fetch condition
    if resource:
        resources.append(resource)
    else:
        app.logger.info('no Condition resource found')

    for i in ['messageheader','coverage','organization2','organization4']:
        resource = getattr(fhirtemplates,i) # resources as dict
        resource = pyfhir(resource) #convert to fhirclient
        # add in parameters as tuplse of string using get attribute or as direct call using kwargs....
        if i == 'messageheader':
            resources.insert(0,resource) #insert to beginnning of list
        else:
            resources.append(resource)

    #message_bundle = bundler(resources)

    ################### End Assemble Bundle ################################

    return render_template('sub_template3.html',
                               my_string=f"Getting Resource...for pr_id={r_id}",
                               title=f"{Type}: {r_id}", current_time=datetime.datetime.now(),
                               r_id=r_id,
                               r_dict=resource,
                               )


if __name__ == '__main__':
    app.run(debug=True)
