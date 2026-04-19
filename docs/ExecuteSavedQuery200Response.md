# ExecuteSavedQuery200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**saved_query_id** | **UUID** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from omnismith_sdk.models.execute_saved_query200_response import ExecuteSavedQuery200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteSavedQuery200Response from a JSON string
execute_saved_query200_response_instance = ExecuteSavedQuery200Response.from_json(json)
# print the JSON string representation of the object
print(ExecuteSavedQuery200Response.to_json())

# convert the object into a dict
execute_saved_query200_response_dict = execute_saved_query200_response_instance.to_dict()
# create an instance of ExecuteSavedQuery200Response from a dict
execute_saved_query200_response_from_dict = ExecuteSavedQuery200Response.from_dict(execute_saved_query200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


