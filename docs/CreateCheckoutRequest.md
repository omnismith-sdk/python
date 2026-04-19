# CreateCheckoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier_id** | **UUID** | The tier ID to subscribe to (use the id value from GET /billing/tiers) | 

## Example

```python
from omnismith_sdk.models.create_checkout_request import CreateCheckoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCheckoutRequest from a JSON string
create_checkout_request_instance = CreateCheckoutRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCheckoutRequest.to_json())

# convert the object into a dict
create_checkout_request_dict = create_checkout_request_instance.to_dict()
# create an instance of CreateCheckoutRequest from a dict
create_checkout_request_from_dict = CreateCheckoutRequest.from_dict(create_checkout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


