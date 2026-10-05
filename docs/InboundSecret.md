# InboundSecret

A secret deliveries are verified with. Only a hint is shown.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**hint** | **str** | The last four characters of the secret | 
**created_at** | **datetime** |  | 

## Example

```python
from omnismith_sdk.models.inbound_secret import InboundSecret

# TODO update the JSON string below
json = "{}"
# create an instance of InboundSecret from a JSON string
inbound_secret_instance = InboundSecret.from_json(json)
# print the JSON string representation of the object
print(InboundSecret.to_json())

# convert the object into a dict
inbound_secret_dict = inbound_secret_instance.to_dict()
# create an instance of InboundSecret from a dict
inbound_secret_from_dict = InboundSecret.from_dict(inbound_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


