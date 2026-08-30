# MarketplaceBlueprintDetailResponseMetadata

Blueprint metadata including keywords and install stats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **List[str]** | Categorization keywords | [optional] 
**installs** | **int** | Total number of installations across all projects | [optional] 
**version** | **int** | Schema version of the blueprint package | [optional] 

## Example

```python
from omnismith_sdk.models.marketplace_blueprint_detail_response_metadata import MarketplaceBlueprintDetailResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceBlueprintDetailResponseMetadata from a JSON string
marketplace_blueprint_detail_response_metadata_instance = MarketplaceBlueprintDetailResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(MarketplaceBlueprintDetailResponseMetadata.to_json())

# convert the object into a dict
marketplace_blueprint_detail_response_metadata_dict = marketplace_blueprint_detail_response_metadata_instance.to_dict()
# create an instance of MarketplaceBlueprintDetailResponseMetadata from a dict
marketplace_blueprint_detail_response_metadata_from_dict = MarketplaceBlueprintDetailResponseMetadata.from_dict(marketplace_blueprint_detail_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


