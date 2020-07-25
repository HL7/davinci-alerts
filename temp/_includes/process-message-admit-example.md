
### Examples
{:.no_toc}

**Scenario:**

Patient Y has been admitted to Provider X 's facility.  Acting in the role of Sender, Provider X alerts Payer Z, who is acting in the Recipient role, of the admission.  The Notification is transacted as the `[$process-message]` operation. The body of the operation is a Message Bundle containing:

1. The Message Header which is the first resource in the bundle and contains the the message event code - that identifies the nature of the notification.
1. The other resources in the bundle depend on the type of the notification use case as defined by either the MessageDefinition and GraphDefinition or FHIR Profiles.

An HTTP Status success code is returned on successful submission.

**Push Notification using the $process-message**

`POST [base]/$process-message`

**Request body**

~~~
{% include_relative Bundle-admit-notification-message-bundle-01.json %}
~~~

**Response**

~~~
HTTP/1.1 200 OK
[other headers]
~~~
