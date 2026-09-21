# EntityActionOutcome

What happened to one record. `receipt` is set when the action executed; otherwise `error` carries the body the single-record endpoint would have returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **UUID** | OpenAPI schema for the outcome of the action on one record of a batch. | 
**status** | **str** | &#x60;executed&#x60; — written as the receipt says. &#x60;precondition_failed&#x60; — the record was not in the state the action needs (&#x60;error.reason&#x60; says why). &#x60;rule_violated&#x60; — a template rule refused the write (&#x60;error.errors&#x60; keyed by &#x60;attributes.&lt;slug&gt;&#x60;). &#x60;failed&#x60; — any other refusal: unknown record, no permission, a value failing its type. | 
**receipt** | [**ExecuteEntityActionResponse**](ExecuteEntityActionResponse.md) |  | 
**error** | [**ErrorResponse**](ErrorResponse.md) |  | 

## Example

```python
from omnismith_sdk.models.entity_action_outcome import EntityActionOutcome

# TODO update the JSON string below
json = "{}"
# create an instance of EntityActionOutcome from a JSON string
entity_action_outcome_instance = EntityActionOutcome.from_json(json)
# print the JSON string representation of the object
print(EntityActionOutcome.to_json())

# convert the object into a dict
entity_action_outcome_dict = entity_action_outcome_instance.to_dict()
# create an instance of EntityActionOutcome from a dict
entity_action_outcome_from_dict = EntityActionOutcome.from_dict(entity_action_outcome_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


