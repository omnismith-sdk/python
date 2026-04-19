# DashboardBlockResponse

Dashboard block details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**dashboard_id** | **UUID** |  | [optional] 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**config** | **object** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

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


