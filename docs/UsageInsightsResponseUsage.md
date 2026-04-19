# UsageInsightsResponseUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **int** |  | [optional] 
**templates** | **int** |  | [optional] 
**entities** | **int** |  | [optional] 
**projects** | **int** |  | [optional] 
**dashboards** | **int** |  | [optional] 
**automations** | **int** |  | [optional] 
**channels** | **int** |  | [optional] 
**metric_ingestions** | **int** |  | [optional] 
**dimension_updates** | **int** |  | [optional] 
**ai_credits** | **int** |  | [optional] 
**disk_space_mb** | **float** |  | [optional] 

## Example

```python
from omnismith_sdk.models.usage_insights_response_usage import UsageInsightsResponseUsage

# TODO update the JSON string below
json = "{}"
# create an instance of UsageInsightsResponseUsage from a JSON string
usage_insights_response_usage_instance = UsageInsightsResponseUsage.from_json(json)
# print the JSON string representation of the object
print(UsageInsightsResponseUsage.to_json())

# convert the object into a dict
usage_insights_response_usage_dict = usage_insights_response_usage_instance.to_dict()
# create an instance of UsageInsightsResponseUsage from a dict
usage_insights_response_usage_from_dict = UsageInsightsResponseUsage.from_dict(usage_insights_response_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


