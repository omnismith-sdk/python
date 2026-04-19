# TemplateEntityCountResponse

Entity count for a template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **UUID** |  | [optional] 
**entity_count** | **int** |  | [optional] 

## Example

```python
from omnismith_sdk.models.template_entity_count_response import TemplateEntityCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateEntityCountResponse from a JSON string
template_entity_count_response_instance = TemplateEntityCountResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateEntityCountResponse.to_json())

# convert the object into a dict
template_entity_count_response_dict = template_entity_count_response_instance.to_dict()
# create an instance of TemplateEntityCountResponse from a dict
template_entity_count_response_from_dict = TemplateEntityCountResponse.from_dict(template_entity_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


