# UpdateDashboardBlockRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**config** | **object** | Block-specific configuration | [optional] 

## Example

```python
from omnismith_sdk.models.update_dashboard_block_request import UpdateDashboardBlockRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDashboardBlockRequest from a JSON string
update_dashboard_block_request_instance = UpdateDashboardBlockRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDashboardBlockRequest.to_json())

# convert the object into a dict
update_dashboard_block_request_dict = update_dashboard_block_request_instance.to_dict()
# create an instance of UpdateDashboardBlockRequest from a dict
update_dashboard_block_request_from_dict = UpdateDashboardBlockRequest.from_dict(update_dashboard_block_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


