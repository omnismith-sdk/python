# BiSchemaField

Connector-friendly field definition for BI datasets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **UUID** | Template UUID to which this field belongs | [optional] 
**template_name** | **str** | Display name of the template schema | [optional] 
**column_name** | **str** | Sanitized SQL-friendly column identifier for BI connectors | [optional] 
**label** | **str** | Human-readable column header label | [optional] 
**source** | **str** | Field origin (\&quot;system\&quot; for metadata columns, \&quot;attribute\&quot; for dynamic template attributes) | [optional] 
**attribute_id** | **UUID** | Attribute definition UUID if source is attribute | [optional] 
**attribute_name** | **str** | Display name of the attribute definition | [optional] 
**attribute_type** | **str** | Kind of dynamic attribute (dimension, metric, list, reference) | [optional] 
**data_type** | **str** | Canonical data type mapping for BI tooling (string, number, boolean, datetime, date) | [optional] 
**reference_target_template_id** | **UUID** | Target template UUID if this is a reference attribute | [optional] 
**reference_target_attribute_id** | **UUID** | Target display attribute UUID if this is a reference attribute | [optional] 
**list_options** | [**List[BiFieldOption]**](BiFieldOption.md) | Allowed selectable options if this is a list attribute | [optional] 

## Example

```python
from omnismith_sdk.models.bi_schema_field import BiSchemaField

# TODO update the JSON string below
json = "{}"
# create an instance of BiSchemaField from a JSON string
bi_schema_field_instance = BiSchemaField.from_json(json)
# print the JSON string representation of the object
print(BiSchemaField.to_json())

# convert the object into a dict
bi_schema_field_dict = bi_schema_field_instance.to_dict()
# create an instance of BiSchemaField from a dict
bi_schema_field_from_dict = BiSchemaField.from_dict(bi_schema_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


