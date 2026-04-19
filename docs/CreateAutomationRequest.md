# CreateAutomationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**trigger** | [**CreateAutomationRequestTrigger**](CreateAutomationRequestTrigger.md) |  | 
**conditions** | [**List[CreateAutomationRequestConditionsInner]**](CreateAutomationRequestConditionsInner.md) |  | 
**actions** | [**List[CreateAutomationRequestActionsInner]**](CreateAutomationRequestActionsInner.md) |  | 
**cooldown_seconds** | **int** |  | [optional] 

## Example

```python
from omnismith_sdk.models.create_automation_request import CreateAutomationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAutomationRequest from a JSON string
create_automation_request_instance = CreateAutomationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAutomationRequest.to_json())

# convert the object into a dict
create_automation_request_dict = create_automation_request_instance.to_dict()
# create an instance of CreateAutomationRequest from a dict
create_automation_request_from_dict = CreateAutomationRequest.from_dict(create_automation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


