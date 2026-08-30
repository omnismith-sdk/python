# CreateTemplateRequest

Payload for creating a new dynamic schema template (content type).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[TemplateAttributeInput]**](TemplateAttributeInput.md) | Structured list of template attributes with optional per-template default values. Preferred over flat attribute_ids. | [optional] 
**groups** | [**List[TemplateGroupInput]**](TemplateGroupInput.md) | Optional ordered attribute groups for organizing template fields into visual UI sections (1 or 2 columns). | [optional] 
**name** | **str** | Human-readable name of the template. | 
**description** | **str** | Optional description of what entities conforming to this template represent. | [optional] 
**category** | **str** | Optional category tag for grouping templates in navigation. | [optional] 
**attribute_ids** | **List[UUID]** | Flat list of attribute UUIDs to associate with this template without custom default values. | [optional] 
**attribute_slugs** | **List[str]** | Flat list of attribute slugs to associate with this template by slug resolution. | [optional] 
**id** | **UUID** | Optional explicit client-generated UUIDv7. Generated automatically if omitted. | [optional] 
**slug** | **str** | Unique template slug identifier (letters, numbers, underscores). Auto-generated from name if omitted. | [optional] 

## Example

```python
from omnismith_sdk.models.create_template_request import CreateTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTemplateRequest from a JSON string
create_template_request_instance = CreateTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTemplateRequest.to_json())

# convert the object into a dict
create_template_request_dict = create_template_request_instance.to_dict()
# create an instance of CreateTemplateRequest from a dict
create_template_request_from_dict = CreateTemplateRequest.from_dict(create_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


