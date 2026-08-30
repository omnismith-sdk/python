# UpdateDashboardRequestConfig

Updated dashboard canvas (minCols: 12, maxCols: 12) and auto-refresh configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_cols** | **int** | Minimum number of grid columns (standard: 12) | [optional] [default to 12]
**max_cols** | **int** | Maximum number of grid columns (standard: 12) | [optional] [default to 12]
**min_rows** | **int** | Minimum number of grid rows (standard: 1) | [optional] [default to 1]
**max_rows** | **int** | Maximum number of grid rows (standard: 100) | [optional] [default to 100]
**auto_refresh** | **int** | Auto-refresh interval in seconds (0 &#x3D; off, 30, 60, 300) | [optional] [default to 0]
**thumbnail** | **str** | Base64 data URL preview thumbnail of the dashboard canvas | [optional] 

## Example

```python
from omnismith_sdk.models.update_dashboard_request_config import UpdateDashboardRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDashboardRequestConfig from a JSON string
update_dashboard_request_config_instance = UpdateDashboardRequestConfig.from_json(json)
# print the JSON string representation of the object
print(UpdateDashboardRequestConfig.to_json())

# convert the object into a dict
update_dashboard_request_config_dict = update_dashboard_request_config_instance.to_dict()
# create an instance of UpdateDashboardRequestConfig from a dict
update_dashboard_request_config_from_dict = UpdateDashboardRequestConfig.from_dict(update_dashboard_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


