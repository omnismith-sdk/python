# AttributeResponseReferenceConfig

Configuration for Reference attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_template_id** | **UUID** |  | [optional] 
**target_attribute_id** | **UUID** |  | [optional] 

## Example

```python
from omnismith_sdk.models.attribute_response_reference_config import AttributeResponseReferenceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeResponseReferenceConfig from a JSON string
attribute_response_reference_config_instance = AttributeResponseReferenceConfig.from_json(json)
# print the JSON string representation of the object
print(AttributeResponseReferenceConfig.to_json())

# convert the object into a dict
attribute_response_reference_config_dict = attribute_response_reference_config_instance.to_dict()
# create an instance of AttributeResponseReferenceConfig from a dict
attribute_response_reference_config_from_dict = AttributeResponseReferenceConfig.from_dict(attribute_response_reference_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


