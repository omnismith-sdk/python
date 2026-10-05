# InboundEndpointOverviewResponse

A public URL through which an outside system writes records into the template. Read the full definition and the delivery log with the inbound endpoint tools.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Inbound endpoint UUID | 
**name** | **str** | Endpoint name | 
**enabled** | **bool** | Whether the endpoint accepts deliveries | 
**mode** | **str** | How records are written: &#x60;create&#x60;, &#x60;update&#x60; or &#x60;upsert&#x60; by external key | 
**preset** | **str** | The sender&#39;s signature preset | 
**url** | **str** | The receive URL configured in the sender | 

## Example

```python
from omnismith_sdk.models.inbound_endpoint_overview_response import InboundEndpointOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InboundEndpointOverviewResponse from a JSON string
inbound_endpoint_overview_response_instance = InboundEndpointOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(InboundEndpointOverviewResponse.to_json())

# convert the object into a dict
inbound_endpoint_overview_response_dict = inbound_endpoint_overview_response_instance.to_dict()
# create an instance of InboundEndpointOverviewResponse from a dict
inbound_endpoint_overview_response_from_dict = InboundEndpointOverviewResponse.from_dict(inbound_endpoint_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


