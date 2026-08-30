# CreateDashboardBlockRequestConfig

Widget configuration object containing data source, metrics, time windows, and 12-column grid layout properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **UUID** | UUID of the entity template serving as the data source (required for all block types). | [optional] 
**metric_attribute_id** | **UUID** | UUID of the metric attribute to aggregate/plot (required for chart and metric gauge blocks). | [optional] 
**time_window** | **int** | Time range query window in seconds for historical telemetry. CRITICAL for chart and time-series gauge blocks to query Entity Log data points. Presets: 3600 (1 hour), 10800 (3 hours), 21600 (6 hours), 43200 (12 hours), 86400 (24 hours / 1 day, recommended default), 604800 (7 days / 1 week), 2592000 (30 days / 1 month). | [optional] [default to 86400]
**bucket_width** | **str** | Time bucket interval for chart data aggregation. Standard values: \&quot;1 min\&quot;, \&quot;5 min\&quot;, \&quot;10 min\&quot;, \&quot;15 min\&quot;, \&quot;1 hour\&quot; (default), \&quot;6 hours\&quot;, \&quot;12 hours\&quot;, \&quot;1 day\&quot;, \&quot;1 week\&quot;, \&quot;1 month\&quot;. | [optional] [default to '1 hour']
**aggregate** | **str** | Aggregation function for telemetry metric points: \&quot;avg\&quot; (default for gauge/chart), \&quot;sum\&quot;, \&quot;min\&quot;, \&quot;max\&quot;, \&quot;first\&quot;, \&quot;last\&quot;, \&quot;count\&quot;. | [optional] [default to 'avg']
**entity_limit** | **int** | Maximum number of entity series lines to plot concurrently in chart blocks (1-50, default: 10). | [optional] [default to 10]
**min** | **float** | Minimum scale value for gauge blocks (default: 0). | [optional] [default to 0]
**max** | **float** | Maximum scale value for gauge blocks (default: 100). | [optional] [default to 100]
**unit** | **str** | Optional unit suffix for gauge blocks (e.g. \&quot;%\&quot;, \&quot;°C\&quot;, \&quot;MB/s\&quot;, \&quot;req/s\&quot;). | [optional] 
**start_color** | **str** | Start gradient hex color for gauge blocks (e.g. \&quot;#3b82f6\&quot;). | [optional] 
**mid_color** | **str** | Middle gradient hex color for gauge blocks (optional). | [optional] 
**end_color** | **str** | End gradient hex color for gauge blocks (e.g. \&quot;#06b6d4\&quot;). | [optional] 
**limit** | **int** | Maximum number of rows to return for list table blocks (default: 10). | [optional] [default to 10]
**sort** | **object** | Sort configuration object for list table blocks (e.g. {\&quot;created_at\&quot;: \&quot;desc\&quot;}). | [optional] 
**visible_attributes** | **List[str]** | Ordered list of attribute UUIDs (or \&quot;created_at\&quot;, \&quot;updated_at\&quot;) to display as columns in list table blocks. | [optional] 
**filters** | [**List[CreateDashboardBlockRequestConfigFiltersInner]**](CreateDashboardBlockRequestConfigFiltersInner.md) | Optional entity filtering conditions applied to block data. | [optional] 
**x** | **int** | Horizontal grid column position (0 to 11 on the 12-column grid canvas). | [optional] [default to 0]
**y** | **int** | Vertical grid row position (0 to N, 0-indexed). | [optional] [default to 0]
**cols** | **int** | Block width in columns on the 12-column grid canvas (1 to 12). Guidelines: 12 &#x3D; full-width (chart/list), 6 &#x3D; half-width (chart/gauge, 2 per row), 4 &#x3D; one-third width (stat/gauge, 3 per row), 3 &#x3D; one-fourth width (stat, 4 per row). Sum of cols in a row should equal 12 for edge-to-edge alignment. | [optional] 
**rows** | **int** | Block height in grid rows (1 to N). Guidelines: 2 &#x3D; KPI stat / radial gauge, 3-4 &#x3D; time-series chart, 4-5 &#x3D; list table. | [optional] 

## Example

```python
from omnismith_sdk.models.create_dashboard_block_request_config import CreateDashboardBlockRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDashboardBlockRequestConfig from a JSON string
create_dashboard_block_request_config_instance = CreateDashboardBlockRequestConfig.from_json(json)
# print the JSON string representation of the object
print(CreateDashboardBlockRequestConfig.to_json())

# convert the object into a dict
create_dashboard_block_request_config_dict = create_dashboard_block_request_config_instance.to_dict()
# create an instance of CreateDashboardBlockRequestConfig from a dict
create_dashboard_block_request_config_from_dict = CreateDashboardBlockRequestConfig.from_dict(create_dashboard_block_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


