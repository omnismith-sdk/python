# ResolvedStatBlockResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_id** | **UUID** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from omnismith_sdk.models.resolved_stat_block_response import ResolvedStatBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedStatBlockResponse from a JSON string
resolved_stat_block_response_instance = ResolvedStatBlockResponse.from_json(json)
# print the JSON string representation of the object
print(ResolvedStatBlockResponse.to_json())

# convert the object into a dict
resolved_stat_block_response_dict = resolved_stat_block_response_instance.to_dict()
# create an instance of ResolvedStatBlockResponse from a dict
resolved_stat_block_response_from_dict = ResolvedStatBlockResponse.from_dict(resolved_stat_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


