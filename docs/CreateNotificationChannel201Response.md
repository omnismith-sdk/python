# CreateNotificationChannel201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Created notification channel UUID | [optional] 

## Example

```python
from omnismith_sdk.models.create_notification_channel201_response import CreateNotificationChannel201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotificationChannel201Response from a JSON string
create_notification_channel201_response_instance = CreateNotificationChannel201Response.from_json(json)
# print the JSON string representation of the object
print(CreateNotificationChannel201Response.to_json())

# convert the object into a dict
create_notification_channel201_response_dict = create_notification_channel201_response_instance.to_dict()
# create an instance of CreateNotificationChannel201Response from a dict
create_notification_channel201_response_from_dict = CreateNotificationChannel201Response.from_dict(create_notification_channel201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


