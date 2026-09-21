# EntityResponseAttributeValues

Attribute values of the entity. The shape depends on the `verbose` flag of the request: - default (compact): an object mapping attribute slug to the display value, e.g. `{\"price\": \"129.99\", \"status\": \"Open\", \"owner\": \"Platform team\"}`. List, reference and file attributes show their resolved label (list option label, referenced entity display value, original filename); the stored ids behind those labels are in `list_item_ids`, `reference_entity_ids` and `file_ids`. Attributes without a slug are keyed by their UUID. Attributes whose value is empty are omitted. - `verbose=true`: an array of `EntityAttributeValue` items, one per attribute (empty values included), each carrying the attribute `id`, `slug`, raw `value`, resolved `custom_value` and `reference_entity_id`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from omnismith_sdk.models.entity_response_attribute_values import EntityResponseAttributeValues

# TODO update the JSON string below
json = "{}"
# create an instance of EntityResponseAttributeValues from a JSON string
entity_response_attribute_values_instance = EntityResponseAttributeValues.from_json(json)
# print the JSON string representation of the object
print(EntityResponseAttributeValues.to_json())

# convert the object into a dict
entity_response_attribute_values_dict = entity_response_attribute_values_instance.to_dict()
# create an instance of EntityResponseAttributeValues from a dict
entity_response_attribute_values_from_dict = EntityResponseAttributeValues.from_dict(entity_response_attribute_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


