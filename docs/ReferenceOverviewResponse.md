# ReferenceOverviewResponse

Foreign entity reference target configuration for reference-type attributes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_template_id** | **UUID** | UUID of target template | 
**target_template_slug** | **str** | Slug identifier of target template | [optional] 
**target_attribute_id** | **UUID** | UUID of target display attribute | 
**target_attribute_slug** | **str** | Slug identifier of target display attribute | [optional] 

## Example

```python
from omnismith_sdk.models.reference_overview_response import ReferenceOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceOverviewResponse from a JSON string
reference_overview_response_instance = ReferenceOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(ReferenceOverviewResponse.to_json())

# convert the object into a dict
reference_overview_response_dict = reference_overview_response_instance.to_dict()
# create an instance of ReferenceOverviewResponse from a dict
reference_overview_response_from_dict = ReferenceOverviewResponse.from_dict(reference_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


