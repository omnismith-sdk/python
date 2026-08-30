# ImportEntities200ResponseAffectedEntitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **UUID** |  | [optional] 
**action** | **str** |  | [optional] 
**expected_attributes** | [**List[ImportEntities200ResponseAffectedEntitiesInnerExpectedAttributesInner]**](ImportEntities200ResponseAffectedEntitiesInnerExpectedAttributesInner.md) |  | [optional] 

## Example

```python
from omnismith_sdk.models.import_entities200_response_affected_entities_inner import ImportEntities200ResponseAffectedEntitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportEntities200ResponseAffectedEntitiesInner from a JSON string
import_entities200_response_affected_entities_inner_instance = ImportEntities200ResponseAffectedEntitiesInner.from_json(json)
# print the JSON string representation of the object
print(ImportEntities200ResponseAffectedEntitiesInner.to_json())

# convert the object into a dict
import_entities200_response_affected_entities_inner_dict = import_entities200_response_affected_entities_inner_instance.to_dict()
# create an instance of ImportEntities200ResponseAffectedEntitiesInner from a dict
import_entities200_response_affected_entities_inner_from_dict = ImportEntities200ResponseAffectedEntitiesInner.from_dict(import_entities200_response_affected_entities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


