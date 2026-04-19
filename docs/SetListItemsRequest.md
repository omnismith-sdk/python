# SetListItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ListItemInput]**](ListItemInput.md) |  | 

## Example

```python
from omnismith_sdk.models.set_list_items_request import SetListItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetListItemsRequest from a JSON string
set_list_items_request_instance = SetListItemsRequest.from_json(json)
# print the JSON string representation of the object
print(SetListItemsRequest.to_json())

# convert the object into a dict
set_list_items_request_dict = set_list_items_request_instance.to_dict()
# create an instance of SetListItemsRequest from a dict
set_list_items_request_from_dict = SetListItemsRequest.from_dict(set_list_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


