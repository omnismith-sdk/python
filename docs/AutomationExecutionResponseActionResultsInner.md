# AutomationExecutionResponseActionResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_index** | **int** |  | [optional] 
**success** | **bool** |  | [optional] 
**error_message** | **str** |  | [optional] 
**executed_at** | **datetime** |  | [optional] 

## Example

```python
from omnismith_sdk.models.automation_execution_response_action_results_inner import AutomationExecutionResponseActionResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationExecutionResponseActionResultsInner from a JSON string
automation_execution_response_action_results_inner_instance = AutomationExecutionResponseActionResultsInner.from_json(json)
# print the JSON string representation of the object
print(AutomationExecutionResponseActionResultsInner.to_json())

# convert the object into a dict
automation_execution_response_action_results_inner_dict = automation_execution_response_action_results_inner_instance.to_dict()
# create an instance of AutomationExecutionResponseActionResultsInner from a dict
automation_execution_response_action_results_inner_from_dict = AutomationExecutionResponseActionResultsInner.from_dict(automation_execution_response_action_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


