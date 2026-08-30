# omnismith_sdk.MarketplaceApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_marketplace_blueprint**](MarketplaceApi.md#delete_marketplace_blueprint) | **DELETE** /marketplace/blueprints/{id} | Delete a marketplace blueprint
[**get_marketplace_blueprint**](MarketplaceApi.md#get_marketplace_blueprint) | **GET** /marketplace/blueprints/{id} | Get marketplace blueprint details
[**install_marketplace_blueprint**](MarketplaceApi.md#install_marketplace_blueprint) | **POST** /marketplace/blueprints/{id}/install | Install a marketplace blueprint into a project
[**list_marketplace_keywords**](MarketplaceApi.md#list_marketplace_keywords) | **GET** /marketplace/keywords | List marketplace keywords
[**publish_marketplace_blueprint**](MarketplaceApi.md#publish_marketplace_blueprint) | **POST** /marketplace/blueprints | Publish or update a marketplace blueprint
[**search_marketplace_blueprints**](MarketplaceApi.md#search_marketplace_blueprints) | **GET** /marketplace/blueprints | Search marketplace blueprints


# **delete_marketplace_blueprint**
> delete_marketplace_blueprint(id)

Delete a marketplace blueprint

Permanently removes a published blueprint from the marketplace catalog. Only the author who published the blueprint or a system administrator has permission to delete it.

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
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60003') # UUID | Unique blueprint UUID to delete

    try:
        # Delete a marketplace blueprint
        api_instance.delete_marketplace_blueprint(id)
    except Exception as e:
        print("Exception when calling MarketplaceApi->delete_marketplace_blueprint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique blueprint UUID to delete | 

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
**204** | Blueprint successfully deleted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - Not the owner of the blueprint |  -  |
**404** | Blueprint not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketplace_blueprint**
> GetMarketplaceBlueprint200Response get_marketplace_blueprint(id)

Get marketplace blueprint details

Retrieves complete information for a specific marketplace blueprint by its UUID. Returns full blueprint metadata, publisher details, popularity metrics, and packaged blueprint schema definition containing template schemas, attribute configurations, and optional demo entities.

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
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60003') # UUID | Unique marketplace blueprint UUID

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
 **id** | **UUID**| Unique marketplace blueprint UUID | 

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
**200** | Marketplace blueprint details |  -  |
**404** | Blueprint not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_marketplace_blueprint**
> install_marketplace_blueprint(id, install_marketplace_blueprint_request)

Install a marketplace blueprint into a project

Installs a marketplace blueprint into the specified project context. Provisions all packaged templates, attributes, and relationships defined in the blueprint schema, and optionally populates sample demo entities. Automatically increments the installation count for the blueprint.

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
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60003') # UUID | Unique UUID of the blueprint to install
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
 **id** | **UUID**| Unique UUID of the blueprint to install | 
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
**204** | Blueprint successfully installed into the target project |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - Insufficient project permissions |  -  |
**404** | Blueprint not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_marketplace_keywords**
> ListMarketplaceKeywords200Response list_marketplace_keywords()

List marketplace keywords

Retrieves all distinct categorization keywords and tags associated with published blueprints along with their total occurrence count, ordered by popularity descending. Useful for populating discovery tags, filters, and keyword clouds.

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
        # List marketplace keywords
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

Publishes a new blueprint to the public marketplace or updates an existing blueprint owned by the authenticated user. Snapshots selected templates, attributes, and optional sample entities into an exportable blueprint package with title, description, and searchable keywords.

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
**201** | Blueprint successfully published |  -  |
**200** | Blueprint successfully updated |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - Not the owner of the blueprint |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_marketplace_blueprints**
> SearchMarketplaceBlueprints200Response search_marketplace_blueprints(search=search, keywords=keywords, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, featured=featured)

Search marketplace blueprints

Searches and lists public blueprints available in the marketplace catalog. Blueprints package reusable template schemas, attribute definitions, and sample data that users can install directly into their projects. Supports full-text search across titles and descriptions, keyword tag filtering, filtering by featured status, and sorting by creation date, install counts, or title.

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
    search = 'crm pipeline' # str | Free-text search filter across blueprint title and description (optional)
    keywords = 'crm,sales,leads' # str | Comma-separated keywords or tags to filter blueprints (optional)
    limit = 20 # int | Number of blueprint records to return per page (max 100) (optional) (default to 20)
    offset = 0 # int | Number of blueprint records to skip for pagination (optional) (default to 0)
    sort_by = created_at # str | Field to sort blueprint results by (optional) (default to created_at)
    sort_direction = desc # str | Sort direction order (ascending or descending) (optional) (default to desc)
    featured = true # bool | Filter to return only curated and featured marketplace blueprints (optional)

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
 **search** | **str**| Free-text search filter across blueprint title and description | [optional] 
 **keywords** | **str**| Comma-separated keywords or tags to filter blueprints | [optional] 
 **limit** | **int**| Number of blueprint records to return per page (max 100) | [optional] [default to 20]
 **offset** | **int**| Number of blueprint records to skip for pagination | [optional] [default to 0]
 **sort_by** | **str**| Field to sort blueprint results by | [optional] [default to created_at]
 **sort_direction** | **str**| Sort direction order (ascending or descending) | [optional] [default to desc]
 **featured** | **bool**| Filter to return only curated and featured marketplace blueprints | [optional] 

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
**200** | Paginated list of marketplace blueprints |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

