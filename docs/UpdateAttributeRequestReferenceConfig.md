# UpdateAttributeRequestReferenceConfig

string, target_attribute_id: string}|null

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_template_id** | **UUID** |  | [optional] 
**target_attribute_id** | **UUID** |  | [optional] 

## Example

```python
from omnismith_sdk.models.update_attribute_request_reference_config import UpdateAttributeRequestReferenceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAttributeRequestReferenceConfig from a JSON string
update_attribute_request_reference_config_instance = UpdateAttributeRequestReferenceConfig.from_json(json)
# print the JSON string representation of the object
print(UpdateAttributeRequestReferenceConfig.to_json())

# convert the object into a dict
update_attribute_request_reference_config_dict = update_attribute_request_reference_config_instance.to_dict()
# create an instance of UpdateAttributeRequestReferenceConfig from a dict
update_attribute_request_reference_config_from_dict = UpdateAttributeRequestReferenceConfig.from_dict(update_attribute_request_reference_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


