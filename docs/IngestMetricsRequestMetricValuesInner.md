# IngestMetricsRequestMetricValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **UUID** | Target metric attribute UUID (provide either attribute_id or attribute_slug) | [optional] 
**attribute_slug** | **str** | Target metric attribute slug (provide either attribute_id or attribute_slug) | [optional] 
**value** | **str** | Numeric observation value formatted as a string | [optional] 
**updated_at** | **datetime** | Observation timestamp in ISO 8601 or YYYY-MM-DD HH:MM:SS format. Defaults to current UTC time when omitted. | [optional] 

## Example

```python
from omnismith_sdk.models.ingest_metrics_request_metric_values_inner import IngestMetricsRequestMetricValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of IngestMetricsRequestMetricValuesInner from a JSON string
ingest_metrics_request_metric_values_inner_instance = IngestMetricsRequestMetricValuesInner.from_json(json)
# print the JSON string representation of the object
print(IngestMetricsRequestMetricValuesInner.to_json())

# convert the object into a dict
ingest_metrics_request_metric_values_inner_dict = ingest_metrics_request_metric_values_inner_instance.to_dict()
# create an instance of IngestMetricsRequestMetricValuesInner from a dict
ingest_metrics_request_metric_values_inner_from_dict = IngestMetricsRequestMetricValuesInner.from_dict(ingest_metrics_request_metric_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


