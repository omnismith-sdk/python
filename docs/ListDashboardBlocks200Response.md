# ListDashboardBlocks200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DashboardBlockResponse]**](DashboardBlockResponse.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.list_dashboard_blocks200_response import ListDashboardBlocks200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDashboardBlocks200Response from a JSON string
list_dashboard_blocks200_response_instance = ListDashboardBlocks200Response.from_json(json)
# print the JSON string representation of the object
print(ListDashboardBlocks200Response.to_json())

# convert the object into a dict
list_dashboard_blocks200_response_dict = list_dashboard_blocks200_response_instance.to_dict()
# create an instance of ListDashboardBlocks200Response from a dict
list_dashboard_blocks200_response_from_dict = ListDashboardBlocks200Response.from_dict(list_dashboard_blocks200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


