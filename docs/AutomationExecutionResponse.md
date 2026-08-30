# AutomationExecutionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique execution record UUID | [optional] 
**automation_id** | **UUID** | Associated automation rule UUID | [optional] 
**entity_id** | **UUID** | UUID of the entity that triggered the execution | [optional] 
**triggered_at** | **datetime** | Timestamp when the trigger event was evaluated | [optional] 
**completed_at** | **datetime** | Timestamp when all actions completed execution | [optional] 
**status** | **str** | Overall execution outcome status | [optional] 
**action_results** | [**List[AutomationExecutionResponseActionResultsInner]**](AutomationExecutionResponseActionResultsInner.md) | Individual action execution outcomes | [optional] 
**error_message** | **str** | Top-level error message if execution failed | [optional] 

## Example

```python
from omnismith_sdk.models.automation_execution_response import AutomationExecutionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationExecutionResponse from a JSON string
automation_execution_response_instance = AutomationExecutionResponse.from_json(json)
# print the JSON string representation of the object
print(AutomationExecutionResponse.to_json())

# convert the object into a dict
automation_execution_response_dict = automation_execution_response_instance.to_dict()
# create an instance of AutomationExecutionResponse from a dict
automation_execution_response_from_dict = AutomationExecutionResponse.from_dict(automation_execution_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


