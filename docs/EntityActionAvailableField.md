# EntityActionAvailableField

One value the action asks for, resolved to the attribute it writes. Send it under `values` keyed by `slug` (or `attribute_id`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **UUID** |  | 
**slug** | **str** | Attribute slug; the key to use in &#x60;values&#x60;. Null for an attribute without a slug — use &#x60;attribute_id&#x60; then. | 
**name** | **str** |  | 
**attribute_type** | **int** | 0: Dimension, 2: List, 3: Reference (metrics are never action fields) | 
**data_type** | **int** | 0: String, 1: Number, 2: Boolean, 3: Datetime, 4: Date, 5: File, 6: Image, 7: Markdown | 
**required** | **bool** | Execution refuses an empty value with 422 keyed by &#x60;attributes.&lt;slug&gt;&#x60; | 
**hint** | **str** |  | 
**list_items** | [**List[EntityActionAvailableFieldListItemsInner]**](EntityActionAvailableFieldListItemsInner.md) | The choices of a list attribute; the value to send is the item &#x60;id&#x60;. Empty for other attribute types. | 
**reference_config** | [**EntityActionAvailableFieldReferenceConfig**](EntityActionAvailableFieldReferenceConfig.md) |  | 

## Example

```python
from omnismith_sdk.models.entity_action_available_field import EntityActionAvailableField

# TODO update the JSON string below
json = "{}"
# create an instance of EntityActionAvailableField from a JSON string
entity_action_available_field_instance = EntityActionAvailableField.from_json(json)
# print the JSON string representation of the object
print(EntityActionAvailableField.to_json())

# convert the object into a dict
entity_action_available_field_dict = entity_action_available_field_instance.to_dict()
# create an instance of EntityActionAvailableField from a dict
entity_action_available_field_from_dict = EntityActionAvailableField.from_dict(entity_action_available_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


