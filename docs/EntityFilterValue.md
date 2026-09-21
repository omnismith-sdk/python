# EntityFilterValue

A string for eq / neq / gt / lt / like / not-like; a non-empty list of strings for in / not-in; exactly `[lower, upper]` (inclusive) for between; omitted for empty / not-empty. List and reference attributes compare the stored id, never the label.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from omnismith_sdk.models.entity_filter_value import EntityFilterValue

# TODO update the JSON string below
json = "{}"
# create an instance of EntityFilterValue from a JSON string
entity_filter_value_instance = EntityFilterValue.from_json(json)
# print the JSON string representation of the object
print(EntityFilterValue.to_json())

# convert the object into a dict
entity_filter_value_dict = entity_filter_value_instance.to_dict()
# create an instance of EntityFilterValue from a dict
entity_filter_value_from_dict = EntityFilterValue.from_dict(entity_filter_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


