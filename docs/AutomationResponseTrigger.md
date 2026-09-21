# AutomationResponseTrigger

Event trigger configuration defining when this automation fires

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Trigger event type. &#x60;on_action_executed&#x60; fires when the named entity action runs on a record, whether or not the write changed anything. | [optional] 
**template_id** | **UUID** | Target template UUID | [optional] 
**attribute_id** | **UUID** | Target attribute UUID for attribute change triggers | [optional] 
**action_id** | **UUID** | Entity action UUID; required for &#x60;on_action_executed&#x60;, must be null otherwise | [optional] 

## Example

```python
from omnismith_sdk.models.automation_response_trigger import AutomationResponseTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationResponseTrigger from a JSON string
automation_response_trigger_instance = AutomationResponseTrigger.from_json(json)
# print the JSON string representation of the object
print(AutomationResponseTrigger.to_json())

# convert the object into a dict
automation_response_trigger_dict = automation_response_trigger_instance.to_dict()
# create an instance of AutomationResponseTrigger from a dict
automation_response_trigger_from_dict = AutomationResponseTrigger.from_dict(automation_response_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


