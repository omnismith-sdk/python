# UpdateAutomationRequestTrigger

Updated event trigger criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Trigger event type | [optional] 
**template_id** | **UUID** | Template UUID | [optional] 
**attribute_id** | **UUID** | Attribute UUID for attribute change triggers | [optional] 

## Example

```python
from omnismith_sdk.models.update_automation_request_trigger import UpdateAutomationRequestTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAutomationRequestTrigger from a JSON string
update_automation_request_trigger_instance = UpdateAutomationRequestTrigger.from_json(json)
# print the JSON string representation of the object
print(UpdateAutomationRequestTrigger.to_json())

# convert the object into a dict
update_automation_request_trigger_dict = update_automation_request_trigger_instance.to_dict()
# create an instance of UpdateAutomationRequestTrigger from a dict
update_automation_request_trigger_from_dict = UpdateAutomationRequestTrigger.from_dict(update_automation_request_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


