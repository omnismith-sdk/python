# CreateDashboardRequestConfig

Dashboard canvas and auto-refresh configuration. Standard layout uses a 12-column grid.

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
from omnismith_sdk.models.create_dashboard_request_config import CreateDashboardRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDashboardRequestConfig from a JSON string
create_dashboard_request_config_instance = CreateDashboardRequestConfig.from_json(json)
# print the JSON string representation of the object
print(CreateDashboardRequestConfig.to_json())

# convert the object into a dict
create_dashboard_request_config_dict = create_dashboard_request_config_instance.to_dict()
# create an instance of CreateDashboardRequestConfig from a dict
create_dashboard_request_config_from_dict = CreateDashboardRequestConfig.from_dict(create_dashboard_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


