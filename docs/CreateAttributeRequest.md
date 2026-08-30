# CreateAttributeRequest

Payload for creating a new schema attribute definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name of the attribute. | 
**attribute_type** | **int** | Attribute kind. 0: Dimension (standard field), 1: Metric (time-series observation), 2: List (enumerated choice option), 3: Reference (foreign entity pointer). | 
**data_type** | **int** | Storage data type. 0: String, 1: Number, 2: Boolean, 3: Datetime, 4: Date, 5: File, 6: Image, 7: Markdown. | 
**template_ids** | **List[UUID]** | Optional array of template UUIDs to immediately associate this attribute with. | [optional] 
**description** | **str** | Optional descriptive summary of the attribute and its business purpose. | [optional] 
**reference_config** | [**CreateAttributeRequestReferenceConfig**](CreateAttributeRequestReferenceConfig.md) |  | [optional] 
**id** | **UUID** | Optional explicit client-generated UUIDv7. If omitted, a UUIDv7 is automatically generated. | [optional] 
**slug** | **str** | Unique slug identifier within the project (letters, numbers, underscores). If omitted, generated automatically from name. | [optional] 

## Example

```python
from omnismith_sdk.models.create_attribute_request import CreateAttributeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAttributeRequest from a JSON string
create_attribute_request_instance = CreateAttributeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAttributeRequest.to_json())

# convert the object into a dict
create_attribute_request_dict = create_attribute_request_instance.to_dict()
# create an instance of CreateAttributeRequest from a dict
create_attribute_request_from_dict = CreateAttributeRequest.from_dict(create_attribute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


