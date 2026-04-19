# ExportEntitiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_search** | **str** |  | [optional] 
**filters** | [**List[ExportEntitiesRequestFiltersInner]**](ExportEntitiesRequestFiltersInner.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.export_entities_request import ExportEntitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExportEntitiesRequest from a JSON string
export_entities_request_instance = ExportEntitiesRequest.from_json(json)
# print the JSON string representation of the object
print(ExportEntitiesRequest.to_json())

# convert the object into a dict
export_entities_request_dict = export_entities_request_instance.to_dict()
# create an instance of ExportEntitiesRequest from a dict
export_entities_request_from_dict = ExportEntitiesRequest.from_dict(export_entities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


