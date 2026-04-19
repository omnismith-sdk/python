# ResolvedGaugeBlockResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_id** | **UUID** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**percentage** | **float** |  | [optional] 

## Example

```python
from omnismith_sdk.models.resolved_gauge_block_response import ResolvedGaugeBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedGaugeBlockResponse from a JSON string
resolved_gauge_block_response_instance = ResolvedGaugeBlockResponse.from_json(json)
# print the JSON string representation of the object
print(ResolvedGaugeBlockResponse.to_json())

# convert the object into a dict
resolved_gauge_block_response_dict = resolved_gauge_block_response_instance.to_dict()
# create an instance of ResolvedGaugeBlockResponse from a dict
resolved_gauge_block_response_from_dict = ResolvedGaugeBlockResponse.from_dict(resolved_gauge_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


