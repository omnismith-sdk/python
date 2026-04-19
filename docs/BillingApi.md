# omnismith_sdk.BillingApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_checkout**](BillingApi.md#create_checkout) | **POST** /billing/checkout | Create a checkout session for subscription
[**get_all_tiers**](BillingApi.md#get_all_tiers) | **GET** /billing/tiers | List all available tiers
[**get_portal_url**](BillingApi.md#get_portal_url) | **GET** /billing/portal | Get customer portal URL
[**get_usage_insights**](BillingApi.md#get_usage_insights) | **GET** /billing/usage/insights | Get current tier usage insights
[**get_user_tier**](BillingApi.md#get_user_tier) | **GET** /billing/tier | Get current user tier
[**log_ai_usage**](BillingApi.md#log_ai_usage) | **POST** /billing/log-usage | Log AI usage credits


# **create_checkout**
> CheckoutResponse create_checkout(create_checkout_request)

Create a checkout session for subscription

Creates a LemonSqueezy checkout session to subscribe to a paid tier. Returns a URL to redirect the user to complete payment.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.checkout_response import CheckoutResponse
from omnismith_sdk.models.create_checkout_request import CreateCheckoutRequest
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
    api_instance = omnismith_sdk.BillingApi(api_client)
    create_checkout_request = omnismith_sdk.CreateCheckoutRequest() # CreateCheckoutRequest | 

    try:
        # Create a checkout session for subscription
        api_response = api_instance.create_checkout(create_checkout_request)
        print("The response of BillingApi->create_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->create_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_checkout_request** | [**CreateCheckoutRequest**](CreateCheckoutRequest.md)|  | 

### Return type

[**CheckoutResponse**](CheckoutResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Checkout session created successfully |  -  |
**400** | Invalid tier level (e.g., Free tier) |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_tiers**
> GetAllTiers200Response get_all_tiers()

List all available tiers

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.get_all_tiers200_response import GetAllTiers200Response
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
    api_instance = omnismith_sdk.BillingApi(api_client)

    try:
        # List all available tiers
        api_response = api_instance.get_all_tiers()
        print("The response of BillingApi->get_all_tiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_all_tiers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAllTiers200Response**](GetAllTiers200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all tiers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portal_url**
> PortalUrlResponse get_portal_url()

Get customer portal URL

Returns a LemonSqueezy customer portal URL where users can manage their subscription (cancel, update payment method, view invoices).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.portal_url_response import PortalUrlResponse
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
    api_instance = omnismith_sdk.BillingApi(api_client)

    try:
        # Get customer portal URL
        api_response = api_instance.get_portal_url()
        print("The response of BillingApi->get_portal_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_portal_url: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PortalUrlResponse**](PortalUrlResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Portal URL retrieved successfully |  -  |
**401** | Unauthorized |  -  |
**404** | No active subscription found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_insights**
> UsageInsightsResponse get_usage_insights()

Get current tier usage insights

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.usage_insights_response import UsageInsightsResponse
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
    api_instance = omnismith_sdk.BillingApi(api_client)

    try:
        # Get current tier usage insights
        api_response = api_instance.get_usage_insights()
        print("The response of BillingApi->get_usage_insights:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_usage_insights: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UsageInsightsResponse**](UsageInsightsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tier usage insights with limits and percentages |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_tier**
> TierResponse get_user_tier()

Get current user tier

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.tier_response import TierResponse
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
    api_instance = omnismith_sdk.BillingApi(api_client)

    try:
        # Get current user tier
        api_response = api_instance.get_user_tier()
        print("The response of BillingApi->get_user_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_user_tier: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TierResponse**](TierResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User tier details |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_ai_usage**
> LogAiUsage200Response log_ai_usage(log_ai_usage_request)

Log AI usage credits

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.log_ai_usage200_response import LogAiUsage200Response
from omnismith_sdk.models.log_ai_usage_request import LogAiUsageRequest
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
    api_instance = omnismith_sdk.BillingApi(api_client)
    log_ai_usage_request = omnismith_sdk.LogAiUsageRequest() # LogAiUsageRequest | 

    try:
        # Log AI usage credits
        api_response = api_instance.log_ai_usage(log_ai_usage_request)
        print("The response of BillingApi->log_ai_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->log_ai_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_ai_usage_request** | [**LogAiUsageRequest**](LogAiUsageRequest.md)|  | 

### Return type

[**LogAiUsage200Response**](LogAiUsage200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage logged successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

