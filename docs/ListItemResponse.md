# ListItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**attribute_id** | **UUID** |  | [optional] 
**value** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from omnismith_sdk.models.list_item_response import ListItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListItemResponse from a JSON string
list_item_response_instance = ListItemResponse.from_json(json)
# print the JSON string representation of the object
print(ListItemResponse.to_json())

# convert the object into a dict
list_item_response_dict = list_item_response_instance.to_dict()
# create an instance of ListItemResponse from a dict
list_item_response_from_dict = ListItemResponse.from_dict(list_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


