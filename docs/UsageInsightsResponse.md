# UsageInsightsResponse

Detailed usage insights with limits and percentages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier_id** | **UUID** | The ID of the current tier | [optional] 
**usage** | [**UsageInsightsResponseUsage**](UsageInsightsResponseUsage.md) |  | [optional] 
**limits** | [**UsageInsightsResponseUsage**](UsageInsightsResponseUsage.md) |  | [optional] 
**percentages** | [**UsageInsightsResponsePercentages**](UsageInsightsResponsePercentages.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.usage_insights_response import UsageInsightsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsageInsightsResponse from a JSON string
usage_insights_response_instance = UsageInsightsResponse.from_json(json)
# print the JSON string representation of the object
print(UsageInsightsResponse.to_json())

# convert the object into a dict
usage_insights_response_dict = usage_insights_response_instance.to_dict()
# create an instance of UsageInsightsResponse from a dict
usage_insights_response_from_dict = UsageInsightsResponse.from_dict(usage_insights_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


