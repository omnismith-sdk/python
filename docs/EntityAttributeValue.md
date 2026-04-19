# EntityAttributeValue

Structured attribute value including display/custom value for references

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**custom_value** | **str** |  | [optional] 
**reference_entity_id** | **UUID** |  | [optional] 

## Example

```python
from omnismith_sdk.models.entity_attribute_value import EntityAttributeValue

# TODO update the JSON string below
json = "{}"
# create an instance of EntityAttributeValue from a JSON string
entity_attribute_value_instance = EntityAttributeValue.from_json(json)
# print the JSON string representation of the object
print(EntityAttributeValue.to_json())

# convert the object into a dict
entity_attribute_value_dict = entity_attribute_value_instance.to_dict()
# create an instance of EntityAttributeValue from a dict
entity_attribute_value_from_dict = EntityAttributeValue.from_dict(entity_attribute_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


