# InboundDeliveryDetail

One row of an endpoint's delivery log with the stored body and headers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**received_at** | **datetime** |  | 
**delivery_id** | **str** | The sender&#39;s id for the delivery, when the endpoint names a delivery id source | 
**outcome** | **str** | &#x60;processed&#x60;: every record was written. &#x60;partial&#x60;: some records of a multi-record delivery failed. &#x60;skipped&#x60;: the match condition did not hold, or the delivery id was already processed. &#x60;rejected&#x60;: the request was wrong (400, 401, 413, 422). &#x60;failed&#x60;: it could not be written right now (409, 429, 5xx). | 
**http_status** | **int** | The status the sender was answered with | 
**error** | **Dict[str, object]** | The answer&#39;s error body for a non-2xx delivery, &#x60;{errors, items}&#x60; for a partial one, or &#x60;{\&quot;reason\&quot;: ...}&#x60; for a signature failure | 
**entity_ids** | **List[UUID]** | Records created or updated | 
**body_truncated** | **bool** | The stored body was cut at 256 KB | 
**duration_ms** | **int** |  | 
**replay_of** | **UUID** | The delivery this one replayed | 
**replayed_by** | **str** | Email of the user who asked for the replay | 
**body** | **str** | The raw body as received, at most 256 KB. Null for a delivery that failed signature verification. | 
**headers** | **Dict[str, str]** | The allow-listed request headers: content type, user agent and the delivery id header. Signature headers are never stored. | 

## Example

```python
from omnismith_sdk.models.inbound_delivery_detail import InboundDeliveryDetail

# TODO update the JSON string below
json = "{}"
# create an instance of InboundDeliveryDetail from a JSON string
inbound_delivery_detail_instance = InboundDeliveryDetail.from_json(json)
# print the JSON string representation of the object
print(InboundDeliveryDetail.to_json())

# convert the object into a dict
inbound_delivery_detail_dict = inbound_delivery_detail_instance.to_dict()
# create an instance of InboundDeliveryDetail from a dict
inbound_delivery_detail_from_dict = InboundDeliveryDetail.from_dict(inbound_delivery_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


