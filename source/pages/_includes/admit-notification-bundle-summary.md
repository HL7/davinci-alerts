**Bundle**

#### Summary of the Mandatory Requirements
1.  A  code  in `Bundle.type`  = the fixed value  "message"

#### Summary of the Unsupported Elements
1. `Bundle.total`
1. `Bundle.entry.search`
1. `Bundle.entry.request`
1. `Bundle.entry.response`

#### Summary of Constraints
1. FullUrl must be unique in a bundle, or else entries with the same fullUrl must have different meta.versionId (except in history bundles)
1. A message must have a MessageHeader as the first resource
1. fullUrl cannot be a version specific reference
