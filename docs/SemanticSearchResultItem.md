# SemanticSearchResultItem

Entity search match ranked by cosine similarity score

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**EntityResponse**](EntityResponse.md) |  | [optional] 
**similarity_score** | **float** | Cosine similarity score (0.0 to 1.0, where 1.0 is exact match) | [optional] 

## Example

```python
from omnismith_sdk.models.semantic_search_result_item import SemanticSearchResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of SemanticSearchResultItem from a JSON string
semantic_search_result_item_instance = SemanticSearchResultItem.from_json(json)
# print the JSON string representation of the object
print(SemanticSearchResultItem.to_json())

# convert the object into a dict
semantic_search_result_item_dict = semantic_search_result_item_instance.to_dict()
# create an instance of SemanticSearchResultItem from a dict
semantic_search_result_item_from_dict = SemanticSearchResultItem.from_dict(semantic_search_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


