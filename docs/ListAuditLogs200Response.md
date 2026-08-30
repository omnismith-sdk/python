# ListAuditLogs200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AuditLogResponse]**](AuditLogResponse.md) | List of immutable audit log entries | [optional] 
**total** | **int** | Total count of matching audit log records | [optional] 

## Example

```python
from omnismith_sdk.models.list_audit_logs200_response import ListAuditLogs200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAuditLogs200Response from a JSON string
list_audit_logs200_response_instance = ListAuditLogs200Response.from_json(json)
# print the JSON string representation of the object
print(ListAuditLogs200Response.to_json())

# convert the object into a dict
list_audit_logs200_response_dict = list_audit_logs200_response_instance.to_dict()
# create an instance of ListAuditLogs200Response from a dict
list_audit_logs200_response_from_dict = ListAuditLogs200Response.from_dict(list_audit_logs200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


