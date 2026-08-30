# NotificationChannelResponse

Notification delivery channel configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique notification channel UUID | [optional] 
**type** | **str** | Channel delivery type (telegram, webhook, push) | [optional] 
**name** | **str** | User-friendly display name of the notification channel | [optional] 
**credentials** | **Dict[str, str]** | Sanitized or configured integration credentials for the channel | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from omnismith_sdk.models.notification_channel_response import NotificationChannelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannelResponse from a JSON string
notification_channel_response_instance = NotificationChannelResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationChannelResponse.to_json())

# convert the object into a dict
notification_channel_response_dict = notification_channel_response_instance.to_dict()
# create an instance of NotificationChannelResponse from a dict
notification_channel_response_from_dict = NotificationChannelResponse.from_dict(notification_channel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


