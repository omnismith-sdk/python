# PublishMarketplaceBlueprintRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Public display title of the blueprint | 
**description** | **str** | Detailed markdown description explaining what schemas, attributes, and relationships are included in the blueprint | [optional] 
**keywords** | **List[str]** | List of categorization tags and keywords for search indexing | [optional] 
**template_ids** | **List[UUID]** | Array of entity template UUIDs from the current project to snapshot into the blueprint package | 
**id** | **UUID** | Optional blueprint UUID when updating an existing published blueprint owned by the user | [optional] 

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


