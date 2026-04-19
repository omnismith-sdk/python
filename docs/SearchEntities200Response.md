# SearchEntities200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EntityResponse]**](EntityResponse.md) |  | [optional] 
**total** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 

## Example

```python
from omnismith_sdk.models.search_entities200_response import SearchEntities200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchEntities200Response from a JSON string
search_entities200_response_instance = SearchEntities200Response.from_json(json)
# print the JSON string representation of the object
print(SearchEntities200Response.to_json())

# convert the object into a dict
search_entities200_response_dict = search_entities200_response_instance.to_dict()
# create an instance of SearchEntities200Response from a dict
search_entities200_response_from_dict = SearchEntities200Response.from_dict(search_entities200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


