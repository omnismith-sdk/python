# ListInboundDeliveries200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InboundDeliverySummary]**](InboundDeliverySummary.md) |  | 
**total** | **int** | Deliveries matching the filters | 

## Example

```python
from omnismith_sdk.models.list_inbound_deliveries200_response import ListInboundDeliveries200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListInboundDeliveries200Response from a JSON string
list_inbound_deliveries200_response_instance = ListInboundDeliveries200Response.from_json(json)
# print the JSON string representation of the object
print(ListInboundDeliveries200Response.to_json())

# convert the object into a dict
list_inbound_deliveries200_response_dict = list_inbound_deliveries200_response_instance.to_dict()
# create an instance of ListInboundDeliveries200Response from a dict
list_inbound_deliveries200_response_from_dict = ListInboundDeliveries200Response.from_dict(list_inbound_deliveries200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


