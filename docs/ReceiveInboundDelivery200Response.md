# ReceiveInboundDelivery200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**log_id** | **UUID** | The delivery log row | 
**entity_ids** | **List[UUID]** | Records created or updated | 
**reason** | **str** | Why a delivery was skipped | [optional] 
**items** | **List[Dict[str, object]]** | One result per record: &#x60;index&#x60; in the payload, &#x60;entity_id&#x60;, &#x60;created&#x60;, and the &#x60;error&#x60; body of a record that failed | [optional] 
**errors** | **Dict[str, object]** | Record errors of a partial delivery, &#x60;items[i].attributes.&lt;slug&gt;&#x60; &#x3D;&gt; messages | [optional] 

## Example

```python
from omnismith_sdk.models.receive_inbound_delivery200_response import ReceiveInboundDelivery200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiveInboundDelivery200Response from a JSON string
receive_inbound_delivery200_response_instance = ReceiveInboundDelivery200Response.from_json(json)
# print the JSON string representation of the object
print(ReceiveInboundDelivery200Response.to_json())

# convert the object into a dict
receive_inbound_delivery200_response_dict = receive_inbound_delivery200_response_instance.to_dict()
# create an instance of ReceiveInboundDelivery200Response from a dict
receive_inbound_delivery200_response_from_dict = ReceiveInboundDelivery200Response.from_dict(receive_inbound_delivery200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


