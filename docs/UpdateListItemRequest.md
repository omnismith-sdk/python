# UpdateListItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**sort_order** | **int** |  | [optional] 

## Example

```python
from omnismith_sdk.models.update_list_item_request import UpdateListItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateListItemRequest from a JSON string
update_list_item_request_instance = UpdateListItemRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateListItemRequest.to_json())

# convert the object into a dict
update_list_item_request_dict = update_list_item_request_instance.to_dict()
# create an instance of UpdateListItemRequest from a dict
update_list_item_request_from_dict = UpdateListItemRequest.from_dict(update_list_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


