# omnismith_sdk.AuthApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_my_permissions**](AuthApi.md#get_my_permissions) | **GET** /auth/me/permissions | Get current user&#39;s role permissions
[**google_login**](AuthApi.md#google_login) | **POST** /auth/google-login | Login or register via Google Sign-In
[**list_sessions**](AuthApi.md#list_sessions) | **GET** /auth/sessions | List recent login sessions
[**login**](AuthApi.md#login) | **POST** /auth/login | Login user
[**refresh_token**](AuthApi.md#refresh_token) | **POST** /auth/refresh | Refresh access token
[**revoke_session**](AuthApi.md#revoke_session) | **DELETE** /auth/sessions/{id} | Revoke a login session
[**switch_project**](AuthApi.md#switch_project) | **POST** /auth/switch-project | Switch active project context


# **get_my_permissions**
> GetMyPermissions200Response get_my_permissions()

Get current user's role permissions

Returns the permissions for the authenticated user's current role. Returns ["*"] for project owners (full access) or an empty array if no role is assigned.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.get_my_permissions200_response import GetMyPermissions200Response
from omnismith_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.omnismith.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = omnismith_sdk.Configuration(
    host = "https://api.omnismith.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = omnismith_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with omnismith_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = omnismith_sdk.AuthApi(api_client)

    try:
        # Get current user's role permissions
        api_response = api_instance.get_my_permissions()
        print("The response of AuthApi->get_my_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_my_permissions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMyPermissions200Response**](GetMyPermissions200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of permission strings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_login**
> GoogleLogin200Response google_login(google_login_request)

Login or register via Google Sign-In

Authenticates a user using a Google ID token. If the user does not exist, a new account is automatically created.

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.google_login200_response import GoogleLogin200Response
from omnismith_sdk.models.google_login_request import GoogleLoginRequest
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
    api_instance = omnismith_sdk.AuthApi(api_client)
    google_login_request = omnismith_sdk.GoogleLoginRequest() # GoogleLoginRequest | 

    try:
        # Login or register via Google Sign-In
        api_response = api_instance.google_login(google_login_request)
        print("The response of AuthApi->google_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->google_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_login_request** | [**GoogleLoginRequest**](GoogleLoginRequest.md)|  | 

### Return type

[**GoogleLogin200Response**](GoogleLogin200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Login successful |  -  |
**422** | Validation Error |  -  |
**401** | Invalid Google token |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sessions**
> ListSessions200Response list_sessions()

List recent login sessions

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_sessions200_response import ListSessions200Response
from omnismith_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.omnismith.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = omnismith_sdk.Configuration(
    host = "https://api.omnismith.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = omnismith_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with omnismith_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = omnismith_sdk.AuthApi(api_client)

    try:
        # List recent login sessions
        api_response = api_instance.list_sessions()
        print("The response of AuthApi->list_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->list_sessions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListSessions200Response**](ListSessions200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of sessions |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> GoogleLogin200Response login(login_request)

Login user

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.google_login200_response import GoogleLogin200Response
from omnismith_sdk.models.login_request import LoginRequest
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
    api_instance = omnismith_sdk.AuthApi(api_client)
    login_request = omnismith_sdk.LoginRequest() # LoginRequest | 

    try:
        # Login user
        api_response = api_instance.login(login_request)
        print("The response of AuthApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**GoogleLogin200Response**](GoogleLogin200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Login successful |  -  |
**422** | Validation Error |  -  |
**401** | Invalid credentials |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> RefreshToken200Response refresh_token(refresh_token_request)

Refresh access token

Exchange a valid refresh token for a new access token and refresh token. The old refresh token is invalidated (rotation).

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.refresh_token200_response import RefreshToken200Response
from omnismith_sdk.models.refresh_token_request import RefreshTokenRequest
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
    api_instance = omnismith_sdk.AuthApi(api_client)
    refresh_token_request = omnismith_sdk.RefreshTokenRequest() # RefreshTokenRequest | 

    try:
        # Refresh access token
        api_response = api_instance.refresh_token(refresh_token_request)
        print("The response of AuthApi->refresh_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->refresh_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token_request** | [**RefreshTokenRequest**](RefreshTokenRequest.md)|  | 

### Return type

[**RefreshToken200Response**](RefreshToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token refresh successful |  -  |
**401** | Invalid, expired, or revoked refresh token |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_session**
> revoke_session(id)

Revoke a login session

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.omnismith.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = omnismith_sdk.Configuration(
    host = "https://api.omnismith.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = omnismith_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with omnismith_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = omnismith_sdk.AuthApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Session ID

    try:
        # Revoke a login session
        api_instance.revoke_session(id)
    except Exception as e:
        print("Exception when calling AuthApi->revoke_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Session ID | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Session revoked |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Session not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **switch_project**
> GoogleLogin200Response switch_project(switch_project_request)

Switch active project context

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.google_login200_response import GoogleLogin200Response
from omnismith_sdk.models.switch_project_request import SwitchProjectRequest
from omnismith_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.omnismith.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = omnismith_sdk.Configuration(
    host = "https://api.omnismith.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = omnismith_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with omnismith_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = omnismith_sdk.AuthApi(api_client)
    switch_project_request = omnismith_sdk.SwitchProjectRequest() # SwitchProjectRequest | 

    try:
        # Switch active project context
        api_response = api_instance.switch_project(switch_project_request)
        print("The response of AuthApi->switch_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->switch_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **switch_project_request** | [**SwitchProjectRequest**](SwitchProjectRequest.md)|  | 

### Return type

[**GoogleLogin200Response**](GoogleLogin200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project switched successfully |  -  |
**422** | Validation Error |  -  |
**401** | Unauthorized |  -  |
**403** | Access Denied to Project |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

