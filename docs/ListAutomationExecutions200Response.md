# ListAutomationExecutions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AutomationExecutionResponse]**](AutomationExecutionResponse.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from omnismith_sdk.models.list_automation_executions200_response import ListAutomationExecutions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAutomationExecutions200Response from a JSON string
list_automation_executions200_response_instance = ListAutomationExecutions200Response.from_json(json)
# print the JSON string representation of the object
print(ListAutomationExecutions200Response.to_json())

# convert the object into a dict
list_automation_executions200_response_dict = list_automation_executions200_response_instance.to_dict()
# create an instance of ListAutomationExecutions200Response from a dict
list_automation_executions200_response_from_dict = ListAutomationExecutions200Response.from_dict(list_automation_executions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


