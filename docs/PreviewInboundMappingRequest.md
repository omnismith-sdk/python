# PreviewInboundMappingRequest

Send exactly one of `body` and `delivery_id`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **Dict[str, object]** | A sample payload, as the sender would post it: for example the sample event in the sender&#39;s webhook documentation. | [optional] 
**delivery_id** | **UUID** | A delivery from the endpoint&#39;s log to use as the sample instead: the &#x60;log_id&#x60; the sender was answered with. | [optional] 
**mapping** | **Dict[str, object]** | A mapping to try instead of the saved one, in the same shape as the endpoint&#39;s &#x60;mapping&#x60;. It is not saved. | [optional] 

## Example

```python
from omnismith_sdk.models.preview_inbound_mapping_request import PreviewInboundMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewInboundMappingRequest from a JSON string
preview_inbound_mapping_request_instance = PreviewInboundMappingRequest.from_json(json)
# print the JSON string representation of the object
print(PreviewInboundMappingRequest.to_json())

# convert the object into a dict
preview_inbound_mapping_request_dict = preview_inbound_mapping_request_instance.to_dict()
# create an instance of PreviewInboundMappingRequest from a dict
preview_inbound_mapping_request_from_dict = PreviewInboundMappingRequest.from_dict(preview_inbound_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


