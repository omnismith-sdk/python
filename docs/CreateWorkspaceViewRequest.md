# CreateWorkspaceViewRequest

Payload for adding a new view / pane to a workspace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** | Target template UUID or slug defining entity schema bound to this view pane | 
**name** | **str** | Display label for the view pane tab or header (e.g. \&quot;Telegram Channel Hub\&quot;, \&quot;All Pipeline\&quot;) | 
**filters** | **List[object]** | Dynamic filtering rules applied to entities rendered in this view pane. Attribute field can be specified by attribute UUID or attribute slug (e.g. [{\&quot;field\&quot;: \&quot;platform\&quot;, \&quot;operator\&quot;: \&quot;eq\&quot;, \&quot;value\&quot;: \&quot;&lt;list_item_id_or_slug&gt;\&quot;, \&quot;is_active\&quot;: true}]). | [optional] 
**search_string** | **str** | Initial search query string applied to entities in this view | [optional] 
**search_mode** | **str** | Search execution mode (keyword text search or semantic vector similarity search) | [optional] [default to 'keyword']
**sort** | [**CreateWorkspaceViewRequestSort**](CreateWorkspaceViewRequestSort.md) |  | [optional] 
**display_mode** | **str** | Presentation layout type for entity records (table or card grid) | [optional] [default to 'table']
**displayed_columns** | **List[str]** | List of attribute UUIDs or slugs to display as columns in table mode (e.g. [\&quot;title\&quot;, \&quot;platform\&quot;, \&quot;status\&quot;, \&quot;scheduled_date\&quot;]) | [optional] 
**pane_order** | **int** | Display sequence index of this pane within the workspace layout | [optional] 

## Example

```python
from omnismith_sdk.models.create_workspace_view_request import CreateWorkspaceViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkspaceViewRequest from a JSON string
create_workspace_view_request_instance = CreateWorkspaceViewRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWorkspaceViewRequest.to_json())

# convert the object into a dict
create_workspace_view_request_dict = create_workspace_view_request_instance.to_dict()
# create an instance of CreateWorkspaceViewRequest from a dict
create_workspace_view_request_from_dict = CreateWorkspaceViewRequest.from_dict(create_workspace_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


