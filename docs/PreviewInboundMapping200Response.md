# PreviewInboundMapping200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**matched** | **bool** | Whether the &#x60;match&#x60; conditions hold. When they do not, a real delivery is acknowledged and skipped. | 
**skipped** | **str** | &#x60;match&#x60; when the conditions do not hold, &#x60;no_items&#x60; when the &#x60;items&#x60; list is empty; null when records would be written. | 
**items** | [**List[PreviewInboundMapping200ResponseItemsInner]**](PreviewInboundMapping200ResponseItemsInner.md) |  | 
**errors** | **Dict[str, List[str]]** | Every record error by field, &#x60;items[i].attributes.&lt;slug&gt;&#x60; &#x3D;&gt; messages | 

## Example

```python
from omnismith_sdk.models.preview_inbound_mapping200_response import PreviewInboundMapping200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewInboundMapping200Response from a JSON string
preview_inbound_mapping200_response_instance = PreviewInboundMapping200Response.from_json(json)
# print the JSON string representation of the object
print(PreviewInboundMapping200Response.to_json())

# convert the object into a dict
preview_inbound_mapping200_response_dict = preview_inbound_mapping200_response_instance.to_dict()
# create an instance of PreviewInboundMapping200Response from a dict
preview_inbound_mapping200_response_from_dict = PreviewInboundMapping200Response.from_dict(preview_inbound_mapping200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


