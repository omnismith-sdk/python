# AutomationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**trigger** | [**AutomationResponseTrigger**](AutomationResponseTrigger.md) |  | [optional] 
**conditions** | [**List[AutomationResponseConditionsInner]**](AutomationResponseConditionsInner.md) |  | [optional] 
**actions** | [**List[AutomationResponseActionsInner]**](AutomationResponseActionsInner.md) |  | [optional] 
**cooldown_seconds** | **int** |  | [optional] 
**last_triggered_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from omnismith_sdk.models.automation_response import AutomationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationResponse from a JSON string
automation_response_instance = AutomationResponse.from_json(json)
# print the JSON string representation of the object
print(AutomationResponse.to_json())

# convert the object into a dict
automation_response_dict = automation_response_instance.to_dict()
# create an instance of AutomationResponse from a dict
automation_response_from_dict = AutomationResponse.from_dict(automation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


