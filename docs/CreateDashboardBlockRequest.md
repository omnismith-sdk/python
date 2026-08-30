# CreateDashboardBlockRequest

Payload for adding a visualization widget to a dashboard canvas. Requires a block type (stat, chart, gauge, list), header title, and type-specific configuration including 12-column grid layout (x, y, cols, rows) and metric query parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Block visualization type: stat (single KPI counter of matching entities), chart (time-series telemetry multi-line graph aggregating metric values over time), gauge (radial threshold meter displaying metric aggregate within bounds), list (filtered and sorted entity data table). | 
**title** | **str** | Header title displayed on the dashboard widget card (e.g., \&quot;CPU Utilization — Time Series\&quot;, \&quot;Total Servers\&quot;, \&quot;Peak CPU Utilization\&quot;). | 
**config** | [**CreateDashboardBlockRequestConfig**](CreateDashboardBlockRequestConfig.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.create_dashboard_block_request import CreateDashboardBlockRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDashboardBlockRequest from a JSON string
create_dashboard_block_request_instance = CreateDashboardBlockRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDashboardBlockRequest.to_json())

# convert the object into a dict
create_dashboard_block_request_dict = create_dashboard_block_request_instance.to_dict()
# create an instance of CreateDashboardBlockRequest from a dict
create_dashboard_block_request_from_dict = CreateDashboardBlockRequest.from_dict(create_dashboard_block_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


