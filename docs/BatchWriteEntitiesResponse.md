# BatchWriteEntitiesResponse

Summary counters plus the outcome of every operation, in the order submitted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**atomic** | **bool** | Whether the batch ran as a single transaction. | [optional] 
**total** | **int** | Number of operations submitted. | [optional] 
**created** | **int** | Number of entities created. | [optional] 
**updated** | **int** | Number of entities updated. | [optional] 
**replaced** | **int** | Number of entities replaced. | [optional] 
**deleted** | **int** | Number of entities soft-deleted. | [optional] 
**failed** | **int** | Number of operations that failed. Non-zero means the batch partially applied. | [optional] 
**results** | [**List[BatchOperationResult]**](BatchOperationResult.md) | One entry per submitted operation, in the submitted order. | [optional] 

## Example

```python
from omnismith_sdk.models.batch_write_entities_response import BatchWriteEntitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchWriteEntitiesResponse from a JSON string
batch_write_entities_response_instance = BatchWriteEntitiesResponse.from_json(json)
# print the JSON string representation of the object
print(BatchWriteEntitiesResponse.to_json())

# convert the object into a dict
batch_write_entities_response_dict = batch_write_entities_response_instance.to_dict()
# create an instance of BatchWriteEntitiesResponse from a dict
batch_write_entities_response_from_dict = BatchWriteEntitiesResponse.from_dict(batch_write_entities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


