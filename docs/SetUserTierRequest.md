# SetUserTierRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier_id** | **UUID** |  | 
**reason** | **str** |  | [optional] 

## Example

```python
from omnismith_sdk.models.set_user_tier_request import SetUserTierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetUserTierRequest from a JSON string
set_user_tier_request_instance = SetUserTierRequest.from_json(json)
# print the JSON string representation of the object
print(SetUserTierRequest.to_json())

# convert the object into a dict
set_user_tier_request_dict = set_user_tier_request_instance.to_dict()
# create an instance of SetUserTierRequest from a dict
set_user_tier_request_from_dict = SetUserTierRequest.from_dict(set_user_tier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


