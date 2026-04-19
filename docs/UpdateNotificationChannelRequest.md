# UpdateNotificationChannelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**credentials** | [**UpdateNotificationChannelRequestCredentials**](UpdateNotificationChannelRequestCredentials.md) |  | [optional] 

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


