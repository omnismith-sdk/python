# ValidationErrorResponseViolationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**message** | **str** |  | 
**rule** | [**ValidationErrorResponseViolationsInnerRule**](ValidationErrorResponseViolationsInnerRule.md) |  | 

## Example

```python
from omnismith_sdk.models.validation_error_response_violations_inner import ValidationErrorResponseViolationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorResponseViolationsInner from a JSON string
validation_error_response_violations_inner_instance = ValidationErrorResponseViolationsInner.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorResponseViolationsInner.to_json())

# convert the object into a dict
validation_error_response_violations_inner_dict = validation_error_response_violations_inner_instance.to_dict()
# create an instance of ValidationErrorResponseViolationsInner from a dict
validation_error_response_violations_inner_from_dict = ValidationErrorResponseViolationsInner.from_dict(validation_error_response_violations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


