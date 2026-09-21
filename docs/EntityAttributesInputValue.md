# EntityAttributesInputValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | The operand, as a JSON number. | 
**updated_at** | **datetime** | RFC 3339 timestamp with an explicit offset (&#x60;Z&#x60; or &#x60;±HH:MM&#x60;). Defaults to now when omitted. | [optional] 
**op** | **str** | The operation. &#x60;increment&#x60; adds &#x60;value&#x60; (negative to subtract). | 

## Example

```python
from omnismith_sdk.models.entity_attributes_input_value import EntityAttributesInputValue

# TODO update the JSON string below
json = "{}"
# create an instance of EntityAttributesInputValue from a JSON string
entity_attributes_input_value_instance = EntityAttributesInputValue.from_json(json)
# print the JSON string representation of the object
print(EntityAttributesInputValue.to_json())

# convert the object into a dict
entity_attributes_input_value_dict = entity_attributes_input_value_instance.to_dict()
# create an instance of EntityAttributesInputValue from a dict
entity_attributes_input_value_from_dict = EntityAttributesInputValue.from_dict(entity_attributes_input_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


