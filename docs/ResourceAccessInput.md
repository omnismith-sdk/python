# ResourceAccessInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** |  | 
**resource_id** | **UUID** |  | 
**access_level** | **str** |  | 

## Example

```python
from omnismith_sdk.models.resource_access_input import ResourceAccessInput

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceAccessInput from a JSON string
resource_access_input_instance = ResourceAccessInput.from_json(json)
# print the JSON string representation of the object
print(ResourceAccessInput.to_json())

# convert the object into a dict
resource_access_input_dict = resource_access_input_instance.to_dict()
# create an instance of ResourceAccessInput from a dict
resource_access_input_from_dict = ResourceAccessInput.from_dict(resource_access_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


