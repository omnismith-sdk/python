# AttributeOverviewResponse

Schema attribute definition with semantic type, embedded list options, and reference linking.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Attribute UUID | 
**slug** | **str** | Unique slug identifier within the project | [optional] 
**name** | **str** | Human-readable attribute name | 
**type** | **str** | Semantic data kind: string, number, boolean, datetime, date, file, image, markdown, list, reference, metric | 
**description** | **str** | Attribute description | [optional] 
**options** | [**List[ListOptionOverviewResponse]**](ListOptionOverviewResponse.md) | Selectable choice options for list-type attributes (null for other types) | [optional] 
**reference** | [**ReferenceOverviewResponse**](ReferenceOverviewResponse.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.attribute_overview_response import AttributeOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeOverviewResponse from a JSON string
attribute_overview_response_instance = AttributeOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(AttributeOverviewResponse.to_json())

# convert the object into a dict
attribute_overview_response_dict = attribute_overview_response_instance.to_dict()
# create an instance of AttributeOverviewResponse from a dict
attribute_overview_response_from_dict = AttributeOverviewResponse.from_dict(attribute_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


