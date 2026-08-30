# CreateEntityRequestAttributeValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **UUID** | Target attribute UUID (provide either attribute_id or attribute_slug) | [optional] 
**attribute_slug** | **str** | Target attribute slug identifier (provide either attribute_id or attribute_slug) | [optional] 
**value** | **str** | Serialized attribute value. Formats: String (\&quot;Sample\&quot;), Number (\&quot;123.45\&quot;), Boolean (\&quot;true\&quot;|\&quot;false\&quot;), Date (\&quot;YYYY-MM-DD\&quot;), Datetime (\&quot;YYYY-MM-DD HH:MM:SS\&quot;), List (ListItem UUID), Reference (target Entity UUID) | [optional] 
**updated_at** | **datetime** | Observation or creation timestamp in ISO 8601 or YYYY-MM-DD HH:MM:SS format. Defaults to current UTC time if omitted. | [optional] 

## Example

```python
from omnismith_sdk.models.create_entity_request_attribute_values_inner import CreateEntityRequestAttributeValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEntityRequestAttributeValuesInner from a JSON string
create_entity_request_attribute_values_inner_instance = CreateEntityRequestAttributeValuesInner.from_json(json)
# print the JSON string representation of the object
print(CreateEntityRequestAttributeValuesInner.to_json())

# convert the object into a dict
create_entity_request_attribute_values_inner_dict = create_entity_request_attribute_values_inner_instance.to_dict()
# create an instance of CreateEntityRequestAttributeValuesInner from a dict
create_entity_request_attribute_values_inner_from_dict = CreateEntityRequestAttributeValuesInner.from_dict(create_entity_request_attribute_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


