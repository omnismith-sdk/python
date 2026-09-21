# EntityAttributesInputValueAnyOf1

Operation object: apply an atomic operation to the stored value instead of overwriting it. Number attributes and metrics only; a never-set value counts as 0.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | The operation. &#x60;increment&#x60; adds &#x60;value&#x60; (negative to subtract). | 
**value** | **float** | The operand, as a JSON number. | 

## Example

```python
from omnismith_sdk.models.entity_attributes_input_value_any_of1 import EntityAttributesInputValueAnyOf1

# TODO update the JSON string below
json = "{}"
# create an instance of EntityAttributesInputValueAnyOf1 from a JSON string
entity_attributes_input_value_any_of1_instance = EntityAttributesInputValueAnyOf1.from_json(json)
# print the JSON string representation of the object
print(EntityAttributesInputValueAnyOf1.to_json())

# convert the object into a dict
entity_attributes_input_value_any_of1_dict = entity_attributes_input_value_any_of1_instance.to_dict()
# create an instance of EntityAttributesInputValueAnyOf1 from a dict
entity_attributes_input_value_any_of1_from_dict = EntityAttributesInputValueAnyOf1.from_dict(entity_attributes_input_value_any_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


