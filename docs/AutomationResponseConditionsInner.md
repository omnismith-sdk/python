# AutomationResponseConditionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **UUID** |  | [optional] 
**operator** | **str** |  | [optional] 
**value** | **object** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from omnismith_sdk.models.automation_response_conditions_inner import AutomationResponseConditionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationResponseConditionsInner from a JSON string
automation_response_conditions_inner_instance = AutomationResponseConditionsInner.from_json(json)
# print the JSON string representation of the object
print(AutomationResponseConditionsInner.to_json())

# convert the object into a dict
automation_response_conditions_inner_dict = automation_response_conditions_inner_instance.to_dict()
# create an instance of AutomationResponseConditionsInner from a dict
automation_response_conditions_inner_from_dict = AutomationResponseConditionsInner.from_dict(automation_response_conditions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


