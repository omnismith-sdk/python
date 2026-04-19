# CreateAutomationRequestConditionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **UUID** |  | 
**operator** | **str** |  | 
**value** | **object** |  | [optional] 
**mode** | **str** |  | 

## Example

```python
from omnismith_sdk.models.create_automation_request_conditions_inner import CreateAutomationRequestConditionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAutomationRequestConditionsInner from a JSON string
create_automation_request_conditions_inner_instance = CreateAutomationRequestConditionsInner.from_json(json)
# print the JSON string representation of the object
print(CreateAutomationRequestConditionsInner.to_json())

# convert the object into a dict
create_automation_request_conditions_inner_dict = create_automation_request_conditions_inner_instance.to_dict()
# create an instance of CreateAutomationRequestConditionsInner from a dict
create_automation_request_conditions_inner_from_dict = CreateAutomationRequestConditionsInner.from_dict(create_automation_request_conditions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


