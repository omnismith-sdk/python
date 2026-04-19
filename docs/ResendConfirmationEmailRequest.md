# ResendConfirmationEmailRequest

Payload for resending the email confirmation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email address | 

## Example

```python
from omnismith_sdk.models.resend_confirmation_email_request import ResendConfirmationEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResendConfirmationEmailRequest from a JSON string
resend_confirmation_email_request_instance = ResendConfirmationEmailRequest.from_json(json)
# print the JSON string representation of the object
print(ResendConfirmationEmailRequest.to_json())

# convert the object into a dict
resend_confirmation_email_request_dict = resend_confirmation_email_request_instance.to_dict()
# create an instance of ResendConfirmationEmailRequest from a dict
resend_confirmation_email_request_from_dict = ResendConfirmationEmailRequest.from_dict(resend_confirmation_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


