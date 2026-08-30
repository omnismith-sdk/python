# MarketplaceBlueprintDetailResponse

Full blueprint detail representation including packaged schema definitions and demo data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique blueprint UUID | [optional] 
**user_id** | **UUID** | UUID of the publisher user | [optional] 
**title** | **str** | Blueprint display title | [optional] 
**description** | **str** | Detailed markdown description of the blueprint | [optional] 
**metadata** | [**MarketplaceBlueprintDetailResponseMetadata**](MarketplaceBlueprintDetailResponseMetadata.md) |  | [optional] 
**blueprint** | **object** | JSONB serialized blueprint payload containing templates, attributes, and optional demo entities | [optional] 
**is_featured** | **bool** | Whether the blueprint is featured in the marketplace | [optional] 
**created_at** | **datetime** | Publish timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from omnismith_sdk.models.marketplace_blueprint_detail_response import MarketplaceBlueprintDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceBlueprintDetailResponse from a JSON string
marketplace_blueprint_detail_response_instance = MarketplaceBlueprintDetailResponse.from_json(json)
# print the JSON string representation of the object
print(MarketplaceBlueprintDetailResponse.to_json())

# convert the object into a dict
marketplace_blueprint_detail_response_dict = marketplace_blueprint_detail_response_instance.to_dict()
# create an instance of MarketplaceBlueprintDetailResponse from a dict
marketplace_blueprint_detail_response_from_dict = MarketplaceBlueprintDetailResponse.from_dict(marketplace_blueprint_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


