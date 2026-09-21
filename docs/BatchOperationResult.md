# BatchOperationResult

The outcome of a single operation. On failure, `error` carries the same body the equivalent single-entity endpoint would have returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Position of this operation in the submitted array. | [optional] 
**op** | **str** | The operation that was attempted. | [optional] 
**id** | **UUID** | Entity the operation acted on. For a successful create this is the newly generated identifier. Null when a create failed before an identifier existed. | [optional] 
**status** | **str** | Outcome of this operation. | [optional] 
**error** | [**ErrorResponse**](ErrorResponse.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.batch_operation_result import BatchOperationResult

# TODO update the JSON string below
json = "{}"
# create an instance of BatchOperationResult from a JSON string
batch_operation_result_instance = BatchOperationResult.from_json(json)
# print the JSON string representation of the object
print(BatchOperationResult.to_json())

# convert the object into a dict
batch_operation_result_dict = batch_operation_result_instance.to_dict()
# create an instance of BatchOperationResult from a dict
batch_operation_result_from_dict = BatchOperationResult.from_dict(batch_operation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


