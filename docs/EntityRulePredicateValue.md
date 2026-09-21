# EntityRulePredicateValue

Comparison value serialized as a string (list item UUID for list attributes, entity UUID for references, `true`/`false` for booleans). A list of list item UUIDs for `in`. Omitted for `is_empty` / `is_not_empty`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from omnismith_sdk.models.entity_rule_predicate_value import EntityRulePredicateValue

# TODO update the JSON string below
json = "{}"
# create an instance of EntityRulePredicateValue from a JSON string
entity_rule_predicate_value_instance = EntityRulePredicateValue.from_json(json)
# print the JSON string representation of the object
print(EntityRulePredicateValue.to_json())

# convert the object into a dict
entity_rule_predicate_value_dict = entity_rule_predicate_value_instance.to_dict()
# create an instance of EntityRulePredicateValue from a dict
entity_rule_predicate_value_from_dict = EntityRulePredicateValue.from_dict(entity_rule_predicate_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


