# TestNotificationChannel422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from omnismith_sdk.models.test_notification_channel422_response import TestNotificationChannel422Response

# TODO update the JSON string below
json = "{}"
# create an instance of TestNotificationChannel422Response from a JSON string
test_notification_channel422_response_instance = TestNotificationChannel422Response.from_json(json)
# print the JSON string representation of the object
print(TestNotificationChannel422Response.to_json())

# convert the object into a dict
test_notification_channel422_response_dict = test_notification_channel422_response_instance.to_dict()
# create an instance of TestNotificationChannel422Response from a dict
test_notification_channel422_response_from_dict = TestNotificationChannel422Response.from_dict(test_notification_channel422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


