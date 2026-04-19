# ProjectSchemaResponse

Complete project schema including attributes, templates, list items, and reference configs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[AttributeResponse]**](AttributeResponse.md) |  | [optional] 
**templates** | [**List[TemplateResponse]**](TemplateResponse.md) |  | [optional] 
**list_items** | [**List[ListItemResponse]**](ListItemResponse.md) |  | [optional] 
**reference_configs** | [**List[ReferenceConfigResponse]**](ReferenceConfigResponse.md) |  | [optional] 

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


