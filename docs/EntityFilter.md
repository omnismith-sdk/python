# EntityFilter

One filter clause. The value shape follows the operator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Attribute slug or UUID, a standard field (&#x60;id&#x60;, &#x60;created_at&#x60;, &#x60;updated_at&#x60;), or a one-hop path through a reference attribute: &#x60;&lt;reference&gt;.&lt;attribute of its target template&gt;&#x60; (e.g. &#x60;customer.tier&#x60;). | 
**operator** | **str** | eq, neq, gt, lt, like (case-insensitive substring), not-like, empty, not-empty, in, not-in, between | 
**value** | [**EntityFilterValue**](EntityFilterValue.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.entity_filter import EntityFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EntityFilter from a JSON string
entity_filter_instance = EntityFilter.from_json(json)
# print the JSON string representation of the object
print(EntityFilter.to_json())

# convert the object into a dict
entity_filter_dict = entity_filter_instance.to_dict()
# create an instance of EntityFilter from a dict
entity_filter_from_dict = EntityFilter.from_dict(entity_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


