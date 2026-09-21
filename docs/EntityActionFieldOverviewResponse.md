# EntityActionFieldOverviewResponse

Field required or prompted from the operator when executing this action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **UUID** | Attribute UUID to set | 
**attribute_slug** | **str** | Attribute slug identifier | [optional] 
**required** | **bool** | Whether the field must be supplied | 
**hint** | **str** | Guidance text for the operator | [optional] 

## Example

```python
from omnismith_sdk.models.entity_action_field_overview_response import EntityActionFieldOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntityActionFieldOverviewResponse from a JSON string
entity_action_field_overview_response_instance = EntityActionFieldOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(EntityActionFieldOverviewResponse.to_json())

# convert the object into a dict
entity_action_field_overview_response_dict = entity_action_field_overview_response_instance.to_dict()
# create an instance of EntityActionFieldOverviewResponse from a dict
entity_action_field_overview_response_from_dict = EntityActionFieldOverviewResponse.from_dict(entity_action_field_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


