# InboundSecretRevealed

A secret as it is issued. `value` is shown this once and never returned again: give it to whoever configures the sender and do not store it anywhere else.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**hint** | **str** | The last four characters of the secret | 
**created_at** | **datetime** |  | 
**value** | **str** | The secret to configure in the sender | 

## Example

```python
from omnismith_sdk.models.inbound_secret_revealed import InboundSecretRevealed

# TODO update the JSON string below
json = "{}"
# create an instance of InboundSecretRevealed from a JSON string
inbound_secret_revealed_instance = InboundSecretRevealed.from_json(json)
# print the JSON string representation of the object
print(InboundSecretRevealed.to_json())

# convert the object into a dict
inbound_secret_revealed_dict = inbound_secret_revealed_instance.to_dict()
# create an instance of InboundSecretRevealed from a dict
inbound_secret_revealed_from_dict = InboundSecretRevealed.from_dict(inbound_secret_revealed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


