# UpdateWorkspaceViewRequest

Payload for updating workspace view / pane configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Updated display label for the view pane tab or header | [optional] 
**filters** | **List[object]** | Updated dynamic filtering rules applied to entities in this view. Attribute field can be specified by attribute UUID or attribute slug (e.g. [{\&quot;field\&quot;: \&quot;platform\&quot;, \&quot;operator\&quot;: \&quot;eq\&quot;, \&quot;value\&quot;: \&quot;&lt;list_item_id_or_slug&gt;\&quot;, \&quot;is_active\&quot;: true}]). | [optional] 
**search_string** | **str** | Updated search query string applied to entities in this view | [optional] 
**search_mode** | **str** | Updated search execution mode (keyword or semantic) | [optional] 
**sort** | [**UpdateWorkspaceViewRequestSort**](UpdateWorkspaceViewRequestSort.md) |  | [optional] 
**display_mode** | **str** | Updated presentation layout mode (table or grid) | [optional] 
**displayed_columns** | **List[str]** | Updated list of attribute UUIDs or slugs to display as columns in table mode (e.g. [\&quot;title\&quot;, \&quot;platform\&quot;, \&quot;status\&quot;, \&quot;scheduled_date\&quot;]) | [optional] 
**pane_order** | **int** | Updated display sequence index within the workspace layout | [optional] 

## Example

```python
from omnismith_sdk.models.update_workspace_view_request import UpdateWorkspaceViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkspaceViewRequest from a JSON string
update_workspace_view_request_instance = UpdateWorkspaceViewRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkspaceViewRequest.to_json())

# convert the object into a dict
update_workspace_view_request_dict = update_workspace_view_request_instance.to_dict()
# create an instance of UpdateWorkspaceViewRequest from a dict
update_workspace_view_request_from_dict = UpdateWorkspaceViewRequest.from_dict(update_workspace_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


