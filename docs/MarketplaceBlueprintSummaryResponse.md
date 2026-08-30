# MarketplaceBlueprintSummaryResponse

Summary representation of a marketplace blueprint for catalog listings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique blueprint UUID | [optional] 
**user_id** | **UUID** | UUID of the publisher user | [optional] 
**title** | **str** | Blueprint display title | [optional] 
**description** | **str** | Detailed markdown description of the blueprint | [optional] 
**metadata** | [**MarketplaceBlueprintDetailResponseMetadata**](MarketplaceBlueprintDetailResponseMetadata.md) |  | [optional] 
**is_featured** | **bool** | Whether the blueprint is featured in the marketplace | [optional] 
**created_at** | **datetime** | Publish timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from omnismith_sdk.models.marketplace_blueprint_summary_response import MarketplaceBlueprintSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceBlueprintSummaryResponse from a JSON string
marketplace_blueprint_summary_response_instance = MarketplaceBlueprintSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(MarketplaceBlueprintSummaryResponse.to_json())

# convert the object into a dict
marketplace_blueprint_summary_response_dict = marketplace_blueprint_summary_response_instance.to_dict()
# create an instance of MarketplaceBlueprintSummaryResponse from a dict
marketplace_blueprint_summary_response_from_dict = MarketplaceBlueprintSummaryResponse.from_dict(marketplace_blueprint_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


