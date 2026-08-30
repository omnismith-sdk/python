# CreateAutomationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Descriptive display name of the automation rule | 
**description** | **str** | Optional summary describing the purpose and behavior of the automation | [optional] 
**trigger** | [**CreateAutomationRequestTrigger**](CreateAutomationRequestTrigger.md) |  | 
**conditions** | [**List[CreateAutomationRequestConditionsInner]**](CreateAutomationRequestConditionsInner.md) | Condition expressions that must all evaluate to true against the entity for actions to run | 
**actions** | [**List[CreateAutomationRequestActionsInner]**](CreateAutomationRequestActionsInner.md) | List of dispatch actions to execute when trigger and conditions are met | 
**cooldown_seconds** | **int** | Minimum throttle cooldown window in seconds between firings for the same entity | [optional] 

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


