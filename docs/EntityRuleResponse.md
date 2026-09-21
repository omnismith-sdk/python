# EntityRuleResponse

A template-scoped business rule: when every `when` condition holds (an empty list always holds), every `then` constraint must hold or the write is rejected with 422.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Rule UUID | [optional] 
**template_id** | **UUID** | UUID of the template the rule belongs to | [optional] 
**name** | **str** | Short name shown in the template editor | [optional] 
**message** | **str** | Text returned to the client when the rule is violated | [optional] 
**is_enabled** | **bool** | Disabled rules are stored but not enforced | [optional] 
**when** | [**List[EntityRulePredicate]**](EntityRulePredicate.md) | Conditions that activate the rule; all must hold. Empty means the rule is unconditional. | [optional] 
**then** | [**List[EntityRulePredicate]**](EntityRulePredicate.md) | Constraints that must hold once the rule is active; at least one. Each failing constraint yields an &#x60;attributes.&lt;slug&gt;&#x60; error. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from omnismith_sdk.models.entity_rule_response import EntityRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntityRuleResponse from a JSON string
entity_rule_response_instance = EntityRuleResponse.from_json(json)
# print the JSON string representation of the object
print(EntityRuleResponse.to_json())

# convert the object into a dict
entity_rule_response_dict = entity_rule_response_instance.to_dict()
# create an instance of EntityRuleResponse from a dict
entity_rule_response_from_dict = EntityRuleResponse.from_dict(entity_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


