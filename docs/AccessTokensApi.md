# omnismith_sdk.AccessTokensApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_token**](AccessTokensApi.md#create_access_token) | **POST** /access-tokens | Create a programmatic API access token
[**delete_access_token**](AccessTokensApi.md#delete_access_token) | **DELETE** /access-tokens/{id} | Delete an API access token
[**list_access_tokens**](AccessTokensApi.md#list_access_tokens) | **GET** /access-tokens | List API access tokens


# **create_access_token**
> CreateAccessToken201Response create_access_token(create_access_token_request)

Create a programmatic API access token

Generates a new programmatic API access token prefixed with `omni_` (e.g. `omni_live_secret_key_...`) for the authenticated user within the active project context. The token inherits the user's current role permissions and scopes for authenticating automated API clients and scripts. The raw secret key is returned exactly once in the response and cannot be recovered later.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_access_token201_response import CreateAccessToken201Response
from omnismith_sdk.models.create_access_token_request import CreateAccessTokenRequest
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
    api_instance = omnismith_sdk.AccessTokensApi(api_client)
    create_access_token_request = omnismith_sdk.CreateAccessTokenRequest() # CreateAccessTokenRequest | 

    try:
        # Create a programmatic API access token
        api_response = api_instance.create_access_token(create_access_token_request)
        print("The response of AccessTokensApi->create_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessTokensApi->create_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_access_token_request** | [**CreateAccessTokenRequest**](CreateAccessTokenRequest.md)|  | 

### Return type

[**CreateAccessToken201Response**](CreateAccessToken201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Access token generated successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_token**
> delete_access_token(id)

Delete an API access token

Permanently revokes and removes a programmatic API access token by its unique identifier. Any future API request using the revoked secret key will immediately fail authentication with a 401 Unauthorized status.

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
    api_instance = omnismith_sdk.AccessTokensApi(api_client)
    id = UUID('0192a543-7f28-72b1-9b7e-97c997321034') # UUID | Unique UUIDv7 identifier of the access token to delete

    try:
        # Delete an API access token
        api_instance.delete_access_token(id)
    except Exception as e:
        print("Exception when calling AccessTokensApi->delete_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique UUIDv7 identifier of the access token to delete | 

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
**204** | Access token deleted successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_access_tokens**
> ListAccessTokens200Response list_access_tokens()

List API access tokens

Retrieves all active and expired programmatic API access tokens created by the authenticated user for the active project context. Returns token metadata including unique ID, user-assigned label, creation date, expiration timestamp, and last used timestamp. Note: raw secret API keys are only displayed once upon generation and are never returned in list responses.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_access_tokens200_response import ListAccessTokens200Response
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
    api_instance = omnismith_sdk.AccessTokensApi(api_client)

    try:
        # List API access tokens
        api_response = api_instance.list_access_tokens()
        print("The response of AccessTokensApi->list_access_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessTokensApi->list_access_tokens: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListAccessTokens200Response**](ListAccessTokens200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of access token metadata records |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

