# AutomationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique automation UUID | [optional] 
**name** | **str** | Name of the automation rule | [optional] 
**description** | **str** | Optional description of the automation rule | [optional] 
**is_enabled** | **bool** | Whether the automation is currently active and listening for events | [optional] 
**trigger** | [**AutomationResponseTrigger**](AutomationResponseTrigger.md) |  | [optional] 
**conditions** | [**List[AutomationResponseConditionsInner]**](AutomationResponseConditionsInner.md) | Condition expressions that must all evaluate to true to execute actions | [optional] 
**actions** | [**List[AutomationResponseActionsInner]**](AutomationResponseActionsInner.md) | Actions dispatched when conditions evaluate to true | [optional] 
**cooldown_seconds** | **int** | Minimum cooldown seconds between trigger firings for the same entity | [optional] 
**last_triggered_at** | **datetime** | Timestamp when this automation last fired | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

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


