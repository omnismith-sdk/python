# omnismith_sdk.AuthApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_my_permissions**](AuthApi.md#get_my_permissions) | **GET** /auth/me/permissions | Get current user role permissions
[**google_login**](AuthApi.md#google_login) | **POST** /auth/google-login | Authenticate or register with Google Sign-In
[**google_login_redirect**](AuthApi.md#google_login_redirect) | **POST** /auth/google-login-redirect | Google OAuth callback redirect handler
[**list_sessions**](AuthApi.md#list_sessions) | **GET** /auth/sessions | List active and historical user sessions
[**login**](AuthApi.md#login) | **POST** /auth/login | Authenticate user with email and password
[**refresh_token**](AuthApi.md#refresh_token) | **POST** /auth/refresh | Rotate refresh token and issue new access token
[**revoke_session**](AuthApi.md#revoke_session) | **DELETE** /auth/sessions/{id} | Revoke an active login session
[**switch_project**](AuthApi.md#switch_project) | **POST** /auth/switch-project | Switch active project context


# **get_my_permissions**
> GetMyPermissions200Response get_my_permissions()

Get current user role permissions

Returns the complete list of permission strings granted to the authenticated user under their active project role. Returns `["*"]` for project owners who possess full root administrative privileges, or an array of granular permission keys (e.g. `entity.view`, `template.create`, `billing.view_usage`) for custom assigned roles. Returns an empty array if no role is currently assigned.

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
        # Get current user role permissions
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

Authenticate or register with Google Sign-In

Authenticates a user using a Google Identity Services (GIS) ID token. Verifies the cryptographic token signature against Google public keys. If no account exists for the verified email address, a new user account is automatically provisioned and verified. Returns a JWT access token and refresh token for the active session.

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
        # Authenticate or register with Google Sign-In
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
**200** | Authentication successful with issued JWT access and refresh tokens |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_login_redirect**
> google_login_redirect(credential, g_csrf_token=g_csrf_token)

Google OAuth callback redirect handler

Handles Google Identity Services form-urlencoded POST redirection (`credential` and `g_csrf_token`). Authenticates or provisions the user account, initiates an active session, and redirects the browser (HTTP 302) to the frontend application callback URL with JWT access and refresh tokens embedded in the URL fragment.

### Example


```python
import omnismith_sdk
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
    credential = 'credential_example' # str | Google ID token credential issued by Google Identity Services
    g_csrf_token = 'g_csrf_token_example' # str | CSRF token provided by Google Identity Services (optional)

    try:
        # Google OAuth callback redirect handler
        api_instance.google_login_redirect(credential, g_csrf_token=g_csrf_token)
    except Exception as e:
        print("Exception when calling AuthApi->google_login_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential** | **str**| Google ID token credential issued by Google Identity Services | 
 **g_csrf_token** | **str**| CSRF token provided by Google Identity Services | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirects to the frontend application callback route (/auth/google-callback#...) with authentication tokens in the URL fragment |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sessions**
> ListSessions200Response list_sessions()

List active and historical user sessions

Retrieves all login sessions recorded for the authenticated user across devices and browsers. Each session record includes client metadata (IP address, User-Agent), issuance timestamp, expiration date, current status (`active`, `expired`, `revoked`), and revocation details if applicable.

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
        # List active and historical user sessions
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
**200** | List of login session records |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> GoogleLogin200Response login(login_request)

Authenticate user with email and password

Authenticates an existing user account using email and password. Upon successful validation, generates an active login session and returns a short-lived JWT access token and a refresh token for rotating credentials.

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
        # Authenticate user with email and password
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
**200** | Authentication successful with issued JWT access and refresh tokens |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> RefreshToken200Response refresh_token(refresh_token_request)

Rotate refresh token and issue new access token

Exchanges a valid refresh token for a newly issued JWT access token and a rotated refresh token. Implements strict single-use refresh token rotation: the supplied refresh token is permanently invalidated upon successful exchange. If an expired, already-rotated, or revoked token is presented, the request is rejected.

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
        # Rotate refresh token and issue new access token
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
**200** | Token refresh successful with rotated credentials |  -  |
**401** | Invalid, expired, or revoked refresh token |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_session**
> revoke_session(id)

Revoke an active login session

Immediately revokes a specific user login session by its unique session ID. All refresh tokens issued within this session are invalidated, preventing further token refreshes. If the revoked session corresponds to the current client connection, subsequent refresh attempts will fail.

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
    id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7a') # UUID | Unique UUID identifier of the session to revoke

    try:
        # Revoke an active login session
        api_instance.revoke_session(id)
    except Exception as e:
        print("Exception when calling AuthApi->revoke_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique UUID identifier of the session to revoke | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Session revoked successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **switch_project**
> SwitchProject200Response switch_project(switch_project_request)

Switch active project context

Switches the active multi-tenancy project context for the authenticated user session. Verifies that the user is an active member or owner of the target project, then issues a new JWT access token and refresh token containing updated claims for the selected project_id and the user's assigned role.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.switch_project200_response import SwitchProject200Response
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

[**SwitchProject200Response**](SwitchProject200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project switched successfully with issued project-scoped JWT access and refresh tokens |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

