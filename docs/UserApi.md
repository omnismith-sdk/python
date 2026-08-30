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

Validates an email confirmation token sent to a newly registered user's email address and activates the account upon success. If the token is valid, returns a success confirmation message.

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
    token = 'cf_token_abc123xyz' # str | The email confirmation token received via email

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
 **token** | **str**| The email confirmation token received via email | 

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
> CreateProject201Response register_user(register_user_request)

Register a new user

Registers a new user account with email and password. For unauthenticated / public signups, a Cloudflare Turnstile `captchaToken` is required to prevent bot abuse. Sends a confirmation link to the provided email address upon creation.

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.create_project201_response import CreateProject201Response
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

[**CreateProject201Response**](CreateProject201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User registered successfully |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_confirmation_email**
> ResendConfirmationEmail200Response resend_confirmation_email(resend_confirmation_email_request)

Resend the email confirmation link

Resends the account verification email with an activation link for unconfirmed accounts. Rate-limited to prevent abuse. Silently succeeds if the email is not registered for security.

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
**422** | Validation Error |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

