# UpdateNotificationChannelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Updated display name of the notification channel | [optional] 
**credentials** | [**UpdateNotificationChannelRequestCredentials**](UpdateNotificationChannelRequestCredentials.md) |  | [optional] 
**rate_limit_per_minute** | **int** | Maximum messages the channel sends per clock minute, across all automations and records; sends over it fail the action (recorded in the execution history) instead of reaching the destination. Omit to keep the current limit. | [optional] 

## Example

```python
from omnismith_sdk.models.update_notification_channel_request import UpdateNotificationChannelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNotificationChannelRequest from a JSON string
update_notification_channel_request_instance = UpdateNotificationChannelRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateNotificationChannelRequest.to_json())

# convert the object into a dict
update_notification_channel_request_dict = update_notification_channel_request_instance.to_dict()
# create an instance of UpdateNotificationChannelRequest from a dict
update_notification_channel_request_from_dict = UpdateNotificationChannelRequest.from_dict(update_notification_channel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


