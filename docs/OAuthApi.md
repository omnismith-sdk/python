# omnismith_sdk.OAuthApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_o_auth_authorization**](OAuthApi.md#approve_o_auth_authorization) | **POST** /oauth/authorize/approve | Approve OAuth Authorization Consent
[**exchange_o_auth_token**](OAuthApi.md#exchange_o_auth_token) | **POST** /oauth/token | Exchange OAuth 2.0 Token
[**get_jwks**](OAuthApi.md#get_jwks) | **GET** /.well-known/jwks.json | Get JSON Web Key Set
[**get_o_auth_authorize_info**](OAuthApi.md#get_o_auth_authorize_info) | **GET** /oauth/authorize/info | Get OAuth Authorization Consent Screen Info
[**get_o_auth_server_metadata**](OAuthApi.md#get_o_auth_server_metadata) | **GET** /.well-known/oauth-authorization-server | Get OAuth Authorization Server Metadata
[**register_o_auth_client**](OAuthApi.md#register_o_auth_client) | **POST** /oauth/register | Register Dynamic OAuth Client
[**revoke_o_auth_token**](OAuthApi.md#revoke_o_auth_token) | **POST** /oauth/revoke | Revoke OAuth Token


# **approve_o_auth_authorization**
> ApproveOAuthAuthorization200Response approve_o_auth_authorization(approve_o_auth_authorization_request)

Approve OAuth Authorization Consent

Approves client access to a specific Omnismith project and generates an authorization code.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.approve_o_auth_authorization200_response import ApproveOAuthAuthorization200Response
from omnismith_sdk.models.approve_o_auth_authorization_request import ApproveOAuthAuthorizationRequest
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
    api_instance = omnismith_sdk.OAuthApi(api_client)
    approve_o_auth_authorization_request = omnismith_sdk.ApproveOAuthAuthorizationRequest() # ApproveOAuthAuthorizationRequest | 

    try:
        # Approve OAuth Authorization Consent
        api_response = api_instance.approve_o_auth_authorization(approve_o_auth_authorization_request)
        print("The response of OAuthApi->approve_o_auth_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->approve_o_auth_authorization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approve_o_auth_authorization_request** | [**ApproveOAuthAuthorizationRequest**](ApproveOAuthAuthorizationRequest.md)|  | 

### Return type

[**ApproveOAuthAuthorization200Response**](ApproveOAuthAuthorization200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authorization approved and code generated |  -  |
**400** | Invalid approval parameters |  -  |
**401** | User not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_o_auth_token**
> ExchangeOAuthToken200Response exchange_o_auth_token(o_auth_token_request)

Exchange OAuth 2.0 Token

Exchanges an authorization code or refresh token for a standard RS256 JWT access token (RFC 6749 / RFC 7636).

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.exchange_o_auth_token200_response import ExchangeOAuthToken200Response
from omnismith_sdk.models.o_auth_token_request import OAuthTokenRequest
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
    api_instance = omnismith_sdk.OAuthApi(api_client)
    o_auth_token_request = omnismith_sdk.OAuthTokenRequest() # OAuthTokenRequest | 

    try:
        # Exchange OAuth 2.0 Token
        api_response = api_instance.exchange_o_auth_token(o_auth_token_request)
        print("The response of OAuthApi->exchange_o_auth_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->exchange_o_auth_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_token_request** | [**OAuthTokenRequest**](OAuthTokenRequest.md)|  | 

### Return type

[**ExchangeOAuthToken200Response**](ExchangeOAuthToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token issued successfully |  -  |
**400** | Invalid grant or request parameters |  -  |
**401** | Invalid client credentials |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jwks**
> GetJwks200Response get_jwks()

Get JSON Web Key Set

Returns the JSON Web Key Set (RFC 7517) containing the active public cryptographic keys used to verify RS256 JWT access tokens issued by the platform.

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.get_jwks200_response import GetJwks200Response
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
    api_instance = omnismith_sdk.OAuthApi(api_client)

    try:
        # Get JSON Web Key Set
        api_response = api_instance.get_jwks()
        print("The response of OAuthApi->get_jwks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->get_jwks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetJwks200Response**](GetJwks200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON Web Key Set |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth_authorize_info**
> GetOAuthAuthorizeInfo200Response get_o_auth_authorize_info(client_id, redirect_uri, response_type, scope=scope, code_challenge=code_challenge, code_challenge_method=code_challenge_method, state=state)

Get OAuth Authorization Consent Screen Info

Retrieves client metadata, requested scopes, verified user identity, and accessible projects to render the OAuth consent interface.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.get_o_auth_authorize_info200_response import GetOAuthAuthorizeInfo200Response
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
    api_instance = omnismith_sdk.OAuthApi(api_client)
    client_id = 'omni_client_0195a8f2c3e471238000000000000001' # str | Registered OAuth client identifier
    redirect_uri = 'https://claude.ai/api/mcp/oauth_callback' # str | Target redirection URI matching registered client URIs
    response_type = 'code' # str | OAuth response type (must be \"code\") (default to 'code')
    scope = 'omnismith:all' # str | Space-delimited requested scopes (optional)
    code_challenge = 'E9Melhoa2OwvFrGMTJguCH5SZXgk6uKUaz312M20O48' # str | PKCE code challenge string (RFC 7636) (optional)
    code_challenge_method = S256 # str | PKCE code challenge transformation method (optional) (default to S256)
    state = 'state_xyz123' # str | Opaque client state parameter for CSRF mitigation (optional)

    try:
        # Get OAuth Authorization Consent Screen Info
        api_response = api_instance.get_o_auth_authorize_info(client_id, redirect_uri, response_type, scope=scope, code_challenge=code_challenge, code_challenge_method=code_challenge_method, state=state)
        print("The response of OAuthApi->get_o_auth_authorize_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->get_o_auth_authorize_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| Registered OAuth client identifier | 
 **redirect_uri** | **str**| Target redirection URI matching registered client URIs | 
 **response_type** | **str**| OAuth response type (must be \&quot;code\&quot;) | [default to &#39;code&#39;]
 **scope** | **str**| Space-delimited requested scopes | [optional] 
 **code_challenge** | **str**| PKCE code challenge string (RFC 7636) | [optional] 
 **code_challenge_method** | **str**| PKCE code challenge transformation method | [optional] [default to S256]
 **state** | **str**| Opaque client state parameter for CSRF mitigation | [optional] 

### Return type

[**GetOAuthAuthorizeInfo200Response**](GetOAuthAuthorizeInfo200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authorization consent info and accessible projects |  -  |
**400** | Invalid authorization request parameters |  -  |
**401** | User not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth_server_metadata**
> GetOAuthServerMetadata200Response get_o_auth_server_metadata()

Get OAuth Authorization Server Metadata

Returns OAuth 2.0 Authorization Server Metadata (RFC 8414) defining the endpoints, supported grant types, and PKCE challenge methods for automated client configuration.

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.get_o_auth_server_metadata200_response import GetOAuthServerMetadata200Response
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
    api_instance = omnismith_sdk.OAuthApi(api_client)

    try:
        # Get OAuth Authorization Server Metadata
        api_response = api_instance.get_o_auth_server_metadata()
        print("The response of OAuthApi->get_o_auth_server_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->get_o_auth_server_metadata: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetOAuthServerMetadata200Response**](GetOAuthServerMetadata200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OAuth 2.0 Authorization Server Metadata |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_o_auth_client**
> RegisterOAuthClient201Response register_o_auth_client(register_o_auth_client_request)

Register Dynamic OAuth Client

Dynamically registers a new OAuth client per RFC 7591 (Dynamic Client Registration). Generates unique client credentials and registers authorized callback redirection URIs.

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.register_o_auth_client201_response import RegisterOAuthClient201Response
from omnismith_sdk.models.register_o_auth_client_request import RegisterOAuthClientRequest
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
    api_instance = omnismith_sdk.OAuthApi(api_client)
    register_o_auth_client_request = omnismith_sdk.RegisterOAuthClientRequest() # RegisterOAuthClientRequest | 

    try:
        # Register Dynamic OAuth Client
        api_response = api_instance.register_o_auth_client(register_o_auth_client_request)
        print("The response of OAuthApi->register_o_auth_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->register_o_auth_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_o_auth_client_request** | [**RegisterOAuthClientRequest**](RegisterOAuthClientRequest.md)|  | 

### Return type

[**RegisterOAuthClient201Response**](RegisterOAuthClient201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Client registered successfully |  -  |
**400** | Invalid client registration parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_o_auth_token**
> RevokeOAuthToken200Response revoke_o_auth_token(revoke_o_auth_token_request)

Revoke OAuth Token

Revokes an issued OAuth access token or refresh token per RFC 7009 (Token Revocation). Returns success even if the token was already revoked or expired.

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.revoke_o_auth_token200_response import RevokeOAuthToken200Response
from omnismith_sdk.models.revoke_o_auth_token_request import RevokeOAuthTokenRequest
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
    api_instance = omnismith_sdk.OAuthApi(api_client)
    revoke_o_auth_token_request = omnismith_sdk.RevokeOAuthTokenRequest() # RevokeOAuthTokenRequest | 

    try:
        # Revoke OAuth Token
        api_response = api_instance.revoke_o_auth_token(revoke_o_auth_token_request)
        print("The response of OAuthApi->revoke_o_auth_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApi->revoke_o_auth_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revoke_o_auth_token_request** | [**RevokeOAuthTokenRequest**](RevokeOAuthTokenRequest.md)|  | 

### Return type

[**RevokeOAuthToken200Response**](RevokeOAuthToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token revoked successfully (or was already invalid) |  -  |
**400** | Invalid revocation parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

