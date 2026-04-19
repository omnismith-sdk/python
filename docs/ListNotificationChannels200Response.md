# ListNotificationChannels200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NotificationChannelResponse]**](NotificationChannelResponse.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.list_notification_channels200_response import ListNotificationChannels200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListNotificationChannels200Response from a JSON string
list_notification_channels200_response_instance = ListNotificationChannels200Response.from_json(json)
# print the JSON string representation of the object
print(ListNotificationChannels200Response.to_json())

# convert the object into a dict
list_notification_channels200_response_dict = list_notification_channels200_response_instance.to_dict()
# create an instance of ListNotificationChannels200Response from a dict
list_notification_channels200_response_from_dict = ListNotificationChannels200Response.from_dict(list_notification_channels200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


