# ListTemplateEntityCounts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TemplateEntityCountResponse]**](TemplateEntityCountResponse.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.list_template_entity_counts200_response import ListTemplateEntityCounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListTemplateEntityCounts200Response from a JSON string
list_template_entity_counts200_response_instance = ListTemplateEntityCounts200Response.from_json(json)
# print the JSON string representation of the object
print(ListTemplateEntityCounts200Response.to_json())

# convert the object into a dict
list_template_entity_counts200_response_dict = list_template_entity_counts200_response_instance.to_dict()
# create an instance of ListTemplateEntityCounts200Response from a dict
list_template_entity_counts200_response_from_dict = ListTemplateEntityCounts200Response.from_dict(list_template_entity_counts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


