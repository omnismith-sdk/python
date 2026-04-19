# omnismith_sdk.UserApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_user_email**](UserApi.md#confirm_user_email) | **GET** /users/confirm-email | Confirm a user&#39;s email address using a confirmation token
[**register_user**](UserApi.md#register_user) | **POST** /users/register | Register a new user
[**resend_confirmation_email**](UserApi.md#resend_confirmation_email) | **POST** /users/resend-confirmation | Resend the email confirmation link


# **confirm_user_email**
> ConfirmUserEmail200Response confirm_user_email(token)

Confirm a user's email address using a confirmation token

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.confirm_user_email200_response import ConfirmUserEmail200Response
from omnismith_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.omnismith.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = omnismith_sdk.Configuration(
    host = "https://api.omnismith.io/v1"
)


# Enter a context with an instance of the API client
with omnismith_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = omnismith_sdk.UserApi(api_client)
    token = 'token_example' # str | The email confirmation token

    try:
        # Confirm a user's email address using a confirmation token
        api_response = api_instance.confirm_user_email(token)
        print("The response of UserApi->confirm_user_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->confirm_user_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The email confirmation token | 

### Return type

[**ConfirmUserEmail200Response**](ConfirmUserEmail200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Email confirmed successfully |  -  |
**400** | Invalid confirmation token |  -  |
**410** | Confirmation token expired |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_user**
> CreateAttributeItem201Response register_user(register_user_request)

Register a new user

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.create_attribute_item201_response import CreateAttributeItem201Response
from omnismith_sdk.models.register_user_request import RegisterUserRequest
from omnismith_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.omnismith.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = omnismith_sdk.Configuration(
    host = "https://api.omnismith.io/v1"
)


# Enter a context with an instance of the API client
with omnismith_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = omnismith_sdk.UserApi(api_client)
    register_user_request = omnismith_sdk.RegisterUserRequest() # RegisterUserRequest | 

    try:
        # Register a new user
        api_response = api_instance.register_user(register_user_request)
        print("The response of UserApi->register_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->register_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_user_request** | [**RegisterUserRequest**](RegisterUserRequest.md)|  | 

### Return type

[**CreateAttributeItem201Response**](CreateAttributeItem201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User registered successfully |  -  |
**400** | Invalid input |  -  |
**422** | Validation Failed |  -  |
**409** | User already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_confirmation_email**
> ResendConfirmationEmail200Response resend_confirmation_email(resend_confirmation_email_request)

Resend the email confirmation link

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.resend_confirmation_email200_response import ResendConfirmationEmail200Response
from omnismith_sdk.models.resend_confirmation_email_request import ResendConfirmationEmailRequest
from omnismith_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.omnismith.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = omnismith_sdk.Configuration(
    host = "https://api.omnismith.io/v1"
)


# Enter a context with an instance of the API client
with omnismith_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = omnismith_sdk.UserApi(api_client)
    resend_confirmation_email_request = omnismith_sdk.ResendConfirmationEmailRequest() # ResendConfirmationEmailRequest | 

    try:
        # Resend the email confirmation link
        api_response = api_instance.resend_confirmation_email(resend_confirmation_email_request)
        print("The response of UserApi->resend_confirmation_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->resend_confirmation_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resend_confirmation_email_request** | [**ResendConfirmationEmailRequest**](ResendConfirmationEmailRequest.md)|  | 

### Return type

[**ResendConfirmationEmail200Response**](ResendConfirmationEmail200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmation email sent (or silently ignored if user not found) |  -  |
**429** | Confirmation email already sent recently |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

