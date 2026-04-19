# TierResponse

Subscription tier details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**price_cents** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**limits** | [**TierResponseLimits**](TierResponseLimits.md) |  | [optional] 
**features** | [**TierResponseFeatures**](TierResponseFeatures.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.tier_response import TierResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TierResponse from a JSON string
tier_response_instance = TierResponse.from_json(json)
# print the JSON string representation of the object
print(TierResponse.to_json())

# convert the object into a dict
tier_response_dict = tier_response_instance.to_dict()
# create an instance of TierResponse from a dict
tier_response_from_dict = TierResponse.from_dict(tier_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


