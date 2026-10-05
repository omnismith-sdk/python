# UpsertEntityByKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Identifier of the record that holds the key | 
**created** | **bool** | True when the record was created by this call, false when an existing record was updated | 

## Example

```python
from omnismith_sdk.models.upsert_entity_by_key_response import UpsertEntityByKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertEntityByKeyResponse from a JSON string
upsert_entity_by_key_response_instance = UpsertEntityByKeyResponse.from_json(json)
# print the JSON string representation of the object
print(UpsertEntityByKeyResponse.to_json())

# convert the object into a dict
upsert_entity_by_key_response_dict = upsert_entity_by_key_response_instance.to_dict()
# create an instance of UpsertEntityByKeyResponse from a dict
upsert_entity_by_key_response_from_dict = UpsertEntityByKeyResponse.from_dict(upsert_entity_by_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


