# BiTimeSeriesResponse

Flat time-series dataset for BI tooling

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BiTimeSeriesRow]**](BiTimeSeriesRow.md) | List of flat time-bucketed metric observations | [optional] 

## Example

```python
from omnismith_sdk.models.bi_time_series_response import BiTimeSeriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BiTimeSeriesResponse from a JSON string
bi_time_series_response_instance = BiTimeSeriesResponse.from_json(json)
# print the JSON string representation of the object
print(BiTimeSeriesResponse.to_json())

# convert the object into a dict
bi_time_series_response_dict = bi_time_series_response_instance.to_dict()
# create an instance of BiTimeSeriesResponse from a dict
bi_time_series_response_from_dict = BiTimeSeriesResponse.from_dict(bi_time_series_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


