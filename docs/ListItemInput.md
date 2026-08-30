# ListItemInput

Specification for an individual list item option.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Display label / value for this choice option. | 
**sort_order** | **int** | Sorting rank for displaying this option in selection lists (lower numbers appear first). | [optional] [default to 0]
**id** | **UUID** | Optional explicit UUID for the list item. Generated automatically if omitted. | [optional] 

## Example

```python
from omnismith_sdk.models.list_item_input import ListItemInput

# TODO update the JSON string below
json = "{}"
# create an instance of ListItemInput from a JSON string
list_item_input_instance = ListItemInput.from_json(json)
# print the JSON string representation of the object
print(ListItemInput.to_json())

# convert the object into a dict
list_item_input_dict = list_item_input_instance.to_dict()
# create an instance of ListItemInput from a dict
list_item_input_from_dict = ListItemInput.from_dict(list_item_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


