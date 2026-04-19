# CreateEntityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | [optional] 
**attribute_values** | [**List[CreateEntityRequestAttributeValuesInner]**](CreateEntityRequestAttributeValuesInner.md) |  | [optional] 
**id** | **UUID** |  | [optional] 

## Example

```python
from omnismith_sdk.models.create_entity_request import CreateEntityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEntityRequest from a JSON string
create_entity_request_instance = CreateEntityRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEntityRequest.to_json())

# convert the object into a dict
create_entity_request_dict = create_entity_request_instance.to_dict()
# create an instance of CreateEntityRequest from a dict
create_entity_request_from_dict = CreateEntityRequest.from_dict(create_entity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


