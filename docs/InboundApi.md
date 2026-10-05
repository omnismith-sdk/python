# omnismith_sdk.InboundApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_inbound_endpoint_secret**](InboundApi.md#add_inbound_endpoint_secret) | **POST** /templates/{templateId}/inbound-endpoints/{id}/secrets | Add a secret to an inbound endpoint (start a rotation)
[**create_template_inbound_endpoint**](InboundApi.md#create_template_inbound_endpoint) | **POST** /templates/{templateId}/inbound-endpoints | Create an inbound endpoint on a template
[**delete_inbound_endpoint_secret**](InboundApi.md#delete_inbound_endpoint_secret) | **DELETE** /templates/{templateId}/inbound-endpoints/{id}/secrets/{secretId} | Remove a secret from an inbound endpoint (finish a rotation)
[**delete_template_inbound_endpoint**](InboundApi.md#delete_template_inbound_endpoint) | **DELETE** /templates/{templateId}/inbound-endpoints/{id} | Delete an inbound endpoint
[**get_inbound_delivery**](InboundApi.md#get_inbound_delivery) | **GET** /templates/{templateId}/inbound-endpoints/{id}/deliveries/{deliveryId} | Get one delivery an inbound endpoint received
[**get_template_inbound_endpoint**](InboundApi.md#get_template_inbound_endpoint) | **GET** /templates/{templateId}/inbound-endpoints/{id} | Get an inbound endpoint
[**list_inbound_deliveries**](InboundApi.md#list_inbound_deliveries) | **GET** /templates/{templateId}/inbound-endpoints/{id}/deliveries | List the deliveries an inbound endpoint received
[**list_template_inbound_endpoints**](InboundApi.md#list_template_inbound_endpoints) | **GET** /templates/{templateId}/inbound-endpoints | List the inbound endpoints of a template
[**preview_inbound_mapping**](InboundApi.md#preview_inbound_mapping) | **POST** /templates/{templateId}/inbound-endpoints/{id}/preview | Preview what an inbound mapping does with a sample payload
[**receive_inbound_delivery**](InboundApi.md#receive_inbound_delivery) | **POST** /inbound/{projectId}/{endpointId} | Receive a delivery from an outside system
[**replay_inbound_delivery**](InboundApi.md#replay_inbound_delivery) | **POST** /templates/{templateId}/inbound-endpoints/{id}/deliveries/{deliveryId}/replay | Replay a stored inbound delivery through the current mapping
[**update_template_inbound_endpoint**](InboundApi.md#update_template_inbound_endpoint) | **PATCH** /templates/{templateId}/inbound-endpoints/{id} | Update an inbound endpoint


# **add_inbound_endpoint_secret**
> InboundSecretRevealed add_inbound_endpoint_secret(template_id, id, x_omnismith_project_id=x_omnismith_project_id, add_inbound_endpoint_secret_request=add_inbound_endpoint_secret_request)

Add a secret to an inbound endpoint (start a rotation)

Adds a second secret. Deliveries signed with either secret are accepted until the old one is removed with `deleteInboundEndpointSecret`. An endpoint holds at most two secrets. The body may be empty to have the secret generated.

The response carries the secret once and never again: give it to whoever configures the sender and do not store it anywhere else. Like updating the endpoint, this requires your own permission to create and edit records of the template.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.add_inbound_endpoint_secret_request import AddInboundEndpointSecretRequest
from omnismith_sdk.models.inbound_secret_revealed import InboundSecretRevealed
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
    api_instance = omnismith_sdk.InboundApi(api_client)
    template_id = 'customer' # str | UUID or slug of the template
    id = UUID('01a0f0e2-7c1a-7000-8000-000000000001') # UUID | Inbound endpoint UUID
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)
    add_inbound_endpoint_secret_request = omnismith_sdk.AddInboundEndpointSecretRequest() # AddInboundEndpointSecretRequest |  (optional)

    try:
        # Add a secret to an inbound endpoint (start a rotation)
        api_response = api_instance.add_inbound_endpoint_secret(template_id, id, x_omnismith_project_id=x_omnismith_project_id, add_inbound_endpoint_secret_request=add_inbound_endpoint_secret_request)
        print("The response of InboundApi->add_inbound_endpoint_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboundApi->add_inbound_endpoint_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| UUID or slug of the template | 
 **id** | **UUID**| Inbound endpoint UUID | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 
 **add_inbound_endpoint_secret_request** | [**AddInboundEndpointSecretRequest**](AddInboundEndpointSecretRequest.md)|  | [optional] 

### Return type

[**InboundSecretRevealed**](InboundSecretRevealed.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The new secret, shown once |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_inbound_endpoint**
> InboundEndpointCreatedResponse create_template_inbound_endpoint(template_id, create_inbound_endpoint_request, x_omnismith_project_id=x_omnismith_project_id)

Create an inbound endpoint on a template

Creates a public URL through which an outside system (Stripe, GitHub, a form tool, a device) writes records into the template without an Omnismith credential. Pick the sender's `signature` preset and describe the `mapping` from the payload to the template's attributes.

The response carries the receive URL to configure in the sender and, once only, the secret the sender signs with. Hand both to the user, once, for pasting into the sender. Do not repeat the secret later and never store it in a record: it is never returned again, and a lost secret is replaced with `addInboundEndpointSecret` (the `add_inbound_endpoint_secret` tool).

To verify the feed: check the mapping on a sample event from the sender's documentation with `previewInboundMapping` (the `preview_inbound_mapping` tool), ask the user to send a test event, then read `listInboundDeliveries` (the `list_inbound_deliveries` tool).

An endpoint lets its sender create and edit the template's records, so creating one also requires your own permission to create and edit records of the template.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_inbound_endpoint_request import CreateInboundEndpointRequest
from omnismith_sdk.models.inbound_endpoint_created_response import InboundEndpointCreatedResponse
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
    api_instance = omnismith_sdk.InboundApi(api_client)
    template_id = 'customer' # str | UUID or slug of the template
    create_inbound_endpoint_request = omnismith_sdk.CreateInboundEndpointRequest() # CreateInboundEndpointRequest | 
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Create an inbound endpoint on a template
        api_response = api_instance.create_template_inbound_endpoint(template_id, create_inbound_endpoint_request, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of InboundApi->create_template_inbound_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboundApi->create_template_inbound_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| UUID or slug of the template | 
 **create_inbound_endpoint_request** | [**CreateInboundEndpointRequest**](CreateInboundEndpointRequest.md)|  | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**InboundEndpointCreatedResponse**](InboundEndpointCreatedResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Endpoint created, with its secret |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inbound_endpoint_secret**
> delete_inbound_endpoint_secret(template_id, id, secret_id, x_omnismith_project_id=x_omnismith_project_id)

Remove a secret from an inbound endpoint (finish a rotation)

Deliveries signed with this secret are rejected from now on. An endpoint keeps at least one secret, so the last one cannot be removed (422).

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
    api_instance = omnismith_sdk.InboundApi(api_client)
    template_id = 'customer' # str | UUID or slug of the template
    id = UUID('01a0f0e2-7c1a-7000-8000-000000000001') # UUID | Inbound endpoint UUID
    secret_id = UUID('01a0f0e2-7c1a-7000-8000-0000000000c1') # UUID | Secret UUID, from the endpoint's `secrets`
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Remove a secret from an inbound endpoint (finish a rotation)
        api_instance.delete_inbound_endpoint_secret(template_id, id, secret_id, x_omnismith_project_id=x_omnismith_project_id)
    except Exception as e:
        print("Exception when calling InboundApi->delete_inbound_endpoint_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| UUID or slug of the template | 
 **id** | **UUID**| Inbound endpoint UUID | 
 **secret_id** | **UUID**| Secret UUID, from the endpoint&#39;s &#x60;secrets&#x60; | 
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
**204** | Secret removed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_inbound_endpoint**
> delete_template_inbound_endpoint(template_id, id, x_omnismith_project_id=x_omnismith_project_id)

Delete an inbound endpoint

Deletes the endpoint. Its URL answers 404 from then on, so the sender's deliveries stop being accepted. Records it wrote are not affected.

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
    api_instance = omnismith_sdk.InboundApi(api_client)
    template_id = 'customer' # str | UUID or slug of the template
    id = UUID('01a0f0e2-7c1a-7000-8000-000000000001') # UUID | Inbound endpoint UUID
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Delete an inbound endpoint
        api_instance.delete_template_inbound_endpoint(template_id, id, x_omnismith_project_id=x_omnismith_project_id)
    except Exception as e:
        print("Exception when calling InboundApi->delete_template_inbound_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| UUID or slug of the template | 
 **id** | **UUID**| Inbound endpoint UUID | 
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
**204** | Endpoint deleted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound_delivery**
> InboundDeliveryDetail get_inbound_delivery(template_id, id, delivery_id, x_omnismith_project_id=x_omnismith_project_id)

Get one delivery an inbound endpoint received

One row of the delivery log with the stored body (at most 256 KB), the allow-listed headers, and `error`: for a rejected or partial delivery, the per-record `items` and field `errors` it was answered with. `deliveryId` is the `log_id` the sender was answered with. The stored body can serve as the sample for `previewInboundMapping` (`delivery_id`).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.inbound_delivery_detail import InboundDeliveryDetail
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
    api_instance = omnismith_sdk.InboundApi(api_client)
    template_id = 'customer' # str | UUID or slug of the template
    id = UUID('01a0f0e2-7c1a-7000-8000-000000000001') # UUID | Inbound endpoint UUID
    delivery_id = UUID('01a0f0e2-7c1a-7000-8000-0000000000d1') # UUID | Delivery log row UUID
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Get one delivery an inbound endpoint received
        api_response = api_instance.get_inbound_delivery(template_id, id, delivery_id, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of InboundApi->get_inbound_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboundApi->get_inbound_delivery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| UUID or slug of the template | 
 **id** | **UUID**| Inbound endpoint UUID | 
 **delivery_id** | **UUID**| Delivery log row UUID | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**InboundDeliveryDetail**](InboundDeliveryDetail.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The delivery |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_inbound_endpoint**
> InboundEndpointResponse get_template_inbound_endpoint(template_id, id, x_omnismith_project_id=x_omnismith_project_id)

Get an inbound endpoint

Returns the endpoint with its receive URL. Secret values are never returned; each secret shows only a hint.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.inbound_endpoint_response import InboundEndpointResponse
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
    api_instance = omnismith_sdk.InboundApi(api_client)
    template_id = 'customer' # str | UUID or slug of the template
    id = UUID('01a0f0e2-7c1a-7000-8000-000000000001') # UUID | Inbound endpoint UUID
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Get an inbound endpoint
        api_response = api_instance.get_template_inbound_endpoint(template_id, id, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of InboundApi->get_template_inbound_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboundApi->get_template_inbound_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| UUID or slug of the template | 
 **id** | **UUID**| Inbound endpoint UUID | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**InboundEndpointResponse**](InboundEndpointResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The endpoint |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inbound_deliveries**
> ListInboundDeliveries200Response list_inbound_deliveries(template_id, id, x_omnismith_project_id=x_omnismith_project_id, outcome=outcome, var_from=var_from, to=to, limit=limit, offset=offset)

List the deliveries an inbound endpoint received

The endpoint's delivery log, newest first: every delivery that passed signature verification, and at most one signature failure per 10 seconds. Rows are kept for 7 days. Bodies are left out; read one delivery for its body and headers.

This is how a feed is verified after a test event. On `rejected` or `partial`, read the delivery with `getInboundDelivery` (the `get_inbound_delivery` tool) for its per-record errors, fix the mapping with `updateTemplateInboundEndpoint` (the `update_template_inbound_endpoint` tool), then recover it with `replayInboundDelivery` (the `replay_inbound_delivery` tool). A `401` row (`reason` `mismatch` or `missing_signature`) usually means the sender is configured with the wrong secret or header.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_inbound_deliveries200_response import ListInboundDeliveries200Response
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
    api_instance = omnismith_sdk.InboundApi(api_client)
    template_id = 'customer' # str | UUID or slug of the template
    id = UUID('01a0f0e2-7c1a-7000-8000-000000000001') # UUID | Inbound endpoint UUID
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)
    outcome = ['[\"rejected\",\"failed\"]'] # List[str] | Only deliveries with one of these outcomes; comma-separated (optional)
    var_from = '2026-10-01T00:00:00Z' # datetime | Only deliveries received at or after this RFC 3339 time (optional)
    to = '2026-10-01T23:59:59Z' # datetime | Only deliveries received at or before this RFC 3339 time (optional)
    limit = 20 # int | Page size (optional) (default to 20)
    offset = 0 # int | Number of deliveries to skip (optional) (default to 0)

    try:
        # List the deliveries an inbound endpoint received
        api_response = api_instance.list_inbound_deliveries(template_id, id, x_omnismith_project_id=x_omnismith_project_id, outcome=outcome, var_from=var_from, to=to, limit=limit, offset=offset)
        print("The response of InboundApi->list_inbound_deliveries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboundApi->list_inbound_deliveries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| UUID or slug of the template | 
 **id** | **UUID**| Inbound endpoint UUID | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 
 **outcome** | [**List[str]**](str.md)| Only deliveries with one of these outcomes; comma-separated | [optional] 
 **var_from** | **datetime**| Only deliveries received at or after this RFC 3339 time | [optional] 
 **to** | **datetime**| Only deliveries received at or before this RFC 3339 time | [optional] 
 **limit** | **int**| Page size | [optional] [default to 20]
 **offset** | **int**| Number of deliveries to skip | [optional] [default to 0]

### Return type

[**ListInboundDeliveries200Response**](ListInboundDeliveries200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of the delivery log |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_template_inbound_endpoints**
> ListTemplateInboundEndpoints200Response list_template_inbound_endpoints(template_id, x_omnismith_project_id=x_omnismith_project_id)

List the inbound endpoints of a template

Returns every inbound endpoint that writes records into the template, in creation order, each with its receive URL, signature, mapping and secret hints. Secret values are never returned. The schema overview (`get_schema_overview`) already lists each template's endpoints in brief.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_template_inbound_endpoints200_response import ListTemplateInboundEndpoints200Response
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
    api_instance = omnismith_sdk.InboundApi(api_client)
    template_id = 'customer' # str | UUID or slug of the template
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # List the inbound endpoints of a template
        api_response = api_instance.list_template_inbound_endpoints(template_id, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of InboundApi->list_template_inbound_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboundApi->list_template_inbound_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| UUID or slug of the template | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**ListTemplateInboundEndpoints200Response**](ListTemplateInboundEndpoints200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbound endpoints of the template |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_inbound_mapping**
> PreviewInboundMapping200Response preview_inbound_mapping(template_id, id, preview_inbound_mapping_request, x_omnismith_project_id=x_omnismith_project_id)

Preview what an inbound mapping does with a sample payload

A dry run: maps a sample payload with the endpoint's mapping, or with an unsaved `mapping` to try, and reports what each record would become. Nothing is written.

Use it before saving a mapping and before asking the sender for a test event: pass the sample event from the sender's documentation as `body`, or a delivery from the endpoint's log as `delivery_id`.

The answer says whether the `match` conditions hold, and per record: the external key, whether it would `create` or `update` a record (and which), the attribute values after list and reference resolution, in the write API's shape, and the error a real delivery would meet: mapping errors, type errors and rule violations, keyed as on receive (`items[i].attributes.<slug>`). A mapping that does not fit the template, or an `items` path that names no list, is answered with 422.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.preview_inbound_mapping200_response import PreviewInboundMapping200Response
from omnismith_sdk.models.preview_inbound_mapping_request import PreviewInboundMappingRequest
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
    api_instance = omnismith_sdk.InboundApi(api_client)
    template_id = 'customer' # str | UUID or slug of the template
    id = UUID('01a0f0e2-7c1a-7000-8000-000000000001') # UUID | Inbound endpoint UUID
    preview_inbound_mapping_request = omnismith_sdk.PreviewInboundMappingRequest() # PreviewInboundMappingRequest | 
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Preview what an inbound mapping does with a sample payload
        api_response = api_instance.preview_inbound_mapping(template_id, id, preview_inbound_mapping_request, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of InboundApi->preview_inbound_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboundApi->preview_inbound_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| UUID or slug of the template | 
 **id** | **UUID**| Inbound endpoint UUID | 
 **preview_inbound_mapping_request** | [**PreviewInboundMappingRequest**](PreviewInboundMappingRequest.md)|  | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**PreviewInboundMapping200Response**](PreviewInboundMapping200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | What the mapping would do |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project selected, or the stored delivery cannot serve as a sample (no stored body, or a truncated one) |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receive_inbound_delivery**
> ReceiveInboundDelivery200Response receive_inbound_delivery(project_id, endpoint_id, request_body)

Receive a delivery from an outside system

The receive URL of an inbound endpoint, called by the sending system rather than by API clients. It takes no Omnismith credential: every delivery must carry a valid signature for the endpoint.

- `200` — `processed`: every record was written. `partial`: some records failed; `errors` and `items` say which, and a replay recovers them. `skipped`: nothing was processed, with `reason` `match` (the mapping's conditions did not hold), `no_items` (the items list was empty) or `duplicate` (the delivery id was already processed).
- `400` — the body is not a JSON object or array.
- `401` — the signature is missing or does not verify; `reason` says why.
- `404` — no enabled endpoint at this URL.
- `422` — no record could be written; `errors` are keyed `items[i].attributes.<slug>`, as the entity write API keys them.
- `409`, `429`, `5xx` — the delivery could not be written right now (a key conflict, a quota or rate limit); retry later.
- `413` — the body is over 1 MB.

Every answer after signature verification carries `log_id`, the delivery's row in the endpoint's delivery log.

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.receive_inbound_delivery200_response import ReceiveInboundDelivery200Response
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
    api_instance = omnismith_sdk.InboundApi(api_client)
    project_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Project UUID
    endpoint_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Inbound endpoint UUID
    request_body = None # Dict[str, object] | The sender's JSON payload, unchanged. At most 1 MB.

    try:
        # Receive a delivery from an outside system
        api_response = api_instance.receive_inbound_delivery(project_id, endpoint_id, request_body)
        print("The response of InboundApi->receive_inbound_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboundApi->receive_inbound_delivery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project UUID | 
 **endpoint_id** | **UUID**| Inbound endpoint UUID | 
 **request_body** | [**Dict[str, object]**](object.md)| The sender&#39;s JSON payload, unchanged. At most 1 MB. | 

### Return type

[**ReceiveInboundDelivery200Response**](ReceiveInboundDelivery200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delivery accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**409** | External key conflict |  -  |
**413** | Body over 1 MB |  -  |
**422** | Validation Error |  -  |
**429** | Quota or rate limit reached; retry later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replay_inbound_delivery**
> InboundDeliverySummary replay_inbound_delivery(template_id, id, delivery_id, x_omnismith_project_id=x_omnismith_project_id)

Replay a stored inbound delivery through the current mapping

Recovers a delivery after the mapping or the template was fixed: re-runs the endpoint's current mapping on the stored body and writes the records, attributed to the endpoint as on receive. The signature is not verified again (only verified deliveries are stored) and the duplicate check is skipped.

Only `rejected`, `failed` and `partial` deliveries are replayed; for a `partial` one, only the records that failed. A processed or skipped delivery, one that failed signature verification (nothing of it was stored), and one whose stored body was truncated are refused with 409.

The replay is a new row in the delivery log, returned here, with `replay_of` naming the replayed delivery and `replayed_by` the user who asked. Its `outcome` says whether the records were written now.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.inbound_delivery_summary import InboundDeliverySummary
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
    api_instance = omnismith_sdk.InboundApi(api_client)
    template_id = 'customer' # str | UUID or slug of the template
    id = UUID('01a0f0e2-7c1a-7000-8000-000000000001') # UUID | Inbound endpoint UUID
    delivery_id = UUID('01a0f0e2-7c1a-7000-8000-0000000000d1') # UUID | The delivery log row to replay
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Replay a stored inbound delivery through the current mapping
        api_response = api_instance.replay_inbound_delivery(template_id, id, delivery_id, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of InboundApi->replay_inbound_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboundApi->replay_inbound_delivery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| UUID or slug of the template | 
 **id** | **UUID**| Inbound endpoint UUID | 
 **delivery_id** | **UUID**| The delivery log row to replay | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**InboundDeliverySummary**](InboundDeliverySummary.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The replay&#39;s own delivery log row |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project selected, or the delivery is not replayable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_inbound_endpoint**
> InboundEndpointResponse update_template_inbound_endpoint(template_id, id, update_inbound_endpoint_request, x_omnismith_project_id=x_omnismith_project_id)

Update an inbound endpoint

Partial update: send only the fields to change. `delivery_id_source: null` removes the delivery id source. Set `enabled: false` to stop accepting deliveries without deleting the endpoint. Secrets are changed with the secrets endpoints, never here.

Try a mapping change first with `previewInboundMapping` (the `preview_inbound_mapping` tool), which takes an unsaved `mapping`. After saving, recover the deliveries the old mapping rejected with `replayInboundDelivery` (the `replay_inbound_delivery` tool).

Like create, this requires your own permission to create and edit records of the template.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.inbound_endpoint_response import InboundEndpointResponse
from omnismith_sdk.models.update_inbound_endpoint_request import UpdateInboundEndpointRequest
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
    api_instance = omnismith_sdk.InboundApi(api_client)
    template_id = 'customer' # str | UUID or slug of the template
    id = UUID('01a0f0e2-7c1a-7000-8000-000000000001') # UUID | Inbound endpoint UUID
    update_inbound_endpoint_request = omnismith_sdk.UpdateInboundEndpointRequest() # UpdateInboundEndpointRequest | 
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Update an inbound endpoint
        api_response = api_instance.update_template_inbound_endpoint(template_id, id, update_inbound_endpoint_request, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of InboundApi->update_template_inbound_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboundApi->update_template_inbound_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| UUID or slug of the template | 
 **id** | **UUID**| Inbound endpoint UUID | 
 **update_inbound_endpoint_request** | [**UpdateInboundEndpointRequest**](UpdateInboundEndpointRequest.md)|  | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**InboundEndpointResponse**](InboundEndpointResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated endpoint |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

