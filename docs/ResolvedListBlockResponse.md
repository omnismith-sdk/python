# ResolvedListBlockResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_id** | **UUID** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**items** | [**List[ResolvedListBlockResponseItemsInner]**](ResolvedListBlockResponseItemsInner.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from omnismith_sdk.models.resolved_list_block_response import ResolvedListBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedListBlockResponse from a JSON string
resolved_list_block_response_instance = ResolvedListBlockResponse.from_json(json)
# print the JSON string representation of the object
print(ResolvedListBlockResponse.to_json())

# convert the object into a dict
resolved_list_block_response_dict = resolved_list_block_response_instance.to_dict()
# create an instance of ResolvedListBlockResponse from a dict
resolved_list_block_response_from_dict = ResolvedListBlockResponse.from_dict(resolved_list_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


