# AutomationResponseTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**template_id** | **UUID** |  | [optional] 
**attribute_id** | **UUID** |  | [optional] 

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


