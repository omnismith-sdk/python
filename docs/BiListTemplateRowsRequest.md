# BiListTemplateRowsRequest

Filter and search criteria for querying tabular BI template rows

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_search** | **str** | Full-text query string searched across all string and text dimension attributes of the template | [optional] 
**filter_groups** | **List[List[EntityFilter]]** | Filter groups: clauses inside a group are AND-ed, groups are OR-ed. &#x60;[]&#x60; applies no filter, &#x60;[[a, b]]&#x60; is &#x60;a AND b&#x60;, &#x60;[[a], [b, c]]&#x60; is &#x60;a OR (b AND c)&#x60;. | [optional] 
**fields** | **List[str]** | Optional list of attribute slugs, UUIDs, or standard fields to project (e.g. [\&quot;price\&quot;, \&quot;sku\&quot;]). Excludes non-requested dynamic attributes from column metadata and row outputs, skipping unnecessary attribute hydration and reducing tabular payload size. | [optional] 

## Example

```python
from omnismith_sdk.models.bi_list_template_rows_request import BiListTemplateRowsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BiListTemplateRowsRequest from a JSON string
bi_list_template_rows_request_instance = BiListTemplateRowsRequest.from_json(json)
# print the JSON string representation of the object
print(BiListTemplateRowsRequest.to_json())

# convert the object into a dict
bi_list_template_rows_request_dict = bi_list_template_rows_request_instance.to_dict()
# create an instance of BiListTemplateRowsRequest from a dict
bi_list_template_rows_request_from_dict = BiListTemplateRowsRequest.from_dict(bi_list_template_rows_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


