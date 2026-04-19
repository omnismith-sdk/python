# UpdateEntityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_values** | [**List[CreateEntityRequestAttributeValuesInner]**](CreateEntityRequestAttributeValuesInner.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.update_entity_request import UpdateEntityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEntityRequest from a JSON string
update_entity_request_instance = UpdateEntityRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateEntityRequest.to_json())

# convert the object into a dict
update_entity_request_dict = update_entity_request_instance.to_dict()
# create an instance of UpdateEntityRequest from a dict
update_entity_request_from_dict = UpdateEntityRequest.from_dict(update_entity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


