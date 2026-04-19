# UsageResponse

User resource usage statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_count** | **int** |  | [optional] 
**template_count** | **int** |  | [optional] 
**entity_count** | **int** |  | [optional] 
**project_count** | **int** |  | [optional] 
**dashboard_count** | **int** |  | [optional] 
**disk_usage_bytes** | **int** |  | [optional] 
**monthly_metric_ingestions** | **int** |  | [optional] 
**monthly_dimension_updates** | **int** |  | [optional] 
**ai_credits_used** | **int** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from omnismith_sdk.models.usage_response import UsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsageResponse from a JSON string
usage_response_instance = UsageResponse.from_json(json)
# print the JSON string representation of the object
print(UsageResponse.to_json())

# convert the object into a dict
usage_response_dict = usage_response_instance.to_dict()
# create an instance of UsageResponse from a dict
usage_response_from_dict = UsageResponse.from_dict(usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


