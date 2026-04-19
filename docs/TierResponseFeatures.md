# TierResponseFeatures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_access** | **bool** |  | [optional] 
**export_to_csv** | **bool** |  | [optional] 
**sso_enabled** | **bool** |  | [optional] 
**audit_logs** | **bool** |  | [optional] 
**history_retention_days** | **int** |  | [optional] 

## Example

```python
from omnismith_sdk.models.tier_response_features import TierResponseFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of TierResponseFeatures from a JSON string
tier_response_features_instance = TierResponseFeatures.from_json(json)
# print the JSON string representation of the object
print(TierResponseFeatures.to_json())

# convert the object into a dict
tier_response_features_dict = tier_response_features_instance.to_dict()
# create an instance of TierResponseFeatures from a dict
tier_response_features_from_dict = TierResponseFeatures.from_dict(tier_response_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


