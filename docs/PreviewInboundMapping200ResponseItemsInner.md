# PreviewInboundMapping200ResponseItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Position in the payload&#39;s &#x60;items&#x60; list; 0 without one | 
**external_key** | **str** |  | 
**action** | **str** | What a delivery would do with this record; null when the record fails before that is known | 
**entity_id** | **UUID** | The record an update would change | 
**attributes** | **Dict[str, object]** | Values keyed as in the mapping: a string, null to clear, or &#x60;{value, updated_at}&#x60; for a timed value | 
**error** | **Dict[str, object]** | The error body a real delivery would meet for this record | 

## Example

```python
from omnismith_sdk.models.preview_inbound_mapping200_response_items_inner import PreviewInboundMapping200ResponseItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewInboundMapping200ResponseItemsInner from a JSON string
preview_inbound_mapping200_response_items_inner_instance = PreviewInboundMapping200ResponseItemsInner.from_json(json)
# print the JSON string representation of the object
print(PreviewInboundMapping200ResponseItemsInner.to_json())

# convert the object into a dict
preview_inbound_mapping200_response_items_inner_dict = preview_inbound_mapping200_response_items_inner_instance.to_dict()
# create an instance of PreviewInboundMapping200ResponseItemsInner from a dict
preview_inbound_mapping200_response_items_inner_from_dict = PreviewInboundMapping200ResponseItemsInner.from_dict(preview_inbound_mapping200_response_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


