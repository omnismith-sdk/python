# UpdateTemplateRequest

Payload for full template update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[TemplateAttributeInput]**](TemplateAttributeInput.md) | Structured template attributes with optional per-template default values. Preferred over flat attribute_ids. | [optional] 
**groups** | [**List[TemplateGroupInput]**](TemplateGroupInput.md) | Ordered attribute groups for organizing template fields into visual UI sections. | [optional] 
**name** | **str** | Updated human-readable name of the template. | 
**description** | **str** | Updated description of the template. | [optional] 
**category** | **str** | Updated category tag for grouping in navigation. | [optional] 
**attribute_ids** | **List[UUID]** | Flat list of attribute UUIDs to associate without custom defaults. | [optional] 
**attribute_slugs** | **List[str]** | Flat list of attribute slugs to associate with this template. | [optional] 
**slug** | **str** | Updated unique slug identifier within the project. | [optional] 

## Example

```python
from omnismith_sdk.models.update_template_request import UpdateTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTemplateRequest from a JSON string
update_template_request_instance = UpdateTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTemplateRequest.to_json())

# convert the object into a dict
update_template_request_dict = update_template_request_instance.to_dict()
# create an instance of UpdateTemplateRequest from a dict
update_template_request_from_dict = UpdateTemplateRequest.from_dict(update_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


