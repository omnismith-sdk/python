# ExecuteEntityActionResponse

Receipt of an executed action: the record, the action, and exactly what was written (submitted values with presets applied). The record itself is not returned because its read model is projected asynchronously; fetch it with `GET /entities/{id}` once the change is needed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **UUID** |  | 
**template_id** | **UUID** |  | 
**action** | [**ExecuteEntityActionResponseAction**](ExecuteEntityActionResponseAction.md) |  | 
**attributes** | **Dict[str, str]** | Attribute slug (or UUID for a slugless attribute) → value written, as stored | 

## Example

```python
from omnismith_sdk.models.execute_entity_action_response import ExecuteEntityActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteEntityActionResponse from a JSON string
execute_entity_action_response_instance = ExecuteEntityActionResponse.from_json(json)
# print the JSON string representation of the object
print(ExecuteEntityActionResponse.to_json())

# convert the object into a dict
execute_entity_action_response_dict = execute_entity_action_response_instance.to_dict()
# create an instance of ExecuteEntityActionResponse from a dict
execute_entity_action_response_from_dict = ExecuteEntityActionResponse.from_dict(execute_entity_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


