# InboundEndpointResponse

A public URL through which one outside system writes records into one template. Secret values are only ever returned when a secret is issued.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**template_id** | **UUID** |  | 
**name** | **str** |  | 
**enabled** | **bool** | A disabled endpoint answers every delivery with 404. | 
**url** | **str** | The receive URL to configure in the sender. It is not a secret: the signature authenticates each delivery. | 
**signature** | **Dict[str, object]** | How deliveries are authenticated: &#x60;preset&#x60;, plus the effective parameters for &#x60;custom_hmac&#x60; and &#x60;shared_secret_header&#x60;. | 
**mapping** | **Dict[str, object]** | How a payload becomes records, with every default filled in (&#x60;on_null&#x60;, &#x60;key.prefix&#x60;, &#x60;timestamp.format&#x60;). | 
**delivery_id_source** | [**InboundDeliveryIdSource**](InboundDeliveryIdSource.md) |  | 
**secrets** | [**List[InboundSecret]**](InboundSecret.md) | The secrets deliveries are verified with: one, or two while a rotation is under way. Only a hint of each is shown. | 
**last_signature_failure_at** | **datetime** | When a delivery last failed signature verification. A time newer than the last processed delivery usually means the sender uses the wrong secret. | 
**created_by** | **str** | Email of the user who created the endpoint | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from omnismith_sdk.models.inbound_endpoint_response import InboundEndpointResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InboundEndpointResponse from a JSON string
inbound_endpoint_response_instance = InboundEndpointResponse.from_json(json)
# print the JSON string representation of the object
print(InboundEndpointResponse.to_json())

# convert the object into a dict
inbound_endpoint_response_dict = inbound_endpoint_response_instance.to_dict()
# create an instance of InboundEndpointResponse from a dict
inbound_endpoint_response_from_dict = InboundEndpointResponse.from_dict(inbound_endpoint_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


