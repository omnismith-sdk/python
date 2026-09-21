# BatchExecuteEntityActionResponse

Summary counters plus the outcome for every record, in the order submitted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**atomic** | **bool** | Whether the batch ran as a single transaction. | 
**total** | **int** | Number of records submitted. | 
**executed** | **int** | Records the action ran on. | 
**precondition_failed** | **int** | Records skipped because the precondition did not hold. | 
**rule_violated** | **int** | Records refused by a template rule. | 
**failed** | **int** | Records refused for any other reason. | 
**results** | [**List[EntityActionOutcome]**](EntityActionOutcome.md) |  | 

## Example

```python
from omnismith_sdk.models.batch_execute_entity_action_response import BatchExecuteEntityActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchExecuteEntityActionResponse from a JSON string
batch_execute_entity_action_response_instance = BatchExecuteEntityActionResponse.from_json(json)
# print the JSON string representation of the object
print(BatchExecuteEntityActionResponse.to_json())

# convert the object into a dict
batch_execute_entity_action_response_dict = batch_execute_entity_action_response_instance.to_dict()
# create an instance of BatchExecuteEntityActionResponse from a dict
batch_execute_entity_action_response_from_dict = BatchExecuteEntityActionResponse.from_dict(batch_execute_entity_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


