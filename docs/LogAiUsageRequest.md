# LogAiUsageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credits_deducted** | **int** | Amount of credits to deduct | 
**model** | **str** | Model used | [optional] 
**input_tokens** | **int** | Input tokens | [optional] 
**output_tokens** | **int** | Output tokens | [optional] 

## Example

```python
from omnismith_sdk.models.log_ai_usage_request import LogAiUsageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LogAiUsageRequest from a JSON string
log_ai_usage_request_instance = LogAiUsageRequest.from_json(json)
# print the JSON string representation of the object
print(LogAiUsageRequest.to_json())

# convert the object into a dict
log_ai_usage_request_dict = log_ai_usage_request_instance.to_dict()
# create an instance of LogAiUsageRequest from a dict
log_ai_usage_request_from_dict = LogAiUsageRequest.from_dict(log_ai_usage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


