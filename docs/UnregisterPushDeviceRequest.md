# UnregisterPushDeviceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | FCM device registration token to remove | 

## Example

```python
from omnismith_sdk.models.unregister_push_device_request import UnregisterPushDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnregisterPushDeviceRequest from a JSON string
unregister_push_device_request_instance = UnregisterPushDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(UnregisterPushDeviceRequest.to_json())

# convert the object into a dict
unregister_push_device_request_dict = unregister_push_device_request_instance.to_dict()
# create an instance of UnregisterPushDeviceRequest from a dict
unregister_push_device_request_from_dict = UnregisterPushDeviceRequest.from_dict(unregister_push_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


