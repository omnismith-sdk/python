# RegisterPushDeviceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | FCM device registration token | 
**device_name** | **str** | Optional device name for identification | [optional] 

## Example

```python
from omnismith_sdk.models.register_push_device_request import RegisterPushDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterPushDeviceRequest from a JSON string
register_push_device_request_instance = RegisterPushDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterPushDeviceRequest.to_json())

# convert the object into a dict
register_push_device_request_dict = register_push_device_request_instance.to_dict()
# create an instance of RegisterPushDeviceRequest from a dict
register_push_device_request_from_dict = RegisterPushDeviceRequest.from_dict(register_push_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


