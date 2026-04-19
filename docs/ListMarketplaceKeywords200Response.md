# ListMarketplaceKeywords200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ListMarketplaceKeywords200ResponseDataInner]**](ListMarketplaceKeywords200ResponseDataInner.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.list_marketplace_keywords200_response import ListMarketplaceKeywords200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListMarketplaceKeywords200Response from a JSON string
list_marketplace_keywords200_response_instance = ListMarketplaceKeywords200Response.from_json(json)
# print the JSON string representation of the object
print(ListMarketplaceKeywords200Response.to_json())

# convert the object into a dict
list_marketplace_keywords200_response_dict = list_marketplace_keywords200_response_instance.to_dict()
# create an instance of ListMarketplaceKeywords200Response from a dict
list_marketplace_keywords200_response_from_dict = ListMarketplaceKeywords200Response.from_dict(list_marketplace_keywords200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


