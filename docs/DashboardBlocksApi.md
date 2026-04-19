# omnismith_sdk.DashboardBlocksApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard_block**](DashboardBlocksApi.md#create_dashboard_block) | **POST** /dashboards/{dashboardId}/blocks | Create a new block in a dashboard
[**delete_dashboard_block**](DashboardBlocksApi.md#delete_dashboard_block) | **DELETE** /dashboards/{dashboardId}/blocks/{blockId} | Delete a dashboard block
[**get_dashboard_block**](DashboardBlocksApi.md#get_dashboard_block) | **GET** /dashboards/{dashboardId}/blocks/{blockId} | Get a dashboard block by ID
[**list_dashboard_blocks**](DashboardBlocksApi.md#list_dashboard_blocks) | **GET** /dashboards/{dashboardId}/blocks | List all blocks in a dashboard
[**resolve_dashboard_block**](DashboardBlocksApi.md#resolve_dashboard_block) | **GET** /dashboards/{dashboardId}/blocks/{blockId}/resolve | Resolve a dashboard block to its computed data
[**update_dashboard_block**](DashboardBlocksApi.md#update_dashboard_block) | **PUT** /dashboards/{dashboardId}/blocks/{blockId} | Update a dashboard block


# **create_dashboard_block**
> CreateAttributeItem201Response create_dashboard_block(dashboard_id, create_dashboard_block_request)

Create a new block in a dashboard

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_attribute_item201_response import CreateAttributeItem201Response
from omnismith_sdk.models.create_dashboard_block_request import CreateDashboardBlockRequest
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
    api_instance = omnismith_sdk.DashboardBlocksApi(api_client)
    dashboard_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Dashboard ID
    create_dashboard_block_request = omnismith_sdk.CreateDashboardBlockRequest() # CreateDashboardBlockRequest | 

    try:
        # Create a new block in a dashboard
        api_response = api_instance.create_dashboard_block(dashboard_id, create_dashboard_block_request)
        print("The response of DashboardBlocksApi->create_dashboard_block:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardBlocksApi->create_dashboard_block: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **UUID**| Dashboard ID | 
 **create_dashboard_block_request** | [**CreateDashboardBlockRequest**](CreateDashboardBlockRequest.md)|  | 

### Return type

[**CreateAttributeItem201Response**](CreateAttributeItem201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Block created |  -  |
**404** | Dashboard not found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_block**
> delete_dashboard_block(dashboard_id, block_id)

Delete a dashboard block

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
    api_instance = omnismith_sdk.DashboardBlocksApi(api_client)
    dashboard_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Dashboard ID
    block_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Block ID

    try:
        # Delete a dashboard block
        api_instance.delete_dashboard_block(dashboard_id, block_id)
    except Exception as e:
        print("Exception when calling DashboardBlocksApi->delete_dashboard_block: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **UUID**| Dashboard ID | 
 **block_id** | **UUID**| Block ID | 

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
**204** | Block deleted |  -  |
**404** | Block not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_block**
> DashboardBlockResponse get_dashboard_block(dashboard_id, block_id)

Get a dashboard block by ID

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.dashboard_block_response import DashboardBlockResponse
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
    api_instance = omnismith_sdk.DashboardBlocksApi(api_client)
    dashboard_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Dashboard ID
    block_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Block ID

    try:
        # Get a dashboard block by ID
        api_response = api_instance.get_dashboard_block(dashboard_id, block_id)
        print("The response of DashboardBlocksApi->get_dashboard_block:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardBlocksApi->get_dashboard_block: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **UUID**| Dashboard ID | 
 **block_id** | **UUID**| Block ID | 

### Return type

[**DashboardBlockResponse**](DashboardBlockResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Block details |  -  |
**404** | Block not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dashboard_blocks**
> ListDashboardBlocks200Response list_dashboard_blocks(dashboard_id)

List all blocks in a dashboard

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_dashboard_blocks200_response import ListDashboardBlocks200Response
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
    api_instance = omnismith_sdk.DashboardBlocksApi(api_client)
    dashboard_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Dashboard ID

    try:
        # List all blocks in a dashboard
        api_response = api_instance.list_dashboard_blocks(dashboard_id)
        print("The response of DashboardBlocksApi->list_dashboard_blocks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardBlocksApi->list_dashboard_blocks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **UUID**| Dashboard ID | 

### Return type

[**ListDashboardBlocks200Response**](ListDashboardBlocks200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of blocks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_dashboard_block**
> ResolvedBlockResponse resolve_dashboard_block(dashboard_id, block_id)

Resolve a dashboard block to its computed data

Executes the block configuration and returns computed values based on block type (stat count, gauge value, chart series, or list items)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.resolved_block_response import ResolvedBlockResponse
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
    api_instance = omnismith_sdk.DashboardBlocksApi(api_client)
    dashboard_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Dashboard ID
    block_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Block ID

    try:
        # Resolve a dashboard block to its computed data
        api_response = api_instance.resolve_dashboard_block(dashboard_id, block_id)
        print("The response of DashboardBlocksApi->resolve_dashboard_block:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardBlocksApi->resolve_dashboard_block: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **UUID**| Dashboard ID | 
 **block_id** | **UUID**| Block ID | 

### Return type

[**ResolvedBlockResponse**](ResolvedBlockResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resolved block data |  -  |
**404** | Block not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard_block**
> update_dashboard_block(dashboard_id, block_id, update_dashboard_block_request)

Update a dashboard block

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.update_dashboard_block_request import UpdateDashboardBlockRequest
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
    api_instance = omnismith_sdk.DashboardBlocksApi(api_client)
    dashboard_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Dashboard ID
    block_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Block ID
    update_dashboard_block_request = omnismith_sdk.UpdateDashboardBlockRequest() # UpdateDashboardBlockRequest | 

    try:
        # Update a dashboard block
        api_instance.update_dashboard_block(dashboard_id, block_id, update_dashboard_block_request)
    except Exception as e:
        print("Exception when calling DashboardBlocksApi->update_dashboard_block: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **UUID**| Dashboard ID | 
 **block_id** | **UUID**| Block ID | 
 **update_dashboard_block_request** | [**UpdateDashboardBlockRequest**](UpdateDashboardBlockRequest.md)|  | 

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
**200** | Block updated |  -  |
**404** | Block not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

