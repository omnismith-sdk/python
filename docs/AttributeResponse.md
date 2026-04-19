# AttributeResponse

Attribute details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**attribute_type** | **int** | 0: Dimension, 1: Metric, 2: List, 3: Reference | [optional] 
**data_type** | **int** | 0: String, 1: Number, 2: Boolean, 3: Datetime, 4: Date, 5: File, 6: Image | [optional] 
**template_ids** | **List[UUID]** |  | [optional] 
**reference_config** | [**AttributeResponseReferenceConfig**](AttributeResponseReferenceConfig.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 

## Example

```python
from omnismith_sdk.models.attribute_response import AttributeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeResponse from a JSON string
attribute_response_instance = AttributeResponse.from_json(json)
# print the JSON string representation of the object
print(AttributeResponse.to_json())

# convert the object into a dict
attribute_response_dict = attribute_response_instance.to_dict()
# create an instance of AttributeResponse from a dict
attribute_response_from_dict = AttributeResponse.from_dict(attribute_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


