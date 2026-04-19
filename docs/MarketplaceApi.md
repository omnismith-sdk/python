# omnismith_sdk.MarketplaceApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_marketplace_blueprint**](MarketplaceApi.md#delete_marketplace_blueprint) | **DELETE** /marketplace/blueprints/{id} | Delete a marketplace blueprint
[**get_marketplace_blueprint**](MarketplaceApi.md#get_marketplace_blueprint) | **GET** /marketplace/blueprints/{id} | Get marketplace blueprint details
[**install_marketplace_blueprint**](MarketplaceApi.md#install_marketplace_blueprint) | **POST** /marketplace/blueprints/{id}/install | Install a marketplace blueprint into a project
[**list_marketplace_keywords**](MarketplaceApi.md#list_marketplace_keywords) | **GET** /marketplace/keywords | List all marketplace keywords with blueprint counts
[**publish_marketplace_blueprint**](MarketplaceApi.md#publish_marketplace_blueprint) | **POST** /marketplace/blueprints | Publish or update a marketplace blueprint
[**search_marketplace_blueprints**](MarketplaceApi.md#search_marketplace_blueprints) | **GET** /marketplace/blueprints | Search marketplace blueprints


# **delete_marketplace_blueprint**
> delete_marketplace_blueprint(id)

Delete a marketplace blueprint

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
    api_instance = omnismith_sdk.MarketplaceApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Blueprint ID

    try:
        # Delete a marketplace blueprint
        api_instance.delete_marketplace_blueprint(id)
    except Exception as e:
        print("Exception when calling MarketplaceApi->delete_marketplace_blueprint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Blueprint ID | 

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
**204** | Blueprint deleted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketplace_blueprint**
> GetMarketplaceBlueprint200Response get_marketplace_blueprint(id)

Get marketplace blueprint details

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.get_marketplace_blueprint200_response import GetMarketplaceBlueprint200Response
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
    api_instance = omnismith_sdk.MarketplaceApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Blueprint ID

    try:
        # Get marketplace blueprint details
        api_response = api_instance.get_marketplace_blueprint(id)
        print("The response of MarketplaceApi->get_marketplace_blueprint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->get_marketplace_blueprint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Blueprint ID | 

### Return type

[**GetMarketplaceBlueprint200Response**](GetMarketplaceBlueprint200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Blueprint detail |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_marketplace_blueprint**
> install_marketplace_blueprint(id, install_marketplace_blueprint_request)

Install a marketplace blueprint into a project

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.install_marketplace_blueprint_request import InstallMarketplaceBlueprintRequest
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
    api_instance = omnismith_sdk.MarketplaceApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Blueprint ID
    install_marketplace_blueprint_request = omnismith_sdk.InstallMarketplaceBlueprintRequest() # InstallMarketplaceBlueprintRequest | 

    try:
        # Install a marketplace blueprint into a project
        api_instance.install_marketplace_blueprint(id, install_marketplace_blueprint_request)
    except Exception as e:
        print("Exception when calling MarketplaceApi->install_marketplace_blueprint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Blueprint ID | 
 **install_marketplace_blueprint_request** | [**InstallMarketplaceBlueprintRequest**](InstallMarketplaceBlueprintRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Blueprint installed successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Blueprint not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_marketplace_keywords**
> ListMarketplaceKeywords200Response list_marketplace_keywords()

List all marketplace keywords with blueprint counts

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.list_marketplace_keywords200_response import ListMarketplaceKeywords200Response
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
    api_instance = omnismith_sdk.MarketplaceApi(api_client)

    try:
        # List all marketplace keywords with blueprint counts
        api_response = api_instance.list_marketplace_keywords()
        print("The response of MarketplaceApi->list_marketplace_keywords:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->list_marketplace_keywords: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListMarketplaceKeywords200Response**](ListMarketplaceKeywords200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Distinct keywords sorted by popularity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_marketplace_blueprint**
> GetMarketplaceBlueprint200Response publish_marketplace_blueprint(publish_marketplace_blueprint_request)

Publish or update a marketplace blueprint

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.get_marketplace_blueprint200_response import GetMarketplaceBlueprint200Response
from omnismith_sdk.models.publish_marketplace_blueprint_request import PublishMarketplaceBlueprintRequest
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
    api_instance = omnismith_sdk.MarketplaceApi(api_client)
    publish_marketplace_blueprint_request = omnismith_sdk.PublishMarketplaceBlueprintRequest() # PublishMarketplaceBlueprintRequest | 

    try:
        # Publish or update a marketplace blueprint
        api_response = api_instance.publish_marketplace_blueprint(publish_marketplace_blueprint_request)
        print("The response of MarketplaceApi->publish_marketplace_blueprint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->publish_marketplace_blueprint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_marketplace_blueprint_request** | [**PublishMarketplaceBlueprintRequest**](PublishMarketplaceBlueprintRequest.md)|  | 

### Return type

[**GetMarketplaceBlueprint200Response**](GetMarketplaceBlueprint200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Blueprint created |  -  |
**200** | Blueprint updated |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_marketplace_blueprints**
> SearchMarketplaceBlueprints200Response search_marketplace_blueprints(search=search, keywords=keywords, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, featured=featured)

Search marketplace blueprints

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.search_marketplace_blueprints200_response import SearchMarketplaceBlueprints200Response
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
    api_instance = omnismith_sdk.MarketplaceApi(api_client)
    search = 'search_example' # str | Free-text search on title and description (optional)
    keywords = 'keywords_example' # str | Comma-separated keywords to filter by (optional)
    limit = 20 # int | Number of results per page (optional) (default to 20)
    offset = 0 # int | Pagination offset (optional) (default to 0)
    sort_by = created_at # str | Sort field (optional) (default to created_at)
    sort_direction = desc # str | Sort direction (optional) (default to desc)
    featured = True # bool | Filter by featured status (optional)

    try:
        # Search marketplace blueprints
        api_response = api_instance.search_marketplace_blueprints(search=search, keywords=keywords, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, featured=featured)
        print("The response of MarketplaceApi->search_marketplace_blueprints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->search_marketplace_blueprints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Free-text search on title and description | [optional] 
 **keywords** | **str**| Comma-separated keywords to filter by | [optional] 
 **limit** | **int**| Number of results per page | [optional] [default to 20]
 **offset** | **int**| Pagination offset | [optional] [default to 0]
 **sort_by** | **str**| Sort field | [optional] [default to created_at]
 **sort_direction** | **str**| Sort direction | [optional] [default to desc]
 **featured** | **bool**| Filter by featured status | [optional] 

### Return type

[**SearchMarketplaceBlueprints200Response**](SearchMarketplaceBlueprints200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Marketplace blueprints list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

