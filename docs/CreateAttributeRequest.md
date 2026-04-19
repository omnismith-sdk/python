# CreateAttributeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**attribute_type** | **int** | 0: Dimension, 1: Metric, 2: List, 3: Reference | 
**data_type** | **int** | 0: String, 1: Number, 2: Boolean, 3: Datetime, 4: Date, 5: File, 6: Image | 
**template_ids** | **List[UUID]** |  | [optional] 
**description** | **str** |  | [optional] 
**reference_config** | [**CreateAttributeRequestReferenceConfig**](CreateAttributeRequestReferenceConfig.md) |  | [optional] 
**id** | **UUID** |  | [optional] 

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


