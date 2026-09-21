# EntityRulePredicate

One predicate over an attribute's current value. Used both as a `when` condition and as a `then` constraint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **UUID** | Attribute UUID the predicate reads | 
**operator** | **str** | Comparison operator. &#x60;gt&#x60;/&#x60;gte&#x60;/&#x60;lt&#x60;/&#x60;lte&#x60; apply to number and date attributes, &#x60;contains&#x60;/&#x60;not_contains&#x60; to text, &#x60;in&#x60; to list attributes (value is a list of list item UUIDs), &#x60;eq&#x60;/&#x60;neq&#x60;/&#x60;is_empty&#x60;/&#x60;is_not_empty&#x60; to every non-metric attribute. | 
**value** | [**EntityRulePredicateValue**](EntityRulePredicateValue.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.entity_rule_predicate import EntityRulePredicate

# TODO update the JSON string below
json = "{}"
# create an instance of EntityRulePredicate from a JSON string
entity_rule_predicate_instance = EntityRulePredicate.from_json(json)
# print the JSON string representation of the object
print(EntityRulePredicate.to_json())

# convert the object into a dict
entity_rule_predicate_dict = entity_rule_predicate_instance.to_dict()
# create an instance of EntityRulePredicate from a dict
entity_rule_predicate_from_dict = EntityRulePredicate.from_dict(entity_rule_predicate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


