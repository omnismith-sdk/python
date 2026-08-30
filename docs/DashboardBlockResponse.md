# DashboardBlockResponse

Dashboard visualization block details including type, title, grid placement, and query configurations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Dashboard block unique identifier | [optional] 
**dashboard_id** | **UUID** | Parent dashboard unique identifier | [optional] 
**type** | **str** | Visualization widget type | [optional] 
**title** | **str** | Display title for the block widget header | [optional] 
**config** | **object** | Block layout (x, y, cols, rows) and query configuration object | [optional] 
**created_at** | **datetime** | ISO 8601 creation timestamp | [optional] 
**updated_at** | **datetime** | ISO 8601 last update timestamp | [optional] 

## Example

```python
from omnismith_sdk.models.dashboard_block_response import DashboardBlockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardBlockResponse from a JSON string
dashboard_block_response_instance = DashboardBlockResponse.from_json(json)
# print the JSON string representation of the object
print(DashboardBlockResponse.to_json())

# convert the object into a dict
dashboard_block_response_dict = dashboard_block_response_instance.to_dict()
# create an instance of DashboardBlockResponse from a dict
dashboard_block_response_from_dict = DashboardBlockResponse.from_dict(dashboard_block_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


