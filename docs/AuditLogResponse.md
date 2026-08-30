# AuditLogResponse

An immutable audit log entry recording a historical project mutation or action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **UUID** | Unique audit event identifier (UUIDv7) | [optional] 
**occurred_at** | **datetime** | Event occurrence timestamp in ISO 8601 format | [optional] 
**event_type** | **str** | Action or event identifier (e.g. entity.created, entity.updated, entity.deleted, template.created) | [optional] 
**resource_type** | **str** | Target domain resource type (entity, template, attribute, project) | [optional] 
**resource_id** | **str** | Target resource identifier (UUID) | [optional] 
**value** | **str** | Summary description or serialized payload of the mutation | [optional] 
**author_email** | **str** | Email of the authenticated user who initiated the action | [optional] 
**correlation_id** | **str** | Distributed tracing correlation identifier | [optional] 

## Example

```python
from omnismith_sdk.models.audit_log_response import AuditLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogResponse from a JSON string
audit_log_response_instance = AuditLogResponse.from_json(json)
# print the JSON string representation of the object
print(AuditLogResponse.to_json())

# convert the object into a dict
audit_log_response_dict = audit_log_response_instance.to_dict()
# create an instance of AuditLogResponse from a dict
audit_log_response_from_dict = AuditLogResponse.from_dict(audit_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


