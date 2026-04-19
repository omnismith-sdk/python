# UpdateDashboardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**config** | **object** |  | [optional] 

## Example

```python
from omnismith_sdk.models.update_dashboard_request import UpdateDashboardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDashboardRequest from a JSON string
update_dashboard_request_instance = UpdateDashboardRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDashboardRequest.to_json())

# convert the object into a dict
update_dashboard_request_dict = update_dashboard_request_instance.to_dict()
# create an instance of UpdateDashboardRequest from a dict
update_dashboard_request_from_dict = UpdateDashboardRequest.from_dict(update_dashboard_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


