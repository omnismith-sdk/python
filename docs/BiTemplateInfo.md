# BiTemplateInfo

Template metadata exposed for BI schema discovery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **UUID** | Template UUID | [optional] 
**template_name** | **str** | Human-readable template name | [optional] 
**description** | **str** | Optional template description | [optional] 
**category** | **str** | Optional template category grouping | [optional] 

## Example

```python
from omnismith_sdk.models.bi_template_info import BiTemplateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BiTemplateInfo from a JSON string
bi_template_info_instance = BiTemplateInfo.from_json(json)
# print the JSON string representation of the object
print(BiTemplateInfo.to_json())

# convert the object into a dict
bi_template_info_dict = bi_template_info_instance.to_dict()
# create an instance of BiTemplateInfo from a dict
bi_template_info_from_dict = BiTemplateInfo.from_dict(bi_template_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


