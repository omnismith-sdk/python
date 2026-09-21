# EntityRulePredicateOverviewResponse

Predicate condition or constraint evaluating an entity attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **UUID** | Attribute UUID | 
**attribute_slug** | **str** | Attribute slug identifier | [optional] 
**operator** | **str** | Comparison operator: eq, neq, gt, gte, lt, lte, contains, not_contains, in, is_empty, is_not_empty | 
**value** | [**EntityRulePredicateOverviewResponseValue**](EntityRulePredicateOverviewResponseValue.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.entity_rule_predicate_overview_response import EntityRulePredicateOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntityRulePredicateOverviewResponse from a JSON string
entity_rule_predicate_overview_response_instance = EntityRulePredicateOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(EntityRulePredicateOverviewResponse.to_json())

# convert the object into a dict
entity_rule_predicate_overview_response_dict = entity_rule_predicate_overview_response_instance.to_dict()
# create an instance of EntityRulePredicateOverviewResponse from a dict
entity_rule_predicate_overview_response_from_dict = EntityRulePredicateOverviewResponse.from_dict(entity_rule_predicate_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


