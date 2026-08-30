# UpdateNotificationChannelRequestCredentials

Updated type-specific credentials payload (e.g. `bot_token` for Telegram; `url`, `auth_type`, `token`, `username`, `password`, `headers` for webhook)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bot_token** | **str** | New Telegram bot token | [optional] 
**url** | **str** | Updated webhook destination URL | [optional] 
**auth_type** | **str** | Updated authorization scheme | [optional] 
**token** | **str** | Updated bearer token | [optional] 
**username** | **str** | Updated basic auth username | [optional] 
**password** | **str** | Updated basic auth password | [optional] 
**headers** | **Dict[str, str]** | Updated custom HTTP headers | [optional] 

## Example

```python
from omnismith_sdk.models.update_notification_channel_request_credentials import UpdateNotificationChannelRequestCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNotificationChannelRequestCredentials from a JSON string
update_notification_channel_request_credentials_instance = UpdateNotificationChannelRequestCredentials.from_json(json)
# print the JSON string representation of the object
print(UpdateNotificationChannelRequestCredentials.to_json())

# convert the object into a dict
update_notification_channel_request_credentials_dict = update_notification_channel_request_credentials_instance.to_dict()
# create an instance of UpdateNotificationChannelRequestCredentials from a dict
update_notification_channel_request_credentials_from_dict = UpdateNotificationChannelRequestCredentials.from_dict(update_notification_channel_request_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


