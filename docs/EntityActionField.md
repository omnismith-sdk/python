# EntityActionField

One value the operator is asked for when the action runs. Fields are shown in list order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **UUID** | Attribute UUID to ask for. Must belong to the template and must not be a metric or a preset of the same action. | 
**required** | **bool** | Whether execution refuses an empty value for this field (422 keyed by &#x60;attributes.&lt;slug&gt;&#x60;). Defaults to false. | [optional] [default to False]
**hint** | **str** | Short guidance shown next to the field | [optional] 

## Example

```python
from omnismith_sdk.models.entity_action_field import EntityActionField

# TODO update the JSON string below
json = "{}"
# create an instance of EntityActionField from a JSON string
entity_action_field_instance = EntityActionField.from_json(json)
# print the JSON string representation of the object
print(EntityActionField.to_json())

# convert the object into a dict
entity_action_field_dict = entity_action_field_instance.to_dict()
# create an instance of EntityActionField from a dict
entity_action_field_from_dict = EntityActionField.from_dict(entity_action_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


