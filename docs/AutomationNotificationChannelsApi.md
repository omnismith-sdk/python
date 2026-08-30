# omnismith_sdk.AutomationNotificationChannelsApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification_channel**](AutomationNotificationChannelsApi.md#create_notification_channel) | **POST** /automation/notification-channels | Create a notification channel
[**delete_notification_channel**](AutomationNotificationChannelsApi.md#delete_notification_channel) | **DELETE** /automation/notification-channels/{id} | Delete a notification channel
[**get_notification_channel**](AutomationNotificationChannelsApi.md#get_notification_channel) | **GET** /automation/notification-channels/{id} | Get a notification channel by ID
[**list_notification_channels**](AutomationNotificationChannelsApi.md#list_notification_channels) | **GET** /automation/notification-channels | List notification channels
[**test_notification_channel**](AutomationNotificationChannelsApi.md#test_notification_channel) | **POST** /automation/notification-channels/{id}/test | Send a test notification message
[**update_notification_channel**](AutomationNotificationChannelsApi.md#update_notification_channel) | **PUT** /automation/notification-channels/{id} | Update a notification channel


# **create_notification_channel**
> CreateNotificationChannel201Response create_notification_channel(create_notification_channel_request)

Create a notification channel

Registers a new external notification channel for the current project. Channels can be of type `telegram` (configured with a Telegram bot token), `webhook` (configured with endpoint URL, custom HTTP headers, and authentication methods such as bearer token or basic auth), or `push` (FCM mobile push notifications). Configured channels can then be linked as target actions in automation rules.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_notification_channel201_response import CreateNotificationChannel201Response
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
        # Create a notification channel
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

[**CreateNotificationChannel201Response**](CreateNotificationChannel201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Notification channel successfully created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Tier quota exceeded |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_channel**
> delete_notification_channel(id)

Delete a notification channel

Permanently removes a notification channel from the project by UUID. Automations referencing this channel must be updated to prevent dispatch delivery failures.

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
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60002') # UUID | Unique notification channel UUID to delete

    try:
        # Delete a notification channel
        api_instance.delete_notification_channel(id)
    except Exception as e:
        print("Exception when calling AutomationNotificationChannelsApi->delete_notification_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique notification channel UUID to delete | 

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
**204** | Notification channel successfully deleted |  -  |
**401** | Unauthorized |  -  |
**404** | Notification channel not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_channel**
> NotificationChannelResponse get_notification_channel(id)

Get a notification channel by ID

Retrieves configuration details and status of a specific notification channel by its UUID, including channel type, name, creation timestamp, and credential settings for authorized project administrators.

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
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60002') # UUID | Unique notification channel UUID

    try:
        # Get a notification channel by ID
        api_response = api_instance.get_notification_channel(id)
        print("The response of AutomationNotificationChannelsApi->get_notification_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationNotificationChannelsApi->get_notification_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique notification channel UUID | 

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
**200** | Notification channel details |  -  |
**401** | Unauthorized |  -  |
**404** | Notification channel not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notification_channels**
> ListNotificationChannels200Response list_notification_channels()

List notification channels

Retrieves all notification delivery channels configured within the current project. Channels are reusable destination targets for automation alerts, supporting Telegram bots, external HTTP webhooks, and mobile push notifications. Sensitive credentials are sanitized in list outputs.

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
        # List notification channels
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
**200** | List of configured notification channels |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_notification_channel**
> TestNotificationChannel200Response test_notification_channel(id, test_notification_channel_request)

Send a test notification message

Dispatches an immediate test notification message to verify channel credentials, network reachability, and recipient configuration. Accepts channel-specific parameters such as Telegram `chat_id` or push notification `title` and `message`.

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
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60002') # UUID | Unique notification channel UUID to test
    test_notification_channel_request = omnismith_sdk.TestNotificationChannelRequest() # TestNotificationChannelRequest | 

    try:
        # Send a test notification message
        api_response = api_instance.test_notification_channel(id, test_notification_channel_request)
        print("The response of AutomationNotificationChannelsApi->test_notification_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationNotificationChannelsApi->test_notification_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique notification channel UUID to test | 
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
**200** | Test message delivered successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Notification channel not found |  -  |
**422** | Test message delivery failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_channel**
> update_notification_channel(id, update_notification_channel_request)

Update a notification channel

Updates an existing notification channel configuration by UUID. Allows updating the channel display name or updating integration credentials (such as new bot tokens, webhook endpoints, or authentication credentials).

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
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60002') # UUID | Unique notification channel UUID to update
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
 **id** | **UUID**| Unique notification channel UUID to update | 
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
**204** | Notification channel successfully updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Notification channel not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

