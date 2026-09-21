# omnismith_sdk.DashboardsApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard**](DashboardsApi.md#create_dashboard) | **POST** /dashboards | Create a new dashboard
[**delete_dashboard**](DashboardsApi.md#delete_dashboard) | **DELETE** /dashboards/{id} | Delete a dashboard
[**get_dashboard**](DashboardsApi.md#get_dashboard) | **GET** /dashboards/{id} | Get a dashboard by ID
[**list_dashboards**](DashboardsApi.md#list_dashboards) | **GET** /dashboards | List all dashboards
[**update_dashboard**](DashboardsApi.md#update_dashboard) | **PUT** /dashboards/{id} | Update a dashboard


# **create_dashboard**
> CreateDashboard201Response create_dashboard(create_dashboard_request, x_omnismith_project_id=x_omnismith_project_id)

Create a new dashboard

Creates a new analytics and telemetry dashboard canvas for organizing metric KPIs, charts, gauges, and entity tables within a customizable grid layout.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_dashboard201_response import CreateDashboard201Response
from omnismith_sdk.models.create_dashboard_request import CreateDashboardRequest
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
    api_instance = omnismith_sdk.DashboardsApi(api_client)
    create_dashboard_request = omnismith_sdk.CreateDashboardRequest() # CreateDashboardRequest | Dashboard creation payload
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Create a new dashboard
        api_response = api_instance.create_dashboard(create_dashboard_request, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of DashboardsApi->create_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->create_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_dashboard_request** | [**CreateDashboardRequest**](CreateDashboardRequest.md)| Dashboard creation payload | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**CreateDashboard201Response**](CreateDashboard201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Dashboard created successfully |  -  |
**401** | Unauthorized |  -  |
**402** | Tier quota exceeded |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard**
> delete_dashboard(id, x_omnismith_project_id=x_omnismith_project_id)

Delete a dashboard

Permanently removes a dashboard and all attached visualization blocks, metric widgets, and configurations.

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
    api_instance = omnismith_sdk.DashboardsApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Dashboard unique identifier (UUID) to delete
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Delete a dashboard
        api_instance.delete_dashboard(id, x_omnismith_project_id=x_omnismith_project_id)
    except Exception as e:
        print("Exception when calling DashboardsApi->delete_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Dashboard unique identifier (UUID) to delete | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

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
**204** | Dashboard deleted successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard**
> DashboardResponse get_dashboard(id, x_omnismith_project_id=x_omnismith_project_id)

Get a dashboard by ID

Retrieves metadata and top-level configuration for a specific dashboard by its unique identifier.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.dashboard_response import DashboardResponse
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
    api_instance = omnismith_sdk.DashboardsApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Dashboard unique identifier (UUID)
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Get a dashboard by ID
        api_response = api_instance.get_dashboard(id, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of DashboardsApi->get_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->get_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Dashboard unique identifier (UUID) | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**DashboardResponse**](DashboardResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dashboard details |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dashboards**
> ListDashboards200Response list_dashboards(x_omnismith_project_id=x_omnismith_project_id)

List all dashboards

Retrieves all analytics dashboards configured within the authenticated project context, including dashboard metadata, layout settings, and visualization configurations.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_dashboards200_response import ListDashboards200Response
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
    api_instance = omnismith_sdk.DashboardsApi(api_client)
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # List all dashboards
        api_response = api_instance.list_dashboards(x_omnismith_project_id=x_omnismith_project_id)
        print("The response of DashboardsApi->list_dashboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->list_dashboards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**ListDashboards200Response**](ListDashboards200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of dashboards |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard**
> update_dashboard(id, update_dashboard_request, x_omnismith_project_id=x_omnismith_project_id)

Update a dashboard

Updates dashboard metadata including its display name, description, and canvas layout settings.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.update_dashboard_request import UpdateDashboardRequest
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
    api_instance = omnismith_sdk.DashboardsApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Dashboard unique identifier (UUID) to update
    update_dashboard_request = omnismith_sdk.UpdateDashboardRequest() # UpdateDashboardRequest | Dashboard update payload
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Update a dashboard
        api_instance.update_dashboard(id, update_dashboard_request, x_omnismith_project_id=x_omnismith_project_id)
    except Exception as e:
        print("Exception when calling DashboardsApi->update_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Dashboard unique identifier (UUID) to update | 
 **update_dashboard_request** | [**UpdateDashboardRequest**](UpdateDashboardRequest.md)| Dashboard update payload | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

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
**204** | Dashboard updated successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

