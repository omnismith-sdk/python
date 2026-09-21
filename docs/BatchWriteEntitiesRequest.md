# BatchWriteEntitiesRequest

An ordered, mixed list of entity writes applied in one call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operations** | [**List[BatchOperationInput]**](BatchOperationInput.md) | Operations applied in the order given, at most 100 per call. | 
**atomic** | **bool** | When false (the default) every operation is attempted and failures are reported per index. When true the batch runs in a single transaction and the first failure rolls all of it back. Atomic batches reject metric values, which are published outside the transaction and cannot be rolled back. | [optional] [default to False]

## Example

```python
from omnismith_sdk.models.batch_write_entities_request import BatchWriteEntitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchWriteEntitiesRequest from a JSON string
batch_write_entities_request_instance = BatchWriteEntitiesRequest.from_json(json)
# print the JSON string representation of the object
print(BatchWriteEntitiesRequest.to_json())

# convert the object into a dict
batch_write_entities_request_dict = batch_write_entities_request_instance.to_dict()
# create an instance of BatchWriteEntitiesRequest from a dict
batch_write_entities_request_from_dict = BatchWriteEntitiesRequest.from_dict(batch_write_entities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


