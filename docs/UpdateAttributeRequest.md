# UpdateAttributeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**template_ids** | **List[UUID]** |  | [optional] 
**reference_config** | [**UpdateAttributeRequestReferenceConfig**](UpdateAttributeRequestReferenceConfig.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.update_attribute_request import UpdateAttributeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAttributeRequest from a JSON string
update_attribute_request_instance = UpdateAttributeRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAttributeRequest.to_json())

# convert the object into a dict
update_attribute_request_dict = update_attribute_request_instance.to_dict()
# create an instance of UpdateAttributeRequest from a dict
update_attribute_request_from_dict = UpdateAttributeRequest.from_dict(update_attribute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


