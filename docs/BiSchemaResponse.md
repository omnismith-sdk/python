# BiSchemaResponse

Flattened metadata catalog for BI tooling

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**templates** | [**List[BiTemplateInfo]**](BiTemplateInfo.md) | List of template schemas available for BI integration | [optional] 
**fields** | [**List[BiSchemaField]**](BiSchemaField.md) | Normalized field definitions across all templates with type mappings | [optional] 

## Example

```python
from omnismith_sdk.models.bi_schema_response import BiSchemaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BiSchemaResponse from a JSON string
bi_schema_response_instance = BiSchemaResponse.from_json(json)
# print the JSON string representation of the object
print(BiSchemaResponse.to_json())

# convert the object into a dict
bi_schema_response_dict = bi_schema_response_instance.to_dict()
# create an instance of BiSchemaResponse from a dict
bi_schema_response_from_dict = BiSchemaResponse.from_dict(bi_schema_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


