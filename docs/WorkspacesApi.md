# omnismith_sdk.WorkspacesApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace**](WorkspacesApi.md#create_workspace) | **POST** /workspaces | Create a new workspace
[**create_workspace_view**](WorkspacesApi.md#create_workspace_view) | **POST** /workspaces/{id}/views | Add a new view / pane to a workspace
[**delete_workspace**](WorkspacesApi.md#delete_workspace) | **DELETE** /workspaces/{id} | Delete a workspace and its views
[**delete_workspace_view**](WorkspacesApi.md#delete_workspace_view) | **DELETE** /workspaces/{id}/views/{viewId} | Delete a view / pane from a workspace
[**duplicate_workspace**](WorkspacesApi.md#duplicate_workspace) | **POST** /workspaces/{id}/duplicate | Duplicate an existing workspace and its views
[**get_workspace**](WorkspacesApi.md#get_workspace) | **GET** /workspaces/{id} | Get workspace details and its views
[**get_workspace_view**](WorkspacesApi.md#get_workspace_view) | **GET** /workspaces/{id}/views/{viewId} | Get details of a workspace view / pane
[**list_template_views**](WorkspacesApi.md#list_template_views) | **GET** /workspaces/template/{templateId} | List saved views for a specific template across workspaces
[**list_workspaces**](WorkspacesApi.md#list_workspaces) | **GET** /workspaces | List all workspaces for current project
[**reorder_workspace_views**](WorkspacesApi.md#reorder_workspace_views) | **PUT** /workspaces/{id}/reorder-views | Reorder views inside a workspace
[**set_default_workspace**](WorkspacesApi.md#set_default_workspace) | **POST** /workspaces/{id}/default | Set workspace as the default workspace
[**update_workspace**](WorkspacesApi.md#update_workspace) | **PUT** /workspaces/{id} | Update workspace metadata and layout
[**update_workspace_view**](WorkspacesApi.md#update_workspace_view) | **PUT** /workspaces/{id}/views/{viewId} | Update workspace view / pane filters, sort, display mode, or columns


# **create_workspace**
> CreateDashboard201Response create_workspace(create_workspace_request, x_omnismith_project_id=x_omnismith_project_id)

Create a new workspace

Creates a top-level operational workspace (workbench) in the current project context grouping related views for a specific workflow (e.g. "Editorial & Content Calendar", "Guidelines & Strategy", "Media Studio"). Workspaces appear in the top-level workspace switcher and support multi-pane layouts (single, split-v, split-h, quad) and default workspace indicators.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_dashboard201_response import CreateDashboard201Response
from omnismith_sdk.models.create_workspace_request import CreateWorkspaceRequest
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
    api_instance = omnismith_sdk.WorkspacesApi(api_client)
    create_workspace_request = omnismith_sdk.CreateWorkspaceRequest() # CreateWorkspaceRequest | Workspace creation payload
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Create a new workspace
        api_response = api_instance.create_workspace(create_workspace_request, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of WorkspacesApi->create_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workspace_request** | [**CreateWorkspaceRequest**](CreateWorkspaceRequest.md)| Workspace creation payload | 
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
**201** | Workspace created successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace_view**
> CreateDashboardBlock201Response create_workspace_view(id, create_workspace_view_request, x_omnismith_project_id=x_omnismith_project_id)

Add a new view / pane to a workspace

Creates and mounts a new view pane within an existing workspace bound to a specific entity schema template, configuring presentation mode (table, grid), visible columns, filter criteria, search queries (keyword or semantic), sorting preferences, and pane order. A workspace view represents a specialized filtered lens (e.g. "Telegram Channel Hub" filtered for platform=telegram) inside an operational workspace.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_dashboard_block201_response import CreateDashboardBlock201Response
from omnismith_sdk.models.create_workspace_view_request import CreateWorkspaceViewRequest
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
    api_instance = omnismith_sdk.WorkspacesApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Target workspace unique identifier (UUID)
    create_workspace_view_request = omnismith_sdk.CreateWorkspaceViewRequest() # CreateWorkspaceViewRequest | Workspace view creation payload
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Add a new view / pane to a workspace
        api_response = api_instance.create_workspace_view(id, create_workspace_view_request, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of WorkspacesApi->create_workspace_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->create_workspace_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Target workspace unique identifier (UUID) | 
 **create_workspace_view_request** | [**CreateWorkspaceViewRequest**](CreateWorkspaceViewRequest.md)| Workspace view creation payload | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**CreateDashboardBlock201Response**](CreateDashboardBlock201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Workspace view created successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace**
> delete_workspace(id, x_omnismith_project_id=x_omnismith_project_id)

Delete a workspace and its views

Permanently removes a workspace and all nested view pane configurations from the project.

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
    api_instance = omnismith_sdk.WorkspacesApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Workspace unique identifier (UUID) to delete
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Delete a workspace and its views
        api_instance.delete_workspace(id, x_omnismith_project_id=x_omnismith_project_id)
    except Exception as e:
        print("Exception when calling WorkspacesApi->delete_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Workspace unique identifier (UUID) to delete | 
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
**204** | Workspace deleted successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_view**
> delete_workspace_view(id, view_id, x_omnismith_project_id=x_omnismith_project_id)

Delete a view / pane from a workspace

Permanently removes a view pane from a workspace.

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
    api_instance = omnismith_sdk.WorkspacesApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Workspace unique identifier (UUID)
    view_id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6c') # UUID | Workspace view unique identifier (UUID) to delete
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Delete a view / pane from a workspace
        api_instance.delete_workspace_view(id, view_id, x_omnismith_project_id=x_omnismith_project_id)
    except Exception as e:
        print("Exception when calling WorkspacesApi->delete_workspace_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Workspace unique identifier (UUID) | 
 **view_id** | **UUID**| Workspace view unique identifier (UUID) to delete | 
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
**204** | Workspace view deleted successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_workspace**
> DuplicateWorkspace201Response duplicate_workspace(id, x_omnismith_project_id=x_omnismith_project_id, duplicate_workspace_request=duplicate_workspace_request)

Duplicate an existing workspace and its views

Creates a deep copy of an existing workspace, cloning all nested view panes, filter rules, display configurations, and layout settings into a new workspace with an optional customized name.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.duplicate_workspace201_response import DuplicateWorkspace201Response
from omnismith_sdk.models.duplicate_workspace_request import DuplicateWorkspaceRequest
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
    api_instance = omnismith_sdk.WorkspacesApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Source workspace unique identifier (UUID) to clone
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)
    duplicate_workspace_request = omnismith_sdk.DuplicateWorkspaceRequest() # DuplicateWorkspaceRequest | Optional configuration for the duplicated workspace (optional)

    try:
        # Duplicate an existing workspace and its views
        api_response = api_instance.duplicate_workspace(id, x_omnismith_project_id=x_omnismith_project_id, duplicate_workspace_request=duplicate_workspace_request)
        print("The response of WorkspacesApi->duplicate_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->duplicate_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Source workspace unique identifier (UUID) to clone | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 
 **duplicate_workspace_request** | [**DuplicateWorkspaceRequest**](DuplicateWorkspaceRequest.md)| Optional configuration for the duplicated workspace | [optional] 

### Return type

[**DuplicateWorkspace201Response**](DuplicateWorkspace201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Workspace duplicated successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace**
> WorkspaceDetailsResponse get_workspace(id, x_omnismith_project_id=x_omnismith_project_id)

Get workspace details and its views

Retrieves detailed information for a specific workspace, including its multi-pane layout configuration and all hydrated view panes with their associated template schemas, filter rules, search criteria, column selections, and ordering.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.workspace_details_response import WorkspaceDetailsResponse
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
    api_instance = omnismith_sdk.WorkspacesApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Workspace unique identifier (UUID)
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Get workspace details and its views
        api_response = api_instance.get_workspace(id, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of WorkspacesApi->get_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Workspace unique identifier (UUID) | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**WorkspaceDetailsResponse**](WorkspaceDetailsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace details with hydrated views |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_view**
> WorkspaceViewResponse get_workspace_view(id, view_id, x_omnismith_project_id=x_omnismith_project_id)

Get details of a workspace view / pane

Retrieves complete configuration details for a single workspace view pane, including its schema template binding, active filter rules, search parameters, column visibility, sort order, and layout positioning.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.workspace_view_response import WorkspaceViewResponse
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
    api_instance = omnismith_sdk.WorkspacesApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Workspace unique identifier (UUID)
    view_id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6c') # UUID | Workspace view unique identifier (UUID)
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Get details of a workspace view / pane
        api_response = api_instance.get_workspace_view(id, view_id, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of WorkspacesApi->get_workspace_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->get_workspace_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Workspace unique identifier (UUID) | 
 **view_id** | **UUID**| Workspace view unique identifier (UUID) | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**WorkspaceViewResponse**](WorkspaceViewResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace view details |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_template_views**
> ListTemplateViews200Response list_template_views(template_id, x_omnismith_project_id=x_omnismith_project_id)

List saved views for a specific template across workspaces

Searches and returns all saved workspace view panes configured across any workspace that are bound to a specific entity schema template, facilitating cross-workspace view reuse and discovery.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_template_views200_response import ListTemplateViews200Response
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
    api_instance = omnismith_sdk.WorkspacesApi(api_client)
    template_id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Schema template unique identifier (UUID)
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # List saved views for a specific template across workspaces
        api_response = api_instance.list_template_views(template_id, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of WorkspacesApi->list_template_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->list_template_views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **UUID**| Schema template unique identifier (UUID) | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**ListTemplateViews200Response**](ListTemplateViews200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of saved views for template |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspaces**
> ListWorkspaces200Response list_workspaces(x_omnismith_project_id=x_omnismith_project_id)

List all workspaces for current project

Retrieves all top-level operational workspaces configured within the authenticated project context, including multi-pane layout structures (single, split-v, split-h, quad), view pane counts, sort ordering, and default workspace indicators for workbench navigation.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_workspaces200_response import ListWorkspaces200Response
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
    api_instance = omnismith_sdk.WorkspacesApi(api_client)
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # List all workspaces for current project
        api_response = api_instance.list_workspaces(x_omnismith_project_id=x_omnismith_project_id)
        print("The response of WorkspacesApi->list_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->list_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**ListWorkspaces200Response**](ListWorkspaces200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of workspaces |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reorder_workspace_views**
> reorder_workspace_views(id, reorder_workspace_views_request, x_omnismith_project_id=x_omnismith_project_id)

Reorder views inside a workspace

Updates the visual sequence and tab ordering of view panes inside a workspace by supplying an ordered list of view IDs matching the desired layout arrangement.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.reorder_workspace_views_request import ReorderWorkspaceViewsRequest
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
    api_instance = omnismith_sdk.WorkspacesApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Workspace unique identifier (UUID)
    reorder_workspace_views_request = omnismith_sdk.ReorderWorkspaceViewsRequest() # ReorderWorkspaceViewsRequest | Payload containing ordered view IDs
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Reorder views inside a workspace
        api_instance.reorder_workspace_views(id, reorder_workspace_views_request, x_omnismith_project_id=x_omnismith_project_id)
    except Exception as e:
        print("Exception when calling WorkspacesApi->reorder_workspace_views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Workspace unique identifier (UUID) | 
 **reorder_workspace_views_request** | [**ReorderWorkspaceViewsRequest**](ReorderWorkspaceViewsRequest.md)| Payload containing ordered view IDs | 
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
**204** | Workspace views reordered successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_default_workspace**
> set_default_workspace(id, x_omnismith_project_id=x_omnismith_project_id)

Set workspace as the default workspace

Designates the specified workspace as the primary/default landing view for the project, automatically demoting any existing default workspace.

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
    api_instance = omnismith_sdk.WorkspacesApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Workspace unique identifier (UUID) to designate as default
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Set workspace as the default workspace
        api_instance.set_default_workspace(id, x_omnismith_project_id=x_omnismith_project_id)
    except Exception as e:
        print("Exception when calling WorkspacesApi->set_default_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Workspace unique identifier (UUID) to designate as default | 
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
**204** | Workspace designated as default successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace**
> update_workspace(id, update_workspace_request, x_omnismith_project_id=x_omnismith_project_id)

Update workspace metadata and layout

Updates workspace attributes including display name, description, multi-pane layout arrangement (single, split-v, split-h, quad), sort order sequence, and default workspace status.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.update_workspace_request import UpdateWorkspaceRequest
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
    api_instance = omnismith_sdk.WorkspacesApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Workspace unique identifier (UUID) to update
    update_workspace_request = omnismith_sdk.UpdateWorkspaceRequest() # UpdateWorkspaceRequest | Workspace update payload
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Update workspace metadata and layout
        api_instance.update_workspace(id, update_workspace_request, x_omnismith_project_id=x_omnismith_project_id)
    except Exception as e:
        print("Exception when calling WorkspacesApi->update_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Workspace unique identifier (UUID) to update | 
 **update_workspace_request** | [**UpdateWorkspaceRequest**](UpdateWorkspaceRequest.md)| Workspace update payload | 
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
**204** | Workspace updated successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace_view**
> update_workspace_view(id, view_id, update_workspace_view_request, x_omnismith_project_id=x_omnismith_project_id)

Update workspace view / pane filters, sort, display mode, or columns

Updates the configuration of a specific workspace view pane, modifying its title, filtering rules, search query and mode, sorting preferences, presentation display mode (table or grid), column visibility lists, or pane display sequence. A workspace view represents a specialized filtered lens (e.g. "Telegram Channel Hub") inside an operational workspace.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.update_workspace_view_request import UpdateWorkspaceViewRequest
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
    api_instance = omnismith_sdk.WorkspacesApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Workspace unique identifier (UUID)
    view_id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6c') # UUID | Workspace view unique identifier (UUID) to update
    update_workspace_view_request = omnismith_sdk.UpdateWorkspaceViewRequest() # UpdateWorkspaceViewRequest | Workspace view update payload
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Update workspace view / pane filters, sort, display mode, or columns
        api_instance.update_workspace_view(id, view_id, update_workspace_view_request, x_omnismith_project_id=x_omnismith_project_id)
    except Exception as e:
        print("Exception when calling WorkspacesApi->update_workspace_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Workspace unique identifier (UUID) | 
 **view_id** | **UUID**| Workspace view unique identifier (UUID) to update | 
 **update_workspace_view_request** | [**UpdateWorkspaceViewRequest**](UpdateWorkspaceViewRequest.md)| Workspace view update payload | 
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
**204** | Workspace view updated successfully |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

