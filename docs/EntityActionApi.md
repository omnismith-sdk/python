# omnismith_sdk.EntityActionApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_template_action**](EntityActionApi.md#create_template_action) | **POST** /templates/{templateId}/actions | Create an action on a template
[**delete_template_action**](EntityActionApi.md#delete_template_action) | **DELETE** /templates/{templateId}/actions/{id} | Delete an action
[**get_template_action**](EntityActionApi.md#get_template_action) | **GET** /templates/{templateId}/actions/{id} | Get an action definition
[**list_template_actions**](EntityActionApi.md#list_template_actions) | **GET** /templates/{templateId}/actions | List the actions defined on a template
[**reorder_template_actions**](EntityActionApi.md#reorder_template_actions) | **PUT** /templates/{templateId}/actions/order | Reorder the actions of a template
[**toggle_template_action**](EntityActionApi.md#toggle_template_action) | **POST** /templates/{templateId}/actions/{id}/toggle | Enable or disable an action
[**update_template_action**](EntityActionApi.md#update_template_action) | **PUT** /templates/{templateId}/actions/{id} | Replace an action definition


# **create_template_action**
> CreateTemplateAction201Response create_template_action(template_id, create_entity_action_request, x_omnismith_project_id=x_omnismith_project_id)

Create an action on a template

Defines a named operation on records of a template. `precondition` gates availability (all conditions must hold against the record's current values; empty means always available), `fields` are the values the operator is asked for in dialog order, `presets` are written silently when the action runs. A status transition is `precondition: [status eq <draft-id>]`, `presets: [status = <confirmed-id>]`, no fields. The slug must be unique within the template. Fields and presets must name distinct non-metric attributes of the template and may not overlap. New actions are enabled and appended last.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_entity_action_request import CreateEntityActionRequest
from omnismith_sdk.models.create_template_action201_response import CreateTemplateAction201Response
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
    api_instance = omnismith_sdk.EntityActionApi(api_client)
    template_id = '018b2f1b-8c1a-75b3-8000-7f0000010010' # str | UUID or slug of the template
    create_entity_action_request = omnismith_sdk.CreateEntityActionRequest() # CreateEntityActionRequest | 
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Create an action on a template
        api_response = api_instance.create_template_action(template_id, create_entity_action_request, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of EntityActionApi->create_template_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityActionApi->create_template_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| UUID or slug of the template | 
 **create_entity_action_request** | [**CreateEntityActionRequest**](CreateEntityActionRequest.md)|  | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**CreateTemplateAction201Response**](CreateTemplateAction201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Action created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_action**
> delete_template_action(template_id, id, x_omnismith_project_id=x_omnismith_project_id)

Delete an action

Permanently removes an action from its template. Records the action was run on are not affected.

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
    api_instance = omnismith_sdk.EntityActionApi(api_client)
    template_id = '018b2f1b-8c1a-75b3-8000-7f0000010010' # str | UUID or slug of the template
    id = UUID('01a09900-0000-7000-8000-000000000001') # UUID | Action UUID
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Delete an action
        api_instance.delete_template_action(template_id, id, x_omnismith_project_id=x_omnismith_project_id)
    except Exception as e:
        print("Exception when calling EntityActionApi->delete_template_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| UUID or slug of the template | 
 **id** | **UUID**| Action UUID | 
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
**204** | Action deleted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_action**
> EntityActionResponse get_template_action(template_id, id, x_omnismith_project_id=x_omnismith_project_id)

Get an action definition

Returns one action of a template with its precondition, fields and presets.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.entity_action_response import EntityActionResponse
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
    api_instance = omnismith_sdk.EntityActionApi(api_client)
    template_id = '018b2f1b-8c1a-75b3-8000-7f0000010010' # str | UUID or slug of the template
    id = UUID('01a09900-0000-7000-8000-000000000001') # UUID | Action UUID
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Get an action definition
        api_response = api_instance.get_template_action(template_id, id, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of EntityActionApi->get_template_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityActionApi->get_template_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| UUID or slug of the template | 
 **id** | **UUID**| Action UUID | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**EntityActionResponse**](EntityActionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Action definition |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_template_actions**
> ListTemplateActions200Response list_template_actions(template_id, x_omnismith_project_id=x_omnismith_project_id, is_enabled=is_enabled)

List the actions defined on a template

Returns every action definition of a template in display order, including disabled ones unless filtered. An action is a named operation on one record: a precondition on current values, the fields the operator supplies, and presets written silently. To learn which actions apply to a specific record, and to run one, use the entity action endpoints.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_template_actions200_response import ListTemplateActions200Response
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
    api_instance = omnismith_sdk.EntityActionApi(api_client)
    template_id = '018b2f1b-8c1a-75b3-8000-7f0000010010' # str | UUID or slug of the template
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)
    is_enabled = True # bool | Only enabled (`true`) or only disabled (`false`) actions (optional)

    try:
        # List the actions defined on a template
        api_response = api_instance.list_template_actions(template_id, x_omnismith_project_id=x_omnismith_project_id, is_enabled=is_enabled)
        print("The response of EntityActionApi->list_template_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityActionApi->list_template_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| UUID or slug of the template | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 
 **is_enabled** | **bool**| Only enabled (&#x60;true&#x60;) or only disabled (&#x60;false&#x60;) actions | [optional] 

### Return type

[**ListTemplateActions200Response**](ListTemplateActions200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Actions of the template in display order |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reorder_template_actions**
> ListTemplateActions200Response reorder_template_actions(template_id, reorder_entity_actions_request, x_omnismith_project_id=x_omnismith_project_id)

Reorder the actions of a template

Sets the display order of a template's actions from an ordered list of every action UUID. The list must contain each action of the template exactly once; a partial or repeated list is rejected with 422. Returns the actions in their new order.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_template_actions200_response import ListTemplateActions200Response
from omnismith_sdk.models.reorder_entity_actions_request import ReorderEntityActionsRequest
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
    api_instance = omnismith_sdk.EntityActionApi(api_client)
    template_id = '018b2f1b-8c1a-75b3-8000-7f0000010010' # str | UUID or slug of the template
    reorder_entity_actions_request = omnismith_sdk.ReorderEntityActionsRequest() # ReorderEntityActionsRequest | 
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Reorder the actions of a template
        api_response = api_instance.reorder_template_actions(template_id, reorder_entity_actions_request, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of EntityActionApi->reorder_template_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityActionApi->reorder_template_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| UUID or slug of the template | 
 **reorder_entity_actions_request** | [**ReorderEntityActionsRequest**](ReorderEntityActionsRequest.md)|  | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**ListTemplateActions200Response**](ListTemplateActions200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Actions in their new order |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_template_action**
> EntityActionResponse toggle_template_action(template_id, id, toggle_entity_action_request, x_omnismith_project_id=x_omnismith_project_id)

Enable or disable an action

Turns an action on or off without changing its definition. Disabled actions are stored but neither offered on records nor executable.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.entity_action_response import EntityActionResponse
from omnismith_sdk.models.toggle_entity_action_request import ToggleEntityActionRequest
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
    api_instance = omnismith_sdk.EntityActionApi(api_client)
    template_id = '018b2f1b-8c1a-75b3-8000-7f0000010010' # str | UUID or slug of the template
    id = UUID('01a09900-0000-7000-8000-000000000001') # UUID | Action UUID
    toggle_entity_action_request = omnismith_sdk.ToggleEntityActionRequest() # ToggleEntityActionRequest | 
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Enable or disable an action
        api_response = api_instance.toggle_template_action(template_id, id, toggle_entity_action_request, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of EntityActionApi->toggle_template_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityActionApi->toggle_template_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| UUID or slug of the template | 
 **id** | **UUID**| Action UUID | 
 **toggle_entity_action_request** | [**ToggleEntityActionRequest**](ToggleEntityActionRequest.md)|  | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**EntityActionResponse**](EntityActionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Action with its new enabled state |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_action**
> EntityActionResponse update_template_action(template_id, id, update_entity_action_request, x_omnismith_project_id=x_omnismith_project_id)

Replace an action definition

Replaces the slug, name, description, icon, precondition, fields and presets of an action. The enabled flag and position are unchanged; use the toggle and order endpoints for those. The same validation as on create applies.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.entity_action_response import EntityActionResponse
from omnismith_sdk.models.update_entity_action_request import UpdateEntityActionRequest
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
    api_instance = omnismith_sdk.EntityActionApi(api_client)
    template_id = '018b2f1b-8c1a-75b3-8000-7f0000010010' # str | UUID or slug of the template
    id = UUID('01a09900-0000-7000-8000-000000000001') # UUID | Action UUID
    update_entity_action_request = omnismith_sdk.UpdateEntityActionRequest() # UpdateEntityActionRequest | 
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Replace an action definition
        api_response = api_instance.update_template_action(template_id, id, update_entity_action_request, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of EntityActionApi->update_template_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityActionApi->update_template_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| UUID or slug of the template | 
 **id** | **UUID**| Action UUID | 
 **update_entity_action_request** | [**UpdateEntityActionRequest**](UpdateEntityActionRequest.md)|  | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**EntityActionResponse**](EntityActionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated action |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

