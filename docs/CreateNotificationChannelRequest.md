# CreateNotificationChannelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Channel delivery type (telegram, webhook, push) | 
**name** | **str** | Display name of the notification channel | 
**credentials** | [**CreateNotificationChannelRequestCredentials**](CreateNotificationChannelRequestCredentials.md) |  | 
**rate_limit_per_minute** | **int** | Maximum messages the channel sends per clock minute, across all automations and records; sends over it fail the action (recorded in the execution history) instead of reaching the destination. Defaults to 20, Telegram&#39;s limit for one group. | [optional] [default to 20]

## Example

```python
from omnismith_sdk.models.create_notification_channel_request import CreateNotificationChannelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotificationChannelRequest from a JSON string
create_notification_channel_request_instance = CreateNotificationChannelRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNotificationChannelRequest.to_json())

# convert the object into a dict
create_notification_channel_request_dict = create_notification_channel_request_instance.to_dict()
# create an instance of CreateNotificationChannelRequest from a dict
create_notification_channel_request_from_dict = CreateNotificationChannelRequest.from_dict(create_notification_channel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


