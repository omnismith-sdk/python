# TestNotificationChannelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **str** | Telegram chat ID (required for Telegram channels) | [optional] 
**message** | **str** |  | [optional] 
**title** | **str** | Notification title (used for push notifications) | [optional] 

## Example

```python
from omnismith_sdk.models.test_notification_channel_request import TestNotificationChannelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestNotificationChannelRequest from a JSON string
test_notification_channel_request_instance = TestNotificationChannelRequest.from_json(json)
# print the JSON string representation of the object
print(TestNotificationChannelRequest.to_json())

# convert the object into a dict
test_notification_channel_request_dict = test_notification_channel_request_instance.to_dict()
# create an instance of TestNotificationChannelRequest from a dict
test_notification_channel_request_from_dict = TestNotificationChannelRequest.from_dict(test_notification_channel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


