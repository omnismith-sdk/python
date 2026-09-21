# ReorderEntityActionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[UUID]** | Every action UUID of the template, first to last. Omitting or repeating one is rejected with 422. | 

## Example

```python
from omnismith_sdk.models.reorder_entity_actions_request import ReorderEntityActionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderEntityActionsRequest from a JSON string
reorder_entity_actions_request_instance = ReorderEntityActionsRequest.from_json(json)
# print the JSON string representation of the object
print(ReorderEntityActionsRequest.to_json())

# convert the object into a dict
reorder_entity_actions_request_dict = reorder_entity_actions_request_instance.to_dict()
# create an instance of ReorderEntityActionsRequest from a dict
reorder_entity_actions_request_from_dict = ReorderEntityActionsRequest.from_dict(reorder_entity_actions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


