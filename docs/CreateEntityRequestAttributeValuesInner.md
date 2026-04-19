# CreateEntityRequestAttributeValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **UUID** |  | [optional] 
**value** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from omnismith_sdk.models.create_entity_request_attribute_values_inner import CreateEntityRequestAttributeValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEntityRequestAttributeValuesInner from a JSON string
create_entity_request_attribute_values_inner_instance = CreateEntityRequestAttributeValuesInner.from_json(json)
# print the JSON string representation of the object
print(CreateEntityRequestAttributeValuesInner.to_json())

# convert the object into a dict
create_entity_request_attribute_values_inner_dict = create_entity_request_attribute_values_inner_instance.to_dict()
# create an instance of CreateEntityRequestAttributeValuesInner from a dict
create_entity_request_attribute_values_inner_from_dict = CreateEntityRequestAttributeValuesInner.from_dict(create_entity_request_attribute_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


