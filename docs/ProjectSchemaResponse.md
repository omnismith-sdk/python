# ProjectSchemaResponse

Consolidated schema graph containing templates, attributes, choice options, references, business rules, and actions in a concise, token-efficient shape.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **UUID** | Unique identifier of the active project | [optional] 
**project_name** | **str** | Human-readable name of the active project | [optional] 
**templates** | [**List[TemplateOverviewResponse]**](TemplateOverviewResponse.md) | All active templates with bound attributes, business rules, and executable actions | 
**attributes** | [**List[AttributeOverviewResponse]**](AttributeOverviewResponse.md) | All active attributes with semantic types, list options, and foreign entity references | 

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


