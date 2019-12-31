from importlib import import_module
from pprint import pprint
from functools import reduce


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

r_dict = {
  "resourceType": "Encounter",
  "id": "11",
  "meta": {
    "versionId": "1",
    "lastUpdated": "2019-09-17T22:02:19.290+00:00",
    "source": "#1ac48e14302628ae"
  },
  "subject": {
    "reference": "Patient/6"
  },
  "period": {
    "start": "2019-09-17T21:52:19+00:00"
  },
  "location": [
    {
      "location": {
        "reference": "Location/8",
        "display": "ER, 8100bcac-c2af-4287-98cf-20c69b98f60b"
      },
      "status": "active",
      "period": {
        "start": "2019-09-17T21:52:19+00:00",
        "end": "2019-09-17T21:57:19+00:00"
      }
    },
    {
      "location": {
        "reference": "Location/9",
        "display": "Ward 1, Room d8302386-8ac1-451e-9c8a-63599aeb597b, Bed 1"
      },
      "status": "active",
      "period": {
        "start": "2019-09-17T21:57:19+00:00"
      }
    }
  ]
}

def safegetattr(obj):
    """Returns None no attribute"""
    try:
        print(eval(obj))
    except AttributeError:
        print("none")


instance = pyfhir(r_dict)
instance.status = "completed"
instance.class_fhir = pyfhir({"code":"amb"}, "Coding")
print(instance.resource_type)
pprint(instance.as_json())


print(f'access attribute if exists using gettattr: getattr(instance,"status", None)= {getattr(instance,"status", None)}')
safegetattr("instance.location[0].location.reference")
