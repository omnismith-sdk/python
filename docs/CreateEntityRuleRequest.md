# CreateEntityRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Short name shown in the template editor | 
**message** | **str** | Text returned to the client when the rule is violated | 
**when** | [**List[EntityRulePredicate]**](EntityRulePredicate.md) | Conditions that activate the rule; all must hold. Omit or send an empty list for an unconditional rule (a plain required field). | [optional] 
**then** | [**List[EntityRulePredicate]**](EntityRulePredicate.md) | Constraints that must hold once the rule is active. &#x60;is_not_empty&#x60; on an attribute is the \&quot;required\&quot; constraint. | 

## Example

```python
from omnismith_sdk.models.create_entity_rule_request import CreateEntityRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEntityRuleRequest from a JSON string
create_entity_rule_request_instance = CreateEntityRuleRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEntityRuleRequest.to_json())

# convert the object into a dict
create_entity_rule_request_dict = create_entity_rule_request_instance.to_dict()
# create an instance of CreateEntityRuleRequest from a dict
create_entity_rule_request_from_dict = CreateEntityRuleRequest.from_dict(create_entity_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


