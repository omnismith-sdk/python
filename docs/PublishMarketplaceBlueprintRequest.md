# PublishMarketplaceBlueprintRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Blueprint title | 
**description** | **str** | Blueprint description | [optional] 
**keywords** | **List[str]** | Keywords for search/filtering | [optional] 
**template_ids** | **List[UUID]** | Selected template IDs to snapshot into the marketplace blueprint | 
**id** | **UUID** | Existing blueprint ID for updates | [optional] 

## Example

```python
from omnismith_sdk.models.publish_marketplace_blueprint_request import PublishMarketplaceBlueprintRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublishMarketplaceBlueprintRequest from a JSON string
publish_marketplace_blueprint_request_instance = PublishMarketplaceBlueprintRequest.from_json(json)
# print the JSON string representation of the object
print(PublishMarketplaceBlueprintRequest.to_json())

# convert the object into a dict
publish_marketplace_blueprint_request_dict = publish_marketplace_blueprint_request_instance.to_dict()
# create an instance of PublishMarketplaceBlueprintRequest from a dict
publish_marketplace_blueprint_request_from_dict = PublishMarketplaceBlueprintRequest.from_dict(publish_marketplace_blueprint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


