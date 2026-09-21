# UiLayoutResponse

Consolidated visual form layout configurations, icons, and display rankings for the active project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **UUID** | Unique identifier of the active project | [optional] 
**project_name** | **str** | Human-readable name of the active project | [optional] 
**templates** | [**List[TemplateLayoutResponse]**](TemplateLayoutResponse.md) | Visual form section groups and categories per template | 
**actions** | [**List[ActionLayoutResponse]**](ActionLayoutResponse.md) | Display icons and sort orders for template actions | 
**list_items** | [**List[ListItemLayoutResponse]**](ListItemLayoutResponse.md) | Display sort orders for list choice items | 

## Example

```python
from omnismith_sdk.models.ui_layout_response import UiLayoutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UiLayoutResponse from a JSON string
ui_layout_response_instance = UiLayoutResponse.from_json(json)
# print the JSON string representation of the object
print(UiLayoutResponse.to_json())

# convert the object into a dict
ui_layout_response_dict = ui_layout_response_instance.to_dict()
# create an instance of UiLayoutResponse from a dict
ui_layout_response_from_dict = UiLayoutResponse.from_dict(ui_layout_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


