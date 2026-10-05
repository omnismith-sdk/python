# ListAutomationTimers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AutomationTimerResponse]**](AutomationTimerResponse.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.list_automation_timers200_response import ListAutomationTimers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAutomationTimers200Response from a JSON string
list_automation_timers200_response_instance = ListAutomationTimers200Response.from_json(json)
# print the JSON string representation of the object
print(ListAutomationTimers200Response.to_json())

# convert the object into a dict
list_automation_timers200_response_dict = list_automation_timers200_response_instance.to_dict()
# create an instance of ListAutomationTimers200Response from a dict
list_automation_timers200_response_from_dict = ListAutomationTimers200Response.from_dict(list_automation_timers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


