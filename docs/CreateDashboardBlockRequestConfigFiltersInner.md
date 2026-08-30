# CreateDashboardBlockRequestConfigFiltersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**operator** | **str** |  | 
**value** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] [default to True]

## Example

```python
from omnismith_sdk.models.create_dashboard_block_request_config_filters_inner import CreateDashboardBlockRequestConfigFiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDashboardBlockRequestConfigFiltersInner from a JSON string
create_dashboard_block_request_config_filters_inner_instance = CreateDashboardBlockRequestConfigFiltersInner.from_json(json)
# print the JSON string representation of the object
print(CreateDashboardBlockRequestConfigFiltersInner.to_json())

# convert the object into a dict
create_dashboard_block_request_config_filters_inner_dict = create_dashboard_block_request_config_filters_inner_instance.to_dict()
# create an instance of CreateDashboardBlockRequestConfigFiltersInner from a dict
create_dashboard_block_request_config_filters_inner_from_dict = CreateDashboardBlockRequestConfigFiltersInner.from_dict(create_dashboard_block_request_config_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


