from json import load

map={}
file='2020_05_hl7_connectathon/Synthea_Alert_Test_Data/fhir/admit_notify-2.json'
with open(file) as f:
    b = load(f)

print(b['resourceType'])


r_index = [e['fullUrl'] for e in b['entry'] ]

print(r_index)
print(len(r_index))

for e,i in enumerate(b.entry):

    map[i] = r_index(i.fullUrl)

print map
