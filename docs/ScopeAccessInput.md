# ScopeAccessInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **UUID** |  | 
**conditions** | [**List[ScopeConditionInput]**](ScopeConditionInput.md) |  | 

## Example

```python
from omnismith_sdk.models.scope_access_input import ScopeAccessInput

# TODO update the JSON string below
json = "{}"
# create an instance of ScopeAccessInput from a JSON string
scope_access_input_instance = ScopeAccessInput.from_json(json)
# print the JSON string representation of the object
print(ScopeAccessInput.to_json())

# convert the object into a dict
scope_access_input_dict = scope_access_input_instance.to_dict()
# create an instance of ScopeAccessInput from a dict
scope_access_input_from_dict = ScopeAccessInput.from_dict(scope_access_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


