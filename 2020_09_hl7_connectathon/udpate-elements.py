"""
Script to update element in bundles - in this case the system in Encounter type and Condition code
"""
from json import load, dumps


map={}
file='2020_09_hl7_connectathon/Synthea_Alert_Test_Data/fhir/transfer_notify-100.json'
with open(file) as f:
    b = load(f)

print(b['resourceType'])

for e in b['entry']:

    try:
        print(e['resource']['type'][0]['coding'][0]['display'])
        display = e['resource']['type'][0]['coding'][0]['display']
        system = e['resource']['type'][0]['coding'][0]['system']
    except KeyError:
        pass
    else:
        if display == 'Examplotomy':
            print('change ' + system + ' to http://example.org/fhir/conditions')
            e['resource']['type'][0]['coding'][0]['system'] = 'http://example.org/fhir/conditions'
        elif display == 'Examplotomy Encounter':
            print('change ' + system + ' to http://example.org/fhir/encounters')
            e['resource']['type'][0]['coding'][0]['system'] = 'http://example.org/fhir/encounters'
print(type(b))
print(dumps(b))

with open(file, 'w') as f:
    f.write(dumps(b))
