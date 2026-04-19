# CreateAutomationRequestTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**template_id** | **UUID** |  | [optional] 
**attribute_id** | **UUID** |  | [optional] 

## Example

```python
from omnismith_sdk.models.create_automation_request_trigger import CreateAutomationRequestTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAutomationRequestTrigger from a JSON string
create_automation_request_trigger_instance = CreateAutomationRequestTrigger.from_json(json)
# print the JSON string representation of the object
print(CreateAutomationRequestTrigger.to_json())

# convert the object into a dict
create_automation_request_trigger_dict = create_automation_request_trigger_instance.to_dict()
# create an instance of CreateAutomationRequestTrigger from a dict
create_automation_request_trigger_from_dict = CreateAutomationRequestTrigger.from_dict(create_automation_request_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


