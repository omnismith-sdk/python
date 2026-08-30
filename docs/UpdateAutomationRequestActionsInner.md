# UpdateAutomationRequestActionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Action delivery channel type | [optional] 
**config** | **object** | Action payload and channel routing configuration | [optional] 

## Example

```python
from omnismith_sdk.models.update_automation_request_actions_inner import UpdateAutomationRequestActionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAutomationRequestActionsInner from a JSON string
update_automation_request_actions_inner_instance = UpdateAutomationRequestActionsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateAutomationRequestActionsInner.to_json())

# convert the object into a dict
update_automation_request_actions_inner_dict = update_automation_request_actions_inner_instance.to_dict()
# create an instance of UpdateAutomationRequestActionsInner from a dict
update_automation_request_actions_inner_from_dict = UpdateAutomationRequestActionsInner.from_dict(update_automation_request_actions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


