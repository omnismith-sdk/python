# CreateEntity201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique entity identifier (UUIDv7) | [optional] 

## Example

```python
from omnismith_sdk.models.create_entity201_response import CreateEntity201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEntity201Response from a JSON string
create_entity201_response_instance = CreateEntity201Response.from_json(json)
# print the JSON string representation of the object
print(CreateEntity201Response.to_json())

# convert the object into a dict
create_entity201_response_dict = create_entity201_response_instance.to_dict()
# create an instance of CreateEntity201Response from a dict
create_entity201_response_from_dict = CreateEntity201Response.from_dict(create_entity201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


