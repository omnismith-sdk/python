# ListPushDevices200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PushDeviceResponse]**](PushDeviceResponse.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.list_push_devices200_response import ListPushDevices200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListPushDevices200Response from a JSON string
list_push_devices200_response_instance = ListPushDevices200Response.from_json(json)
# print the JSON string representation of the object
print(ListPushDevices200Response.to_json())

# convert the object into a dict
list_push_devices200_response_dict = list_push_devices200_response_instance.to_dict()
# create an instance of ListPushDevices200Response from a dict
list_push_devices200_response_from_dict = ListPushDevices200Response.from_dict(list_push_devices200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


