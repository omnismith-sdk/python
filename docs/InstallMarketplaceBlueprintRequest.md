# InstallMarketplaceBlueprintRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **UUID** | Target project ID | 
**include_demo_data** | **bool** | Whether to install sample entities included in the blueprint | [optional] [default to False]

## Example

```python
from omnismith_sdk.models.install_marketplace_blueprint_request import InstallMarketplaceBlueprintRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstallMarketplaceBlueprintRequest from a JSON string
install_marketplace_blueprint_request_instance = InstallMarketplaceBlueprintRequest.from_json(json)
# print the JSON string representation of the object
print(InstallMarketplaceBlueprintRequest.to_json())

# convert the object into a dict
install_marketplace_blueprint_request_dict = install_marketplace_blueprint_request_instance.to_dict()
# create an instance of InstallMarketplaceBlueprintRequest from a dict
install_marketplace_blueprint_request_from_dict = InstallMarketplaceBlueprintRequest.from_dict(install_marketplace_blueprint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


