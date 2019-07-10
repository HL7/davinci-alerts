{:.grid}
| ﻿Alert Scenarios                                                   | Resources to include in addition to Patient and Encounter                                                                     | Notes |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------|
| Emergency and Inpatient Admissions                                | US Core R4 Condition                                                                      |       |
| Emergency and Inpatient Discharges                                | US Core R4 Condition                                                                      |       |
| Lab Results                                                       | US Core R4 DiagnosticReport, US Core R4 Observation, US Core R4 DocumentReference         |       |
| Problem with Treatment – such as drug recall, device recall/issue | US Core R4 Medication, US Core R4 AdverseEvent, US Core R4 Device                         |       |
| Encounter/Visit Notification                                      | no additional                                                                             |       |
| Public Health Notification                                        | US Core R4 Condition                                                                      |       |
| Scheduled Appointment/Pre-Admit                                   | R4 Appointment                                                                            |       |
| Referral                                                          | R4 ServiceRequest, R4 Practitioner                                                        |       |
| Ordered Device/Biometric/Patient (i.e. Fit Bit)                   | R4 DeviceRequest                                                                          |       |
| Treatment Start/End                                               | US Core R4 MedicationAdministration                                                       |       |
| Change in Social Determinants of Health                           | R4 Observation                                                                            |       |
| Birth/Death                                                       | No additional resource                                                                    |       |
| Coverage Start/End                                                | DEQM Coverage                                                                             |       |
| Notification of Prior Authorization (Pended to Approved/Denied)   | R4 ClaimResponse                                                                          |       |
| Pharmacy (Pickup, Restock, Dispense)                              | US Core R4 Medication, US Core R4 MedicationDispense, R4 SupplyDelivery, R4 SupplyRequest |       |
| Notification of New Condition                                     | US Core R4 Condition                                                                      |       |
| Work Comp Initial/Visits/Services                                 | US Core R4 Condition, R4 Coverage                                                         |       |
| Changes in Care Team                                              | US Core R4 Practitioner, R4 RelatedPerson, R4 CareTeam                                    |       |
