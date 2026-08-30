# UpdateAttributeRequest

Payload for full attribute update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Updated human-readable name of the attribute. | 
**template_ids** | **List[UUID]** | Complete list of template UUIDs associated with this attribute. Replaces current template associations while preserving restricted templates. | [optional] 
**description** | **str** | Updated description of the attribute. | [optional] 
**reference_config** | [**PatchAttributeRequestReferenceConfig**](PatchAttributeRequestReferenceConfig.md) |  | [optional] 
**data_type** | **int** | Target data type for lossless transition on Dimension (0) attributes: Number(1)-&gt;String(0), Boolean(2)-&gt;String(0), Date(4)&lt;-&gt;Datetime(3), Date/Datetime-&gt;String(0), String(0)&lt;-&gt;Markdown(7). | [optional] 
**slug** | **str** | Updated unique slug identifier within the project. | [optional] 

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


