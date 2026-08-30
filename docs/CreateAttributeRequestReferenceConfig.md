# CreateAttributeRequestReferenceConfig

Required when attribute_type is 3 (Reference). Configures foreign entity relationship target template and display attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_template_id** | **UUID** | UUID of the target template whose entities can be referenced. | [optional] 
**target_attribute_id** | **UUID** | UUID of the attribute on the target template to use for entity display label resolution. | [optional] 

## Example

```python
from omnismith_sdk.models.create_attribute_request_reference_config import CreateAttributeRequestReferenceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAttributeRequestReferenceConfig from a JSON string
create_attribute_request_reference_config_instance = CreateAttributeRequestReferenceConfig.from_json(json)
# print the JSON string representation of the object
print(CreateAttributeRequestReferenceConfig.to_json())

# convert the object into a dict
create_attribute_request_reference_config_dict = create_attribute_request_reference_config_instance.to_dict()
# create an instance of CreateAttributeRequestReferenceConfig from a dict
create_attribute_request_reference_config_from_dict = CreateAttributeRequestReferenceConfig.from_dict(create_attribute_request_reference_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


