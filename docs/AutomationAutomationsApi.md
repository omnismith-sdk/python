# omnismith_sdk.AutomationAutomationsApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_automation**](AutomationAutomationsApi.md#create_automation) | **POST** /automation/automations | Create an automation rule
[**delete_automation**](AutomationAutomationsApi.md#delete_automation) | **DELETE** /automation/automations/{id} | Delete an automation
[**get_automation**](AutomationAutomationsApi.md#get_automation) | **GET** /automation/automations/{id} | Get an automation by ID
[**list_automation_executions**](AutomationAutomationsApi.md#list_automation_executions) | **GET** /automation/automations/{id}/executions | List automation execution logs
[**list_automations**](AutomationAutomationsApi.md#list_automations) | **GET** /automation/automations | List project automations
[**toggle_automation**](AutomationAutomationsApi.md#toggle_automation) | **PATCH** /automation/automations/{id}/toggle | Toggle automation enabled status
[**update_automation**](AutomationAutomationsApi.md#update_automation) | **PUT** /automation/automations/{id} | Update an automation


# **create_automation**
> CreateAutomation201Response create_automation(create_automation_request)

Create an automation rule

Creates a new event-driven automation rule within the current project. Configures event trigger criteria (such as `on_entity_created`, `on_entity_updated`, or `on_attribute_changed`), multi-condition filters evaluating attribute values (using operators `eq`, `neq`, `gt`, `gte`, `lt`, `lte`, `contains`, `not_contains`, `is_empty`, `is_not_empty` across current value or delta modes), automated action targets (`telegram`, `webhook`, `push`), and an optional cooldown window in seconds to throttle repeated firings for the same entity.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_automation201_response import CreateAutomation201Response
from omnismith_sdk.models.create_automation_request import CreateAutomationRequest
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
    api_instance = omnismith_sdk.AutomationAutomationsApi(api_client)
    create_automation_request = omnismith_sdk.CreateAutomationRequest() # CreateAutomationRequest | 

    try:
        # Create an automation rule
        api_response = api_instance.create_automation(create_automation_request)
        print("The response of AutomationAutomationsApi->create_automation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationAutomationsApi->create_automation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_automation_request** | [**CreateAutomationRequest**](CreateAutomationRequest.md)|  | 

### Return type

[**CreateAutomation201Response**](CreateAutomation201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Automation successfully created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Tier quota exceeded |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_automation**
> delete_automation(id)

Delete an automation

Permanently deletes an automation rule by UUID, unbinding event listeners and stopping all future evaluations and action dispatches for that rule.

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
    api_instance = omnismith_sdk.AutomationAutomationsApi(api_client)
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60001') # UUID | Unique automation UUID to delete

    try:
        # Delete an automation
        api_instance.delete_automation(id)
    except Exception as e:
        print("Exception when calling AutomationAutomationsApi->delete_automation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique automation UUID to delete | 

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
**204** | Automation successfully deleted |  -  |
**401** | Unauthorized |  -  |
**404** | Automation not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_automation**
> AutomationResponse get_automation(id)

Get an automation by ID

Retrieves the complete configuration of a specific automation rule by its UUID, including trigger event types, template/attribute references, condition comparison expressions, action payloads, execution cooldown interval, and the timestamp of its last execution.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.automation_response import AutomationResponse
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
    api_instance = omnismith_sdk.AutomationAutomationsApi(api_client)
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60001') # UUID | Unique automation UUID

    try:
        # Get an automation by ID
        api_response = api_instance.get_automation(id)
        print("The response of AutomationAutomationsApi->get_automation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationAutomationsApi->get_automation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique automation UUID | 

### Return type

[**AutomationResponse**](AutomationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Automation details |  -  |
**401** | Unauthorized |  -  |
**404** | Automation not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_automation_executions**
> ListAutomationExecutions200Response list_automation_executions(id, limit=limit, offset=offset, status=status)

List automation execution logs

Retrieves paginated execution logs and audit history for a specific automation rule. Each execution log records the triggering entity ID, trigger timestamp, execution completion time, final status (`pending`, `success`, `partial_failure`, `failed`), detailed action dispatch outcomes with error messages, and top-level execution errors.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_automation_executions200_response import ListAutomationExecutions200Response
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
    api_instance = omnismith_sdk.AutomationAutomationsApi(api_client)
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60001') # UUID | Automation UUID to fetch execution history for
    limit = 20 # int | Maximum number of execution log entries to return per page (optional) (default to 20)
    offset = 0 # int | Number of execution log records to skip for pagination (optional) (default to 0)
    status = 'success' # str | Filter execution logs by execution outcome status (optional)

    try:
        # List automation execution logs
        api_response = api_instance.list_automation_executions(id, limit=limit, offset=offset, status=status)
        print("The response of AutomationAutomationsApi->list_automation_executions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationAutomationsApi->list_automation_executions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Automation UUID to fetch execution history for | 
 **limit** | **int**| Maximum number of execution log entries to return per page | [optional] [default to 20]
 **offset** | **int**| Number of execution log records to skip for pagination | [optional] [default to 0]
 **status** | **str**| Filter execution logs by execution outcome status | [optional] 

### Return type

[**ListAutomationExecutions200Response**](ListAutomationExecutions200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of execution logs |  -  |
**401** | Unauthorized |  -  |
**404** | Automation not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_automations**
> List[AutomationResponse] list_automations(template_id=template_id, is_enabled=is_enabled)

List project automations

Retrieves all automation rules configured within the current project context. Automations define event-driven workflows triggered by entity lifecycle events (such as entity creation, attribute updates, or metric threshold changes), evaluated against multi-attribute conditions, and dispatched to configured action channels (Telegram, webhooks, mobile push). Results can be filtered by entity template or active status.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.automation_response import AutomationResponse
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
    api_instance = omnismith_sdk.AutomationAutomationsApi(api_client)
    template_id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60088') # UUID | Filter automations scoped to a specific entity template UUID (optional)
    is_enabled = true # bool | Filter automations by active enabled status (true for active rules, false for paused rules) (optional)

    try:
        # List project automations
        api_response = api_instance.list_automations(template_id=template_id, is_enabled=is_enabled)
        print("The response of AutomationAutomationsApi->list_automations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationAutomationsApi->list_automations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **UUID**| Filter automations scoped to a specific entity template UUID | [optional] 
 **is_enabled** | **bool**| Filter automations by active enabled status (true for active rules, false for paused rules) | [optional] 

### Return type

[**List[AutomationResponse]**](AutomationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of automation rules |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_automation**
> AutomationResponse toggle_automation(id, toggle_automation_request)

Toggle automation enabled status

Enables or pauses an automation rule without altering its trigger definitions, condition criteria, or action configurations. Paused automations are ignored during event processing.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.automation_response import AutomationResponse
from omnismith_sdk.models.toggle_automation_request import ToggleAutomationRequest
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
    api_instance = omnismith_sdk.AutomationAutomationsApi(api_client)
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60001') # UUID | Unique automation UUID to toggle
    toggle_automation_request = omnismith_sdk.ToggleAutomationRequest() # ToggleAutomationRequest | 

    try:
        # Toggle automation enabled status
        api_response = api_instance.toggle_automation(id, toggle_automation_request)
        print("The response of AutomationAutomationsApi->toggle_automation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationAutomationsApi->toggle_automation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique automation UUID to toggle | 
 **toggle_automation_request** | [**ToggleAutomationRequest**](ToggleAutomationRequest.md)|  | 

### Return type

[**AutomationResponse**](AutomationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Automation status successfully toggled |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_automation**
> update_automation(id, update_automation_request)

Update an automation

Updates an existing automation rule by UUID. Supports modifying rule name, description, trigger event definitions, condition filter criteria, action dispatches, and cooldown throttle settings.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.update_automation_request import UpdateAutomationRequest
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
    api_instance = omnismith_sdk.AutomationAutomationsApi(api_client)
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60001') # UUID | Unique automation UUID to update
    update_automation_request = omnismith_sdk.UpdateAutomationRequest() # UpdateAutomationRequest | 

    try:
        # Update an automation
        api_instance.update_automation(id, update_automation_request)
    except Exception as e:
        print("Exception when calling AutomationAutomationsApi->update_automation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique automation UUID to update | 
 **update_automation_request** | [**UpdateAutomationRequest**](UpdateAutomationRequest.md)|  | 

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
**204** | Automation successfully updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Automation not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

