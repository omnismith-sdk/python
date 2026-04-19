# TierResponseLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **int** |  | [optional] 
**templates** | **int** |  | [optional] 
**entities** | **int** |  | [optional] 
**disk_space_gb** | **int** |  | [optional] 
**projects** | **int** |  | [optional] 
**dashboards** | **int** |  | [optional] 
**automations** | **int** |  | [optional] 
**channels** | **int** |  | [optional] 
**metric_ingestions_per_month** | **int** |  | [optional] 
**dimension_updates_per_month** | **int** |  | [optional] 
**ai_credits** | **int** |  | [optional] 

## Example

```python
from omnismith_sdk.models.tier_response_limits import TierResponseLimits

# TODO update the JSON string below
json = "{}"
# create an instance of TierResponseLimits from a JSON string
tier_response_limits_instance = TierResponseLimits.from_json(json)
# print the JSON string representation of the object
print(TierResponseLimits.to_json())

# convert the object into a dict
tier_response_limits_dict = tier_response_limits_instance.to_dict()
# create an instance of TierResponseLimits from a dict
tier_response_limits_from_dict = TierResponseLimits.from_dict(tier_response_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


