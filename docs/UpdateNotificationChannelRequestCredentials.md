# UpdateNotificationChannelRequestCredentials

Type-specific credentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bot_token** | **str** |  | [optional] 

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


