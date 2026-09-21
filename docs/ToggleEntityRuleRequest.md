# ToggleEntityRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Whether the rule is enforced | 

## Example

```python
from omnismith_sdk.models.toggle_entity_rule_request import ToggleEntityRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ToggleEntityRuleRequest from a JSON string
toggle_entity_rule_request_instance = ToggleEntityRuleRequest.from_json(json)
# print the JSON string representation of the object
print(ToggleEntityRuleRequest.to_json())

# convert the object into a dict
toggle_entity_rule_request_dict = toggle_entity_rule_request_instance.to_dict()
# create an instance of ToggleEntityRuleRequest from a dict
toggle_entity_rule_request_from_dict = ToggleEntityRuleRequest.from_dict(toggle_entity_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


