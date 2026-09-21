# EntityRuleOverviewResponse

Template-scoped validation rule. All writes must satisfy active rules.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Rule UUID | 
**name** | **str** | Short rule name | 
**message** | **str** | Error message returned on violation | 
**is_enabled** | **bool** | Whether the rule is actively enforced | 
**when** | [**List[EntityRulePredicateOverviewResponse]**](EntityRulePredicateOverviewResponse.md) | Activating conditions; empty means unconditional | 
**then** | [**List[EntityRulePredicateOverviewResponse]**](EntityRulePredicateOverviewResponse.md) | Enforced constraints | 

## Example

```python
from omnismith_sdk.models.entity_rule_overview_response import EntityRuleOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntityRuleOverviewResponse from a JSON string
entity_rule_overview_response_instance = EntityRuleOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(EntityRuleOverviewResponse.to_json())

# convert the object into a dict
entity_rule_overview_response_dict = entity_rule_overview_response_instance.to_dict()
# create an instance of EntityRuleOverviewResponse from a dict
entity_rule_overview_response_from_dict = EntityRuleOverviewResponse.from_dict(entity_rule_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


