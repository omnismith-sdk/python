# EntityActionAvailability

An enabled action of the record's template, evaluated against the record: whether it can run now, and what it asks for and sets when it does.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Action UUID | 
**slug** | **str** | The identifier to execute it with: &#x60;POST /entities/{id}/actions/{slug}&#x60; | 
**name** | **str** |  | 
**description** | **str** |  | 
**icon** | **str** | Material icon name | 
**available** | **bool** | Whether the precondition holds for the record&#39;s current values. Executing an unavailable action returns 409. | 
**unavailable_reason** | **str** | Why the action cannot run now, naming the attribute, the expectation and the current value. Null when available. | 
**fields** | [**List[EntityActionAvailableField]**](EntityActionAvailableField.md) | Values to submit, in dialog order | 
**presets** | [**List[EntityActionAvailablePreset]**](EntityActionAvailablePreset.md) | Values the action writes on its own | 

## Example

```python
from omnismith_sdk.models.entity_action_availability import EntityActionAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of EntityActionAvailability from a JSON string
entity_action_availability_instance = EntityActionAvailability.from_json(json)
# print the JSON string representation of the object
print(EntityActionAvailability.to_json())

# convert the object into a dict
entity_action_availability_dict = entity_action_availability_instance.to_dict()
# create an instance of EntityActionAvailability from a dict
entity_action_availability_from_dict = EntityActionAvailability.from_dict(entity_action_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


