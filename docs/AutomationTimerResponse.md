# AutomationTimerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Timer UUID. There is at most one pending timer per automation, record and kind, so re-arming keeps the id. | 
**automation_id** | **UUID** | Automation the timer belongs to | 
**automation_name** | **str** | Name of that automation | 
**entity_id** | **UUID** | Record the timer is about; null for a timer that belongs to no record (a schedule without a template) | 
**kind** | **str** | What the timer is for: the next slot of a schedule, a date attribute reaching its moment, or a \&quot;no change within\&quot; deadline | 
**due_at** | **datetime** | When the timer fires (UTC). It fires within about 30 seconds of this moment; one that came due while the service was down fires once, late. | 

## Example

```python
from omnismith_sdk.models.automation_timer_response import AutomationTimerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationTimerResponse from a JSON string
automation_timer_response_instance = AutomationTimerResponse.from_json(json)
# print the JSON string representation of the object
print(AutomationTimerResponse.to_json())

# convert the object into a dict
automation_timer_response_dict = automation_timer_response_instance.to_dict()
# create an instance of AutomationTimerResponse from a dict
automation_timer_response_from_dict = AutomationTimerResponse.from_dict(automation_timer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


