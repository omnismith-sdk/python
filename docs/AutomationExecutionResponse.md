# AutomationExecutionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**automation_id** | **UUID** |  | [optional] 
**entity_id** | **UUID** |  | [optional] 
**triggered_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**action_results** | [**List[AutomationExecutionResponseActionResultsInner]**](AutomationExecutionResponseActionResultsInner.md) |  | [optional] 
**error_message** | **str** |  | [optional] 

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


