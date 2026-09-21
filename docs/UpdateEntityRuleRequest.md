# UpdateEntityRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Short name shown in the template editor | 
**message** | **str** | Text returned to the client when the rule is violated | 
**when** | [**List[EntityRulePredicate]**](EntityRulePredicate.md) | Full replacement of the activation conditions; empty for an unconditional rule | [optional] 
**then** | [**List[EntityRulePredicate]**](EntityRulePredicate.md) | Full replacement of the constraints | 

## Example

```python
from omnismith_sdk.models.update_entity_rule_request import UpdateEntityRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEntityRuleRequest from a JSON string
update_entity_rule_request_instance = UpdateEntityRuleRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateEntityRuleRequest.to_json())

# convert the object into a dict
update_entity_rule_request_dict = update_entity_rule_request_instance.to_dict()
# create an instance of UpdateEntityRuleRequest from a dict
update_entity_rule_request_from_dict = UpdateEntityRuleRequest.from_dict(update_entity_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


