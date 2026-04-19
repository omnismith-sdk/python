# ValidationErrorResponse

RFC 7807 Validation Error Structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**title** | **str** |  | 
**status** | **int** |  | 
**errors** | **Dict[str, List[str]]** | Map of field names to array of error messages | 

## Example

```python
from omnismith_sdk.models.validation_error_response import ValidationErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorResponse from a JSON string
validation_error_response_instance = ValidationErrorResponse.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorResponse.to_json())

# convert the object into a dict
validation_error_response_dict = validation_error_response_instance.to_dict()
# create an instance of ValidationErrorResponse from a dict
validation_error_response_from_dict = ValidationErrorResponse.from_dict(validation_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


