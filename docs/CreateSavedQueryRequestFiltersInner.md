# CreateSavedQueryRequestFiltersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **UUID** |  | [optional] 
**operator** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from omnismith_sdk.models.create_saved_query_request_filters_inner import CreateSavedQueryRequestFiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSavedQueryRequestFiltersInner from a JSON string
create_saved_query_request_filters_inner_instance = CreateSavedQueryRequestFiltersInner.from_json(json)
# print the JSON string representation of the object
print(CreateSavedQueryRequestFiltersInner.to_json())

# convert the object into a dict
create_saved_query_request_filters_inner_dict = create_saved_query_request_filters_inner_instance.to_dict()
# create an instance of CreateSavedQueryRequestFiltersInner from a dict
create_saved_query_request_filters_inner_from_dict = CreateSavedQueryRequestFiltersInner.from_dict(create_saved_query_request_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


