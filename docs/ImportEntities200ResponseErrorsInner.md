# ImportEntities200ResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row** | **int** |  | [optional] 
**column** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from omnismith_sdk.models.import_entities200_response_errors_inner import ImportEntities200ResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportEntities200ResponseErrorsInner from a JSON string
import_entities200_response_errors_inner_instance = ImportEntities200ResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(ImportEntities200ResponseErrorsInner.to_json())

# convert the object into a dict
import_entities200_response_errors_inner_dict = import_entities200_response_errors_inner_instance.to_dict()
# create an instance of ImportEntities200ResponseErrorsInner from a dict
import_entities200_response_errors_inner_from_dict = ImportEntities200ResponseErrorsInner.from_dict(import_entities200_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


