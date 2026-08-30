# IngestMetricsRequest

Batch payload of time-series metric observations for an entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_values** | [**List[IngestMetricsRequestMetricValuesInner]**](IngestMetricsRequestMetricValuesInner.md) | List of metric attribute observations to ingest | [optional] 

## Example

```python
from omnismith_sdk.models.ingest_metrics_request import IngestMetricsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IngestMetricsRequest from a JSON string
ingest_metrics_request_instance = IngestMetricsRequest.from_json(json)
# print the JSON string representation of the object
print(IngestMetricsRequest.to_json())

# convert the object into a dict
ingest_metrics_request_dict = ingest_metrics_request_instance.to_dict()
# create an instance of IngestMetricsRequest from a dict
ingest_metrics_request_from_dict = IngestMetricsRequest.from_dict(ingest_metrics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


