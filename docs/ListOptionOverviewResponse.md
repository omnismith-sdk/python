# ListOptionOverviewResponse

Selectable choice option for a list attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | List option UUID | 
**value** | **str** | Option display value / choice label | 

## Example

```python
from omnismith_sdk.models.list_option_overview_response import ListOptionOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOptionOverviewResponse from a JSON string
list_option_overview_response_instance = ListOptionOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(ListOptionOverviewResponse.to_json())

# convert the object into a dict
list_option_overview_response_dict = list_option_overview_response_instance.to_dict()
# create an instance of ListOptionOverviewResponse from a dict
list_option_overview_response_from_dict = ListOptionOverviewResponse.from_dict(list_option_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


