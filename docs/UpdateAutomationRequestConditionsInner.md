# UpdateAutomationRequestConditionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **UUID** | Attribute UUID to evaluate | [optional] 
**operator** | **str** | Comparison operator | [optional] 
**value** | **object** | Expected comparison value | [optional] 
**mode** | **str** | Evaluation mode: current value, absolute numeric change, or percentage change | [optional] 

## Example

```python
from omnismith_sdk.models.update_automation_request_conditions_inner import UpdateAutomationRequestConditionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAutomationRequestConditionsInner from a JSON string
update_automation_request_conditions_inner_instance = UpdateAutomationRequestConditionsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateAutomationRequestConditionsInner.to_json())

# convert the object into a dict
update_automation_request_conditions_inner_dict = update_automation_request_conditions_inner_instance.to_dict()
# create an instance of UpdateAutomationRequestConditionsInner from a dict
update_automation_request_conditions_inner_from_dict = UpdateAutomationRequestConditionsInner.from_dict(update_automation_request_conditions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


