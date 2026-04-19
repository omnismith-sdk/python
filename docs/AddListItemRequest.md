# AddListItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**sort_order** | **int** |  | [optional] 
**id** | **UUID** |  | [optional] 

## Example

```python
from omnismith_sdk.models.add_list_item_request import AddListItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddListItemRequest from a JSON string
add_list_item_request_instance = AddListItemRequest.from_json(json)
# print the JSON string representation of the object
print(AddListItemRequest.to_json())

# convert the object into a dict
add_list_item_request_dict = add_list_item_request_instance.to_dict()
# create an instance of AddListItemRequest from a dict
add_list_item_request_from_dict = AddListItemRequest.from_dict(add_list_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


