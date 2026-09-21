# EntityAttributesInputValueAnyOf

Backfill object: the same value plus the moment it was observed, for importing history.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**EntityAttributesInputValueAnyOfValue**](EntityAttributesInputValueAnyOfValue.md) |  | 
**updated_at** | **datetime** | RFC 3339 timestamp with an explicit offset (&#x60;Z&#x60; or &#x60;±HH:MM&#x60;). Defaults to now when omitted. | [optional] 

## Example

```python
from omnismith_sdk.models.entity_attributes_input_value_any_of import EntityAttributesInputValueAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of EntityAttributesInputValueAnyOf from a JSON string
entity_attributes_input_value_any_of_instance = EntityAttributesInputValueAnyOf.from_json(json)
# print the JSON string representation of the object
print(EntityAttributesInputValueAnyOf.to_json())

# convert the object into a dict
entity_attributes_input_value_any_of_dict = entity_attributes_input_value_any_of_instance.to_dict()
# create an instance of EntityAttributesInputValueAnyOf from a dict
entity_attributes_input_value_any_of_from_dict = EntityAttributesInputValueAnyOf.from_dict(entity_attributes_input_value_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


