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
**attribute_values** | [**EntityResponseAttributeValues**](EntityResponseAttributeValues.md) |  | [optional] 
**list_item_ids** | **Dict[str, UUID]** | Compact mode only: list option ids behind the labels shown in &#x60;attribute_values&#x60;, keyed like &#x60;attribute_values&#x60;. Use these ids when writing the attribute or filtering by it — writes and filters take ids, not labels. Absent when &#x60;verbose&#x3D;true&#x60; (the items carry &#x60;value&#x60;). | [optional] 
**reference_entity_ids** | **Dict[str, UUID]** | Compact mode only: referenced entity ids behind the labels shown in &#x60;attribute_values&#x60;, keyed like &#x60;attribute_values&#x60;. Pass one to &#x60;GET /entities/{id}&#x60; to load the referenced record, or use it when writing or filtering the attribute. Absent when &#x60;verbose&#x3D;true&#x60;. | [optional] 
**file_ids** | **Dict[str, UUID]** | Compact mode only: file attachment ids behind the filenames shown in &#x60;attribute_values&#x60;, keyed like &#x60;attribute_values&#x60;. Absent when &#x60;verbose&#x3D;true&#x60;. | [optional] 

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


