# SwitchProjectRequest

Payload for switching the active project context

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **UUID** | The ID of the project to switch to | 

## Example

```python
from omnismith_sdk.models.switch_project_request import SwitchProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchProjectRequest from a JSON string
switch_project_request_instance = SwitchProjectRequest.from_json(json)
# print the JSON string representation of the object
print(SwitchProjectRequest.to_json())

# convert the object into a dict
switch_project_request_dict = switch_project_request_instance.to_dict()
# create an instance of SwitchProjectRequest from a dict
switch_project_request_from_dict = SwitchProjectRequest.from_dict(switch_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


