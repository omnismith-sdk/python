# ListTemplateViews200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WorkspaceViewResponse]**](WorkspaceViewResponse.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.list_template_views200_response import ListTemplateViews200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListTemplateViews200Response from a JSON string
list_template_views200_response_instance = ListTemplateViews200Response.from_json(json)
# print the JSON string representation of the object
print(ListTemplateViews200Response.to_json())

# convert the object into a dict
list_template_views200_response_dict = list_template_views200_response_instance.to_dict()
# create an instance of ListTemplateViews200Response from a dict
list_template_views200_response_from_dict = ListTemplateViews200Response.from_dict(list_template_views200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


