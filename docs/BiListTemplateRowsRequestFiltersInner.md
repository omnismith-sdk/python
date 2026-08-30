# BiListTemplateRowsRequestFiltersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Attribute UUID, attribute slug, or standard field (id, created_at, updated_at) | [optional] 
**operator** | **str** | Filter comparison operator: eq, neq, gt, lt, like, not-like, empty, not-empty | [optional] 
**value** | **str** | Comparison value serialized as string | [optional] 

## Example

```python
from omnismith_sdk.models.bi_list_template_rows_request_filters_inner import BiListTemplateRowsRequestFiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of BiListTemplateRowsRequestFiltersInner from a JSON string
bi_list_template_rows_request_filters_inner_instance = BiListTemplateRowsRequestFiltersInner.from_json(json)
# print the JSON string representation of the object
print(BiListTemplateRowsRequestFiltersInner.to_json())

# convert the object into a dict
bi_list_template_rows_request_filters_inner_dict = bi_list_template_rows_request_filters_inner_instance.to_dict()
# create an instance of BiListTemplateRowsRequestFiltersInner from a dict
bi_list_template_rows_request_filters_inner_from_dict = BiListTemplateRowsRequestFiltersInner.from_dict(bi_list_template_rows_request_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


