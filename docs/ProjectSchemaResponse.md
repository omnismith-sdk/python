# ProjectSchemaResponse

Complete project schema graph containing all active attributes, templates, list choice items, and reference configurations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[AttributeResponse]**](AttributeResponse.md) | All active attributes in the project schema | [optional] 
**templates** | [**List[TemplateResponse]**](TemplateResponse.md) | All active templates and their attribute layout configurations | [optional] 
**list_items** | [**List[ListItemResponse]**](ListItemResponse.md) | All selectable choice items for List-type attributes | [optional] 
**reference_configs** | [**List[ReferenceConfigResponse]**](ReferenceConfigResponse.md) | All entity relationship configurations for Reference-type attributes | [optional] 

## Example

```python
from omnismith_sdk.models.project_schema_response import ProjectSchemaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSchemaResponse from a JSON string
project_schema_response_instance = ProjectSchemaResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectSchemaResponse.to_json())

# convert the object into a dict
project_schema_response_dict = project_schema_response_instance.to_dict()
# create an instance of ProjectSchemaResponse from a dict
project_schema_response_from_dict = ProjectSchemaResponse.from_dict(project_schema_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


