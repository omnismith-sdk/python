# UsageInsightsResponsePercentages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **float** |  | [optional] 
**templates** | **float** |  | [optional] 
**entities** | **float** |  | [optional] 
**projects** | **float** |  | [optional] 
**dashboards** | **float** |  | [optional] 
**automations** | **float** |  | [optional] 
**channels** | **float** |  | [optional] 
**metric_ingestions** | **float** |  | [optional] 
**dimension_updates** | **float** |  | [optional] 
**ai_credits** | **float** |  | [optional] 
**disk_space_mb** | **float** |  | [optional] 

## Example

```python
from omnismith_sdk.models.usage_insights_response_percentages import UsageInsightsResponsePercentages

# TODO update the JSON string below
json = "{}"
# create an instance of UsageInsightsResponsePercentages from a JSON string
usage_insights_response_percentages_instance = UsageInsightsResponsePercentages.from_json(json)
# print the JSON string representation of the object
print(UsageInsightsResponsePercentages.to_json())

# convert the object into a dict
usage_insights_response_percentages_dict = usage_insights_response_percentages_instance.to_dict()
# create an instance of UsageInsightsResponsePercentages from a dict
usage_insights_response_percentages_from_dict = UsageInsightsResponsePercentages.from_dict(usage_insights_response_percentages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


