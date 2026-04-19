# CreateDashboardBlockRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**config** | **object** | Block-specific configuration | [optional] 

## Example

```python
from omnismith_sdk.models.create_dashboard_block_request import CreateDashboardBlockRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDashboardBlockRequest from a JSON string
create_dashboard_block_request_instance = CreateDashboardBlockRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDashboardBlockRequest.to_json())

# convert the object into a dict
create_dashboard_block_request_dict = create_dashboard_block_request_instance.to_dict()
# create an instance of CreateDashboardBlockRequest from a dict
create_dashboard_block_request_from_dict = CreateDashboardBlockRequest.from_dict(create_dashboard_block_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


