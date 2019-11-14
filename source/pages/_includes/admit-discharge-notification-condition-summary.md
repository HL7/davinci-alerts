**Condition**

#### Summary of the Mandatory Requirements
1.  An Encounter Reference  in `Condition.encounter`

#### Summary of Constraints
1. Condition.clinicalStatus SHALL be present if verificationStatus is not entered-in-error and category is problem-list-item
1. If condition is abated, then clinicalStatus must be either inactive, resolved, or remission
1. Condition.clinicalStatus SHALL NOT be present if verification Status is entered-in-error
1. A code in Condition.category SHOULD be from US Core Condition Category Codes value set.