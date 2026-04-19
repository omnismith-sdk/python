# SendFeedbackRequest

Payload for submitting user feedback

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Feedback subject line | 
**category** | **str** | Feedback category | 
**message** | **str** | Detailed feedback message | 

## Example

```python
from omnismith_sdk.models.send_feedback_request import SendFeedbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendFeedbackRequest from a JSON string
send_feedback_request_instance = SendFeedbackRequest.from_json(json)
# print the JSON string representation of the object
print(SendFeedbackRequest.to_json())

# convert the object into a dict
send_feedback_request_dict = send_feedback_request_instance.to_dict()
# create an instance of SendFeedbackRequest from a dict
send_feedback_request_from_dict = SendFeedbackRequest.from_dict(send_feedback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


