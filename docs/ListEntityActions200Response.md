# ListEntityActions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EntityActionAvailability]**](EntityActionAvailability.md) |  | 

## Example

```python
from omnismith_sdk.models.list_entity_actions200_response import ListEntityActions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListEntityActions200Response from a JSON string
list_entity_actions200_response_instance = ListEntityActions200Response.from_json(json)
# print the JSON string representation of the object
print(ListEntityActions200Response.to_json())

# convert the object into a dict
list_entity_actions200_response_dict = list_entity_actions200_response_instance.to_dict()
# create an instance of ListEntityActions200Response from a dict
list_entity_actions200_response_from_dict = ListEntityActions200Response.from_dict(list_entity_actions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


