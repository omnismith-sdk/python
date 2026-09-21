# ListItemLayoutResponse

Display sorting rank for a choice option item in UI dropdowns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_item_id** | **UUID** | List item UUID | 
**attribute_id** | **UUID** | Parent attribute UUID | 
**sort_order** | **int** | Display sorting rank in selection menus | 

## Example

```python
from omnismith_sdk.models.list_item_layout_response import ListItemLayoutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListItemLayoutResponse from a JSON string
list_item_layout_response_instance = ListItemLayoutResponse.from_json(json)
# print the JSON string representation of the object
print(ListItemLayoutResponse.to_json())

# convert the object into a dict
list_item_layout_response_dict = list_item_layout_response_instance.to_dict()
# create an instance of ListItemLayoutResponse from a dict
list_item_layout_response_from_dict = ListItemLayoutResponse.from_dict(list_item_layout_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


