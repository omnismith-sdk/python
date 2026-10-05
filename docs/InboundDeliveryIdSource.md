# InboundDeliveryIdSource

Where the sender puts its own id for a delivery. A delivery whose id was already processed in the last 7 days is acknowledged with 200 and not processed again. Without a source, a retried delivery is processed again: record values stay correct, but metric points can be appended twice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | &#x60;header&#x60; or &#x60;body&#x60; | 
**path** | **str** | A header name (&#x60;X-GitHub-Delivery&#x60;) for &#x60;header&#x60;; a JSON path for &#x60;body&#x60;: &#x60;$&#x60;, &#x60;.name&#x60;, &#x60;[&#39;name&#39;]&#x60; and &#x60;[index]&#x60;, e.g. &#x60;$.id&#x60;. | 

## Example

```python
from omnismith_sdk.models.inbound_delivery_id_source import InboundDeliveryIdSource

# TODO update the JSON string below
json = "{}"
# create an instance of InboundDeliveryIdSource from a JSON string
inbound_delivery_id_source_instance = InboundDeliveryIdSource.from_json(json)
# print the JSON string representation of the object
print(InboundDeliveryIdSource.to_json())

# convert the object into a dict
inbound_delivery_id_source_dict = inbound_delivery_id_source_instance.to_dict()
# create an instance of InboundDeliveryIdSource from a dict
inbound_delivery_id_source_from_dict = InboundDeliveryIdSource.from_dict(inbound_delivery_id_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


