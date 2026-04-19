# DashboardResponse

Dashboard details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**config** | **object** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from omnismith_sdk.models.dashboard_response import DashboardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardResponse from a JSON string
dashboard_response_instance = DashboardResponse.from_json(json)
# print the JSON string representation of the object
print(DashboardResponse.to_json())

# convert the object into a dict
dashboard_response_dict = dashboard_response_instance.to_dict()
# create an instance of DashboardResponse from a dict
dashboard_response_from_dict = DashboardResponse.from_dict(dashboard_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


