# ImportEntities200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total rows processed | [optional] 
**created** | **int** | Number of entities created | [optional] 
**updated** | **int** | Number of entities updated | [optional] 
**skipped** | **int** | Number of rows skipped (no changes) | [optional] 
**failed** | **int** | Number of rows that failed | [optional] 
**errors** | [**List[ImportEntities200ResponseErrorsInner]**](ImportEntities200ResponseErrorsInner.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.import_entities200_response import ImportEntities200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ImportEntities200Response from a JSON string
import_entities200_response_instance = ImportEntities200Response.from_json(json)
# print the JSON string representation of the object
print(ImportEntities200Response.to_json())

# convert the object into a dict
import_entities200_response_dict = import_entities200_response_instance.to_dict()
# create an instance of ImportEntities200Response from a dict
import_entities200_response_from_dict = ImportEntities200Response.from_dict(import_entities200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


