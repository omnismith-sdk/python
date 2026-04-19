# ListAttributeItems200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ListItemResponse]**](ListItemResponse.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.list_attribute_items200_response import ListAttributeItems200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAttributeItems200Response from a JSON string
list_attribute_items200_response_instance = ListAttributeItems200Response.from_json(json)
# print the JSON string representation of the object
print(ListAttributeItems200Response.to_json())

# convert the object into a dict
list_attribute_items200_response_dict = list_attribute_items200_response_instance.to_dict()
# create an instance of ListAttributeItems200Response from a dict
list_attribute_items200_response_from_dict = ListAttributeItems200Response.from_dict(list_attribute_items200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


