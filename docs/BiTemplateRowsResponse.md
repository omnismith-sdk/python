# BiTemplateRowsResponse

Flat row-based dataset for BI tooling

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[BiSchemaField]**](BiSchemaField.md) | Column schema definitions for the tabular dataset | [optional] 
**data** | **List[object]** | Array of flat row objects where keys match column_name | [optional] 
**total** | **int** | Total row count matching the query filters | [optional] 
**limit** | **int** | Limit applied to the row set | [optional] 
**offset** | **int** | Offset applied to the row set | [optional] 

## Example

```python
from omnismith_sdk.models.bi_template_rows_response import BiTemplateRowsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BiTemplateRowsResponse from a JSON string
bi_template_rows_response_instance = BiTemplateRowsResponse.from_json(json)
# print the JSON string representation of the object
print(BiTemplateRowsResponse.to_json())

# convert the object into a dict
bi_template_rows_response_dict = bi_template_rows_response_instance.to_dict()
# create an instance of BiTemplateRowsResponse from a dict
bi_template_rows_response_from_dict = BiTemplateRowsResponse.from_dict(bi_template_rows_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


