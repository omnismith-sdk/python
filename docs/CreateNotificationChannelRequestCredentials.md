# CreateNotificationChannelRequestCredentials

Type-specific credentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bot_token** | **str** |  | [optional] 

## Example

```python
from omnismith_sdk.models.create_notification_channel_request_credentials import CreateNotificationChannelRequestCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotificationChannelRequestCredentials from a JSON string
create_notification_channel_request_credentials_instance = CreateNotificationChannelRequestCredentials.from_json(json)
# print the JSON string representation of the object
print(CreateNotificationChannelRequestCredentials.to_json())

# convert the object into a dict
create_notification_channel_request_credentials_dict = create_notification_channel_request_credentials_instance.to_dict()
# create an instance of CreateNotificationChannelRequestCredentials from a dict
create_notification_channel_request_credentials_from_dict = CreateNotificationChannelRequestCredentials.from_dict(create_notification_channel_request_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


