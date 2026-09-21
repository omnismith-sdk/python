# TemplateOverviewResponse

Template schema definition with bound attributes, validation rules, and executable actions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Template UUID | 
**slug** | **str** | Unique template slug identifier | [optional] 
**name** | **str** | Human-readable template name | 
**description** | **str** | Template description | [optional] 
**attributes** | [**List[TemplateAttributeOverviewResponse]**](TemplateAttributeOverviewResponse.md) | Ordered list of attributes belonging to this template | 
**rules** | [**List[EntityRuleOverviewResponse]**](EntityRuleOverviewResponse.md) | Business validation rules enforced for this template | 
**actions** | [**List[EntityActionOverviewResponse]**](EntityActionOverviewResponse.md) | Executable workflow actions and transitions for records of this template | 

## Example

```python
from omnismith_sdk.models.template_overview_response import TemplateOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateOverviewResponse from a JSON string
template_overview_response_instance = TemplateOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateOverviewResponse.to_json())

# convert the object into a dict
template_overview_response_dict = template_overview_response_instance.to_dict()
# create an instance of TemplateOverviewResponse from a dict
template_overview_response_from_dict = TemplateOverviewResponse.from_dict(template_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


