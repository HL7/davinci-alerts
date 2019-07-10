---
title: General Guidance and Definitions
layout: default
active: guidance

---

{:.no_toc}

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->

* Do not remove this line (it will not be displayed)
{:toc}

### Introduction
{:.self-link}

Da Vinci Alerts are transacted either using a FHIR RESTful push or FHIR subscriptions

### Preconditions and Assumptions

#### Preconditions

- There is an event that drives the generation of the Alert.
- An Alert will be generated for each patient separately.
  - The event can be for one or more patients
- FHIR R4 RESTful endpoints exist for all actors.
  - Note that this is a requirement for FHIR RESTful Push transactions and for RestHook channel transactions when using the FHIR subscriptions.  It is not required for other type of subscription channels or FHIR messaging.
- System level trust exists between the actors.
  - Clients have been authorized by the servers.
  - It is assumed that consent is managed elsewhere.
- “Endpoint Discovery” i.e., a curated list of where to forward the data  is actively maintained and managed by the Alert Senders and Intermediaries.  These interactions are outside the scope of this specification.
   - Note that this is needed when transacting alerts using FHIR RESTful push notifications.


#### Assumptions
- Based on FHIR R4 and US Core R4 profiles where applicable
- Alerts are transacted either using a FHIR RESTful push or FHIR subscriptions.
- The “Alert Bundle” is the FHIR object that is exchanged for all alert transactions.
  - The [DaVinci Communication Resource Profile] is always part of the bundle and provides the necessary context for the alert reason.
  - All supporting data (resources) for each kind of alert is referenced in `Communication.payload` and included in the bundle.
  - type ‘transaction’
  - Graph of resources is use case dependent

The following Table summarizes the Alert Scenarios and the Resources that may be referenced in the [Da Vinci Communication Profile] payload element and included in the alert Bundle:

{% include alert_scenarios.md %}
{: .grid}


{% include examplebutton_default.html example="example" b_title = "Example Button bar" %}

FOO

blah blah blah

### More Stuff

inline json example exploiting Rouge to highlight inline comment (errors in json):

~~~json
{
"foo":  "bar"  \\adding comment here is shown as a error in jekyll,
"foo2":  "bar2"
}
~~~

#### And More Stuff


---

{% include link-list.md %}
