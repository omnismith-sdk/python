# EntityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**attribute_values** | [**Dict[str, EntityAttributeValue]**](EntityAttributeValue.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.entity_response import EntityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntityResponse from a JSON string
entity_response_instance = EntityResponse.from_json(json)
# print the JSON string representation of the object
print(EntityResponse.to_json())

# convert the object into a dict
entity_response_dict = entity_response_instance.to_dict()
# create an instance of EntityResponse from a dict
entity_response_from_dict = EntityResponse.from_dict(entity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


