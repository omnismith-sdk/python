# ToggleEntityActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Whether the action is offered and executable | 

## Example

```python
from omnismith_sdk.models.toggle_entity_action_request import ToggleEntityActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ToggleEntityActionRequest from a JSON string
toggle_entity_action_request_instance = ToggleEntityActionRequest.from_json(json)
# print the JSON string representation of the object
print(ToggleEntityActionRequest.to_json())

# convert the object into a dict
toggle_entity_action_request_dict = toggle_entity_action_request_instance.to_dict()
# create an instance of ToggleEntityActionRequest from a dict
toggle_entity_action_request_from_dict = ToggleEntityActionRequest.from_dict(toggle_entity_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


