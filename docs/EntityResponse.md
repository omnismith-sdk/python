# EntityResponse

Hydrated dynamic entity record conforming to a template schema, including all dimension and metric attribute values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique entity identifier (UUIDv7) | [optional] 
**template_id** | **UUID** | UUID of the template schema to which this entity conforms | [optional] 
**template_slug** | **str** | Human-readable slug of the template schema | [optional] 
**created_at** | **datetime** | Record creation timestamp in ISO 8601 format | [optional] 
**updated_at** | **datetime** | Last modification timestamp in ISO 8601 format | [optional] 
**attribute_values** | [**Dict[str, EntityAttributeValue]**](EntityAttributeValue.md) | Dictionary of attribute values keyed by attribute UUID or attribute slug (controlled by the attribute_key query parameter) | [optional] 

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


