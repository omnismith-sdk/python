# ReferenceConfigResponse

Reference configuration for a Reference-type attribute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_id** | **UUID** |  | [optional] 
**target_template_id** | **UUID** |  | [optional] 
**target_attribute_id** | **UUID** |  | [optional] 

## Example

```python
from omnismith_sdk.models.reference_config_response import ReferenceConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceConfigResponse from a JSON string
reference_config_response_instance = ReferenceConfigResponse.from_json(json)
# print the JSON string representation of the object
print(ReferenceConfigResponse.to_json())

# convert the object into a dict
reference_config_response_dict = reference_config_response_instance.to_dict()
# create an instance of ReferenceConfigResponse from a dict
reference_config_response_from_dict = ReferenceConfigResponse.from_dict(reference_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


