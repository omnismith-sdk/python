# AddInboundEndpointSecretRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | The secret the sender signs with, when the sender issued it (Stripe and Shopify do). Omit it to have one generated, which suits GitHub, custom senders and &#x60;shared_secret_header&#x60; (always generated). The secret is returned once, in this response, and never again. | [optional] 

## Example

```python
from omnismith_sdk.models.add_inbound_endpoint_secret_request import AddInboundEndpointSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddInboundEndpointSecretRequest from a JSON string
add_inbound_endpoint_secret_request_instance = AddInboundEndpointSecretRequest.from_json(json)
# print the JSON string representation of the object
print(AddInboundEndpointSecretRequest.to_json())

# convert the object into a dict
add_inbound_endpoint_secret_request_dict = add_inbound_endpoint_secret_request_instance.to_dict()
# create an instance of AddInboundEndpointSecretRequest from a dict
add_inbound_endpoint_secret_request_from_dict = AddInboundEndpointSecretRequest.from_dict(add_inbound_endpoint_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


