### Workflow Overview

See the [Framework] page for a detailed description of the technical workflow and API guidance.
{:.highlight-note}

Figure 1 below illustrates the general notification workflow of a Sender sending an unsolicited notification to a Receiver or Intermediary when triggered by an event or request.

{% include img.html img="notification_wf1.svg" caption="Figure 1" %}

1. An event or request triggers a notification to be sent from a Sender (aka source application) to a Recipient or Intermediary (aka destination application).  The notification includes common information shared across all Da Vinci notifications and use case dependent information.
2. The Sender notifies the Recipient by sending an "unsolicited" notification to the Recipient's FHIR endpoint.
3. The notification is processed according the Receiver or Intermediary internal business rules.

### Intermediary Workflow

Figure 2 shows the process where an Intermediary, having previously received a notification, forwards the notification to the Recipient. In this case, the Intermediary is responsible for the redistribution of the data.  Note that it may customize the data based on end user needs.  Although not represented in the figure, there may be multiple Intermediaries.

{% include img.html img="notification_wf2.svg" caption="Figure 2" %}

{% include link-list.md %}
