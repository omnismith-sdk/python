# BiTimeSeriesRow

Flat time-series row for BI tooling

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **UUID** | Template UUID | [optional] 
**entity_id** | **UUID** | Entity UUID | [optional] 
**attribute_id** | **UUID** | Metric attribute UUID | [optional] 
**attribute_name** | **str** | Metric attribute display name | [optional] 
**bucket_time** | **datetime** | Bucket start timestamp in ISO 8601 format | [optional] 
**value** | **float** | Aggregated metric value for the time bucket | [optional] 

## Example

```python
from omnismith_sdk.models.bi_time_series_row import BiTimeSeriesRow

# TODO update the JSON string below
json = "{}"
# create an instance of BiTimeSeriesRow from a JSON string
bi_time_series_row_instance = BiTimeSeriesRow.from_json(json)
# print the JSON string representation of the object
print(BiTimeSeriesRow.to_json())

# convert the object into a dict
bi_time_series_row_dict = bi_time_series_row_instance.to_dict()
# create an instance of BiTimeSeriesRow from a dict
bi_time_series_row_from_dict = BiTimeSeriesRow.from_dict(bi_time_series_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


