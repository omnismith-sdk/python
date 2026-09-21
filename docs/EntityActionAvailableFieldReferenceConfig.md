# EntityActionAvailableFieldReferenceConfig

For reference attributes, the template whose entities are valid values; the value to send is an entity id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_template_id** | **UUID** |  | 
**target_attribute_id** | **UUID** |  | 

## Example

```python
from omnismith_sdk.models.entity_action_available_field_reference_config import EntityActionAvailableFieldReferenceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EntityActionAvailableFieldReferenceConfig from a JSON string
entity_action_available_field_reference_config_instance = EntityActionAvailableFieldReferenceConfig.from_json(json)
# print the JSON string representation of the object
print(EntityActionAvailableFieldReferenceConfig.to_json())

# convert the object into a dict
entity_action_available_field_reference_config_dict = entity_action_available_field_reference_config_instance.to_dict()
# create an instance of EntityActionAvailableFieldReferenceConfig from a dict
entity_action_available_field_reference_config_from_dict = EntityActionAvailableFieldReferenceConfig.from_dict(entity_action_available_field_reference_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


