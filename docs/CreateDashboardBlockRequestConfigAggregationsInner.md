# CreateDashboardBlockRequestConfigAggregationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | [optional] 
**var_field** | **str** | Attribute slug or UUID to reduce. Required for every op except count, which must omit it. | [optional] 

## Example

```python
from omnismith_sdk.models.create_dashboard_block_request_config_aggregations_inner import CreateDashboardBlockRequestConfigAggregationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDashboardBlockRequestConfigAggregationsInner from a JSON string
create_dashboard_block_request_config_aggregations_inner_instance = CreateDashboardBlockRequestConfigAggregationsInner.from_json(json)
# print the JSON string representation of the object
print(CreateDashboardBlockRequestConfigAggregationsInner.to_json())

# convert the object into a dict
create_dashboard_block_request_config_aggregations_inner_dict = create_dashboard_block_request_config_aggregations_inner_instance.to_dict()
# create an instance of CreateDashboardBlockRequestConfigAggregationsInner from a dict
create_dashboard_block_request_config_aggregations_inner_from_dict = CreateDashboardBlockRequestConfigAggregationsInner.from_dict(create_dashboard_block_request_config_aggregations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


