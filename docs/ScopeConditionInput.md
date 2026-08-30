# ScopeConditionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Attribute id or a standard entity field (id, created_at, updated_at) | 
**operator** | **str** |  | 
**value** | **str** |  | [optional] 

## Example

```python
from omnismith_sdk.models.scope_condition_input import ScopeConditionInput

# TODO update the JSON string below
json = "{}"
# create an instance of ScopeConditionInput from a JSON string
scope_condition_input_instance = ScopeConditionInput.from_json(json)
# print the JSON string representation of the object
print(ScopeConditionInput.to_json())

# convert the object into a dict
scope_condition_input_dict = scope_condition_input_instance.to_dict()
# create an instance of ScopeConditionInput from a dict
scope_condition_input_from_dict = ScopeConditionInput.from_dict(scope_condition_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


