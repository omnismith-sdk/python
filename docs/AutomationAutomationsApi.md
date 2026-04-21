# omnismith_sdk.AutomationAutomationsApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_automation**](AutomationAutomationsApi.md#create_automation) | **POST** /automation/automations | Create a new automation
[**delete_automation**](AutomationAutomationsApi.md#delete_automation) | **DELETE** /automation/automations/{id} | Delete an automation
[**get_automation**](AutomationAutomationsApi.md#get_automation) | **GET** /automation/automations/{id} | Get an automation by ID
[**list_automation_executions**](AutomationAutomationsApi.md#list_automation_executions) | **GET** /automation/automations/{id}/executions | List automation executions
[**list_automations**](AutomationAutomationsApi.md#list_automations) | **GET** /automation/automations | List automations
[**toggle_automation**](AutomationAutomationsApi.md#toggle_automation) | **PATCH** /automation/automations/{id}/toggle | Toggle automation enabled status
[**update_automation**](AutomationAutomationsApi.md#update_automation) | **PUT** /automation/automations/{id} | Update an automation


# **create_automation**
> CreateAttributeItem201Response create_automation(create_automation_request)

Create a new automation

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_attribute_item201_response import CreateAttributeItem201Response
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
        # Create a new automation
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

[**CreateAttributeItem201Response**](CreateAttributeItem201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Automation created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Tier quota exceeded |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_automation**
> delete_automation(id)

Delete an automation

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
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete an automation
        api_instance.delete_automation(id)
    except Exception as e:
        print("Exception when calling AutomationAutomationsApi->delete_automation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

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
**204** | Automation deleted |  -  |
**401** | Unauthorized |  -  |
**404** | Automation not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_automation**
> AutomationResponse get_automation(id)

Get an automation by ID

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
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **id** | **UUID**|  | 

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

List automation executions

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
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Automation ID
    limit = 20 # int | Number of results (optional) (default to 20)
    offset = 0 # int | Pagination offset (optional) (default to 0)
    status = 'status_example' # str | Filter by status (optional)

    try:
        # List automation executions
        api_response = api_instance.list_automation_executions(id, limit=limit, offset=offset, status=status)
        print("The response of AutomationAutomationsApi->list_automation_executions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationAutomationsApi->list_automation_executions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Automation ID | 
 **limit** | **int**| Number of results | [optional] [default to 20]
 **offset** | **int**| Pagination offset | [optional] [default to 0]
 **status** | **str**| Filter by status | [optional] 

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
**200** | List of executions |  -  |
**401** | Unauthorized |  -  |
**404** | Automation not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_automations**
> List[AutomationResponse] list_automations(template_id=template_id, is_enabled=is_enabled)

List automations

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
    template_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Filter by template ID (optional)
    is_enabled = True # bool | Filter by enabled status (optional)

    try:
        # List automations
        api_response = api_instance.list_automations(template_id=template_id, is_enabled=is_enabled)
        print("The response of AutomationAutomationsApi->list_automations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationAutomationsApi->list_automations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **UUID**| Filter by template ID | [optional] 
 **is_enabled** | **bool**| Filter by enabled status | [optional] 

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
**200** | List of automations |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_automation**
> AutomationResponse toggle_automation(id, toggle_automation_request)

Toggle automation enabled status

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
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
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
 **id** | **UUID**|  | 
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
**200** | Automation toggled |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_automation**
> update_automation(id, update_automation_request)

Update an automation

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
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
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
 **id** | **UUID**|  | 
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
**204** | Automation updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Automation not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

