# UpdateDashboardBlockRequestConfig

Updated block configuration object containing data source, metrics, time windows, and 12-column grid layout properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **UUID** | UUID of the entity template | [optional] 
**metric_attribute_id** | **UUID** | UUID of the metric attribute | [optional] 
**time_window** | **int** | Time range query window in seconds for historical telemetry (e.g. 3600, 10800, 21600, 43200, 86400, 604800, 2592000) | [optional] 
**bucket_width** | **str** | Time bucket interval for chart aggregation (e.g. \&quot;1 min\&quot;, \&quot;5 min\&quot;, \&quot;1 hour\&quot;, \&quot;1 day\&quot;) | [optional] 
**aggregate** | **str** | Aggregation function (\&quot;avg\&quot;, \&quot;sum\&quot;, \&quot;min\&quot;, \&quot;max\&quot;, \&quot;first\&quot;, \&quot;last\&quot;, \&quot;count\&quot;) | [optional] 
**entity_limit** | **int** | Maximum entity series count (1-50) | [optional] 
**min** | **float** | Minimum scale value for gauge blocks | [optional] 
**max** | **float** | Maximum scale value for gauge blocks | [optional] 
**unit** | **str** | Unit suffix for gauge blocks (e.g. \&quot;%\&quot;) | [optional] 
**start_color** | **str** | Start gradient color | [optional] 
**mid_color** | **str** | Middle gradient color | [optional] 
**end_color** | **str** | End gradient color | [optional] 
**limit** | **int** | Entity limit for list blocks | [optional] 
**sort** | **object** | Sort config object for list blocks | [optional] 
**visible_attributes** | **List[str]** | List block visible attribute IDs | [optional] 
**filters** | **List[object]** | Entity filter rules | [optional] 
**x** | **int** | Horizontal grid column (0..11 on 12-column grid) | [optional] 
**y** | **int** | Vertical grid row (0..N) | [optional] 
**cols** | **int** | Block width in columns (1..12) | [optional] 
**rows** | **int** | Block height in rows (1..N) | [optional] 

## Example

```python
from omnismith_sdk.models.update_dashboard_block_request_config import UpdateDashboardBlockRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDashboardBlockRequestConfig from a JSON string
update_dashboard_block_request_config_instance = UpdateDashboardBlockRequestConfig.from_json(json)
# print the JSON string representation of the object
print(UpdateDashboardBlockRequestConfig.to_json())

# convert the object into a dict
update_dashboard_block_request_config_dict = update_dashboard_block_request_config_instance.to_dict()
# create an instance of UpdateDashboardBlockRequestConfig from a dict
update_dashboard_block_request_config_from_dict = UpdateDashboardBlockRequestConfig.from_dict(update_dashboard_block_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


