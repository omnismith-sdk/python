# omnismith_sdk.AutomationNotificationChannelsApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification_channel**](AutomationNotificationChannelsApi.md#create_notification_channel) | **POST** /automation/notification-channels | Create a new notification channel
[**delete_notification_channel**](AutomationNotificationChannelsApi.md#delete_notification_channel) | **DELETE** /automation/notification-channels/{id} | Delete a notification channel
[**get_notification_channel**](AutomationNotificationChannelsApi.md#get_notification_channel) | **GET** /automation/notification-channels/{id} | Get a notification channel
[**list_notification_channels**](AutomationNotificationChannelsApi.md#list_notification_channels) | **GET** /automation/notification-channels | List all notification channels
[**test_notification_channel**](AutomationNotificationChannelsApi.md#test_notification_channel) | **POST** /automation/notification-channels/{id}/test | Send a test message via the notification channel
[**update_notification_channel**](AutomationNotificationChannelsApi.md#update_notification_channel) | **PUT** /automation/notification-channels/{id} | Update a notification channel


# **create_notification_channel**
> CreateAttributeItem201Response create_notification_channel(create_notification_channel_request)

Create a new notification channel

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_attribute_item201_response import CreateAttributeItem201Response
from omnismith_sdk.models.create_notification_channel_request import CreateNotificationChannelRequest
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
    api_instance = omnismith_sdk.AutomationNotificationChannelsApi(api_client)
    create_notification_channel_request = omnismith_sdk.CreateNotificationChannelRequest() # CreateNotificationChannelRequest | 

    try:
        # Create a new notification channel
        api_response = api_instance.create_notification_channel(create_notification_channel_request)
        print("The response of AutomationNotificationChannelsApi->create_notification_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationNotificationChannelsApi->create_notification_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_notification_channel_request** | [**CreateNotificationChannelRequest**](CreateNotificationChannelRequest.md)|  | 

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
**201** | Channel created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Tier quota exceeded |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_channel**
> delete_notification_channel(id)

Delete a notification channel

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
    api_instance = omnismith_sdk.AutomationNotificationChannelsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Channel UUID

    try:
        # Delete a notification channel
        api_instance.delete_notification_channel(id)
    except Exception as e:
        print("Exception when calling AutomationNotificationChannelsApi->delete_notification_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Channel UUID | 

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
**204** | Channel deleted |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_channel**
> NotificationChannelResponse get_notification_channel(id)

Get a notification channel

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.notification_channel_response import NotificationChannelResponse
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
    api_instance = omnismith_sdk.AutomationNotificationChannelsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Channel UUID

    try:
        # Get a notification channel
        api_response = api_instance.get_notification_channel(id)
        print("The response of AutomationNotificationChannelsApi->get_notification_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationNotificationChannelsApi->get_notification_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Channel UUID | 

### Return type

[**NotificationChannelResponse**](NotificationChannelResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Channel details |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notification_channels**
> ListNotificationChannels200Response list_notification_channels()

List all notification channels

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_notification_channels200_response import ListNotificationChannels200Response
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
    api_instance = omnismith_sdk.AutomationNotificationChannelsApi(api_client)

    try:
        # List all notification channels
        api_response = api_instance.list_notification_channels()
        print("The response of AutomationNotificationChannelsApi->list_notification_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationNotificationChannelsApi->list_notification_channels: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListNotificationChannels200Response**](ListNotificationChannels200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of channels |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_notification_channel**
> TestNotificationChannel200Response test_notification_channel(id, test_notification_channel_request)

Send a test message via the notification channel

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.test_notification_channel200_response import TestNotificationChannel200Response
from omnismith_sdk.models.test_notification_channel_request import TestNotificationChannelRequest
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
    api_instance = omnismith_sdk.AutomationNotificationChannelsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Channel UUID
    test_notification_channel_request = omnismith_sdk.TestNotificationChannelRequest() # TestNotificationChannelRequest | 

    try:
        # Send a test message via the notification channel
        api_response = api_instance.test_notification_channel(id, test_notification_channel_request)
        print("The response of AutomationNotificationChannelsApi->test_notification_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationNotificationChannelsApi->test_notification_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Channel UUID | 
 **test_notification_channel_request** | [**TestNotificationChannelRequest**](TestNotificationChannelRequest.md)|  | 

### Return type

[**TestNotificationChannel200Response**](TestNotificationChannel200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Test message sent successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Test failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_channel**
> update_notification_channel(id, update_notification_channel_request)

Update a notification channel

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.update_notification_channel_request import UpdateNotificationChannelRequest
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
    api_instance = omnismith_sdk.AutomationNotificationChannelsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Channel UUID
    update_notification_channel_request = omnismith_sdk.UpdateNotificationChannelRequest() # UpdateNotificationChannelRequest | 

    try:
        # Update a notification channel
        api_instance.update_notification_channel(id, update_notification_channel_request)
    except Exception as e:
        print("Exception when calling AutomationNotificationChannelsApi->update_notification_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Channel UUID | 
 **update_notification_channel_request** | [**UpdateNotificationChannelRequest**](UpdateNotificationChannelRequest.md)|  | 

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
**204** | Channel updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

