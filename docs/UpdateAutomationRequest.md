# UpdateAutomationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Updated display name of the automation rule | [optional] 
**description** | **str** | Updated description of the automation rule | [optional] 
**trigger** | [**UpdateAutomationRequestTrigger**](UpdateAutomationRequestTrigger.md) |  | [optional] 
**conditions** | [**List[UpdateAutomationRequestConditionsInner]**](UpdateAutomationRequestConditionsInner.md) | Updated array of condition criteria evaluated against entity state | [optional] 
**actions** | [**List[UpdateAutomationRequestActionsInner]**](UpdateAutomationRequestActionsInner.md) | Updated list of dispatch actions | [optional] 
**cooldown_seconds** | **int** | Updated cooldown throttle duration in seconds | [optional] 

## Example

```python
from omnismith_sdk.models.update_automation_request import UpdateAutomationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAutomationRequest from a JSON string
update_automation_request_instance = UpdateAutomationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAutomationRequest.to_json())

# convert the object into a dict
update_automation_request_dict = update_automation_request_instance.to_dict()
# create an instance of UpdateAutomationRequest from a dict
update_automation_request_from_dict = UpdateAutomationRequest.from_dict(update_automation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


