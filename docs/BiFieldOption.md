# BiFieldOption

Allowed option for list-type BI fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | List option UUID | [optional] 
**value** | **str** | Display label of the list option | [optional] 
**sort_order** | **int** | Display sort order index | [optional] 

## Example

```python
from omnismith_sdk.models.bi_field_option import BiFieldOption

# TODO update the JSON string below
json = "{}"
# create an instance of BiFieldOption from a JSON string
bi_field_option_instance = BiFieldOption.from_json(json)
# print the JSON string representation of the object
print(BiFieldOption.to_json())

# convert the object into a dict
bi_field_option_dict = bi_field_option_instance.to_dict()
# create an instance of BiFieldOption from a dict
bi_field_option_from_dict = BiFieldOption.from_dict(bi_field_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


