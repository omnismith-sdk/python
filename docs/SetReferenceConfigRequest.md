# SetReferenceConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_template_id** | **UUID** | Target template UUID | 
**target_attribute_id** | **UUID** | Target attribute UUID (display attribute) | 

## Example

```python
from omnismith_sdk.models.set_reference_config_request import SetReferenceConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetReferenceConfigRequest from a JSON string
set_reference_config_request_instance = SetReferenceConfigRequest.from_json(json)
# print the JSON string representation of the object
print(SetReferenceConfigRequest.to_json())

# convert the object into a dict
set_reference_config_request_dict = set_reference_config_request_instance.to_dict()
# create an instance of SetReferenceConfigRequest from a dict
set_reference_config_request_from_dict = SetReferenceConfigRequest.from_dict(set_reference_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


