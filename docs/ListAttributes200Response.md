# ListAttributes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AttributeResponse]**](AttributeResponse.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.list_attributes200_response import ListAttributes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAttributes200Response from a JSON string
list_attributes200_response_instance = ListAttributes200Response.from_json(json)
# print the JSON string representation of the object
print(ListAttributes200Response.to_json())

# convert the object into a dict
list_attributes200_response_dict = list_attributes200_response_instance.to_dict()
# create an instance of ListAttributes200Response from a dict
list_attributes200_response_from_dict = ListAttributes200Response.from_dict(list_attributes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


