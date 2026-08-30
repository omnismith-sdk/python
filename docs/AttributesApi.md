# omnismith_sdk.AttributesApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_attribute**](AttributesApi.md#create_attribute) | **POST** /attributes | Create a new attribute
[**create_attribute_item**](AttributesApi.md#create_attribute_item) | **POST** /attributes/{id}/items | Add a list item to an attribute
[**delete_attribute**](AttributesApi.md#delete_attribute) | **DELETE** /attributes/{id} | Delete an attribute
[**delete_attribute_item**](AttributesApi.md#delete_attribute_item) | **DELETE** /attributes/{id}/items/{itemId} | Remove a list item from an attribute
[**delete_attribute_reference_config**](AttributesApi.md#delete_attribute_reference_config) | **DELETE** /attributes/{id}/reference | Delete reference configuration for an attribute
[**get_attribute**](AttributesApi.md#get_attribute) | **GET** /attributes/{id} | Get an attribute by ID
[**get_attribute_reference_config**](AttributesApi.md#get_attribute_reference_config) | **GET** /attributes/{id}/reference | Get reference configuration for an attribute
[**list_attribute_items**](AttributesApi.md#list_attribute_items) | **GET** /attributes/{id}/items | List items of an attribute
[**list_attributes**](AttributesApi.md#list_attributes) | **GET** /attributes | List all attributes
[**patch_attribute**](AttributesApi.md#patch_attribute) | **PATCH** /attributes/{id} | Patch an attribute (granular partial update)
[**set_attribute_items**](AttributesApi.md#set_attribute_items) | **PUT** /attributes/{id}/items | Set list items for an attribute (replaces all existing items)
[**set_attribute_reference_config**](AttributesApi.md#set_attribute_reference_config) | **PUT** /attributes/{id}/reference | Set or update reference configuration for an attribute
[**update_attribute**](AttributesApi.md#update_attribute) | **PUT** /attributes/{id} | Update an attribute (full replacement)
[**update_attribute_item**](AttributesApi.md#update_attribute_item) | **PUT** /attributes/{id}/items/{itemId} | Update a list item of an attribute


# **create_attribute**
> CreateAttribute201Response create_attribute(create_attribute_request)

Create a new attribute

Defines a new attribute in the project schema. Attributes can be of kind Dimension (0), Metric (1), List (2), or Reference (3). Specify the storage data type (String: 0, Number: 1, Boolean: 2, Datetime: 3, Date: 4, File: 5, Image: 6, Markdown: 7), name, optional project-unique slug (auto-generated from name if omitted), optional template associations, and an optional reference_config if kind is Reference (3). Subject to project tier quota constraints.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_attribute201_response import CreateAttribute201Response
from omnismith_sdk.models.create_attribute_request import CreateAttributeRequest
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
    api_instance = omnismith_sdk.AttributesApi(api_client)
    create_attribute_request = omnismith_sdk.CreateAttributeRequest() # CreateAttributeRequest | 

    try:
        # Create a new attribute
        api_response = api_instance.create_attribute(create_attribute_request)
        print("The response of AttributesApi->create_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributesApi->create_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_attribute_request** | [**CreateAttributeRequest**](CreateAttributeRequest.md)|  | 

### Return type

[**CreateAttribute201Response**](CreateAttribute201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Attribute successfully created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Tier quota exceeded |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_attribute_item**
> CreateAttributeItem201Response create_attribute_item(id, add_list_item_request)

Add a list item to an attribute

Appends a single selectable choice option item to a List-type (attribute_type = 2) attribute. Returns the generated or assigned UUID of the newly created list item.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.add_list_item_request import AddListItemRequest
from omnismith_sdk.models.create_attribute_item201_response import CreateAttributeItem201Response
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
    api_instance = omnismith_sdk.AttributesApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the List-type attribute
    add_list_item_request = omnismith_sdk.AddListItemRequest() # AddListItemRequest | 

    try:
        # Add a list item to an attribute
        api_response = api_instance.create_attribute_item(id, add_list_item_request)
        print("The response of AttributesApi->create_attribute_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributesApi->create_attribute_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| UUID of the List-type attribute | 
 **add_list_item_request** | [**AddListItemRequest**](AddListItemRequest.md)|  | 

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
**201** | List item created successfully |  -  |
**400** | Bad Request - Attribute is not a List type |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attribute**
> delete_attribute(id)

Delete an attribute

Soft-deletes an attribute from the project schema. Soft-deleted attributes are removed from active template projections and future queries, while existing historical dimension and telemetry records remain preserved for audit integrity.

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
    api_instance = omnismith_sdk.AttributesApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the attribute to delete

    try:
        # Delete an attribute
        api_instance.delete_attribute(id)
    except Exception as e:
        print("Exception when calling AttributesApi->delete_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| UUID of the attribute to delete | 

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
**204** | Attribute deleted successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attribute_item**
> delete_attribute_item(id, item_id)

Remove a list item from an attribute

Permanently deletes a specific selectable option item from a List-type (attribute_type = 2) attribute. Validates that the list item exists and belongs to the specified attribute before deletion.

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
    api_instance = omnismith_sdk.AttributesApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the parent List attribute
    item_id = UUID('019a6b2c-8c3a-7c2e-8b3f-6c8a1a2b3c4d') # UUID | UUID of the list item to delete

    try:
        # Remove a list item from an attribute
        api_instance.delete_attribute_item(id, item_id)
    except Exception as e:
        print("Exception when calling AttributesApi->delete_attribute_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| UUID of the parent List attribute | 
 **item_id** | **UUID**| UUID of the list item to delete | 

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
**204** | List item deleted successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found - List item or Attribute not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attribute_reference_config**
> delete_attribute_reference_config(id)

Delete reference configuration for an attribute

Removes the foreign entity reference configuration mapping from a Reference-type (attribute_type = 3) attribute.

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
    api_instance = omnismith_sdk.AttributesApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the Reference attribute

    try:
        # Delete reference configuration for an attribute
        api_instance.delete_attribute_reference_config(id)
    except Exception as e:
        print("Exception when calling AttributesApi->delete_attribute_reference_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| UUID of the Reference attribute | 

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
**204** | Reference configuration deleted successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute**
> AttributeResponse get_attribute(id)

Get an attribute by ID

Retrieves complete attribute metadata by its UUID, including kind (Dimension: 0, Metric: 1, List: 2, Reference: 3), storage data type, assigned template IDs, creation timestamps, and reference configuration if applicable.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.attribute_response import AttributeResponse
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
    api_instance = omnismith_sdk.AttributesApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the attribute to fetch

    try:
        # Get an attribute by ID
        api_response = api_instance.get_attribute(id)
        print("The response of AttributesApi->get_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributesApi->get_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| UUID of the attribute to fetch | 

### Return type

[**AttributeResponse**](AttributeResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attribute details |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_reference_config**
> ReferenceConfigResponse get_attribute_reference_config(id)

Get reference configuration for an attribute

Retrieves the relational reference target configuration for a Reference-type (attribute_type = 3) attribute. Returns the target template UUID and target display attribute UUID used for entity reference pointer resolution.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.reference_config_response import ReferenceConfigResponse
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
    api_instance = omnismith_sdk.AttributesApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the Reference attribute

    try:
        # Get reference configuration for an attribute
        api_response = api_instance.get_attribute_reference_config(id)
        print("The response of AttributesApi->get_attribute_reference_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributesApi->get_attribute_reference_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| UUID of the Reference attribute | 

### Return type

[**ReferenceConfigResponse**](ReferenceConfigResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reference configuration details |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found - Reference configuration not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attribute_items**
> ListAttributeItems200Response list_attribute_items(id)

List items of an attribute

Retrieves all selectable choice option items for a List-type (attribute_type = 2) attribute in ascending sort order. Each item contains its UUID, parent attribute ID, string value, and sort rank.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_attribute_items200_response import ListAttributeItems200Response
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
    api_instance = omnismith_sdk.AttributesApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the List-type attribute

    try:
        # List items of an attribute
        api_response = api_instance.list_attribute_items(id)
        print("The response of AttributesApi->list_attribute_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributesApi->list_attribute_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| UUID of the List-type attribute | 

### Return type

[**ListAttributeItems200Response**](ListAttributeItems200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of option items for the attribute |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attributes**
> ListAttributes200Response list_attributes()

List all attributes

Retrieves all schema attributes defined in the active project. Attributes represent the core schema building blocks across 4 kinds: Dimension (0), Metric (1), List (2), and Reference (3). Each attribute defines its storage data type (String: 0, Number: 1, Boolean: 2, Datetime: 3, Date: 4, File: 5, Image: 6, Markdown: 7), unique slug, optional description, associated templates, and reference configurations.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_attributes200_response import ListAttributes200Response
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
    api_instance = omnismith_sdk.AttributesApi(api_client)

    try:
        # List all attributes
        api_response = api_instance.list_attributes()
        print("The response of AttributesApi->list_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributesApi->list_attributes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListAttributes200Response**](ListAttributes200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all project attributes |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_attribute**
> patch_attribute(id, patch_attribute_request)

Patch an attribute (granular partial update)

Applies partial modifications to an existing attribute without overwriting omitted fields. Allows independently changing name, description, slug, template associations, reference configuration, or transitioning data type. Lossless data type transition rules apply when updating data_type (Dimension only: Number(1)->String(0), Boolean(2)->String(0), Date(4)<->Datetime(3), Date(4)/Datetime(3)->String(0), String(0)<->Markdown(7)). Template associations merge and preserve restricted templates.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.patch_attribute_request import PatchAttributeRequest
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
    api_instance = omnismith_sdk.AttributesApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the attribute to patch
    patch_attribute_request = omnismith_sdk.PatchAttributeRequest() # PatchAttributeRequest | 

    try:
        # Patch an attribute (granular partial update)
        api_instance.patch_attribute(id, patch_attribute_request)
    except Exception as e:
        print("Exception when calling AttributesApi->patch_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| UUID of the attribute to patch | 
 **patch_attribute_request** | [**PatchAttributeRequest**](PatchAttributeRequest.md)|  | 

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
**204** | Attribute patched successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_attribute_items**
> set_attribute_items(id, set_list_items_request)

Set list items for an attribute (replaces all existing items)

Atomically replaces all selectable option items for a List-type (attribute_type = 2) attribute. Existing list items for this attribute are removed and replaced with the provided array of items (with values, sort orders, and optional custom UUIDs). Returns HTTP 400 if the target attribute is not of List kind.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.set_list_items_request import SetListItemsRequest
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
    api_instance = omnismith_sdk.AttributesApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the List-type attribute
    set_list_items_request = omnismith_sdk.SetListItemsRequest() # SetListItemsRequest | 

    try:
        # Set list items for an attribute (replaces all existing items)
        api_instance.set_attribute_items(id, set_list_items_request)
    except Exception as e:
        print("Exception when calling AttributesApi->set_attribute_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| UUID of the List-type attribute | 
 **set_list_items_request** | [**SetListItemsRequest**](SetListItemsRequest.md)|  | 

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
**204** | List items replaced successfully |  -  |
**400** | Bad Request - Attribute is not a List type |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_attribute_reference_config**
> set_attribute_reference_config(id, set_reference_config_request)

Set or update reference configuration for an attribute

Sets or updates the target template and display attribute for a Reference-type (attribute_type = 3) attribute. Enables relational linking and foreign entity display label resolution. Returns HTTP 400 if the target attribute is not of Reference kind.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.set_reference_config_request import SetReferenceConfigRequest
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
    api_instance = omnismith_sdk.AttributesApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the Reference attribute
    set_reference_config_request = omnismith_sdk.SetReferenceConfigRequest() # SetReferenceConfigRequest | 

    try:
        # Set or update reference configuration for an attribute
        api_instance.set_attribute_reference_config(id, set_reference_config_request)
    except Exception as e:
        print("Exception when calling AttributesApi->set_attribute_reference_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| UUID of the Reference attribute | 
 **set_reference_config_request** | [**SetReferenceConfigRequest**](SetReferenceConfigRequest.md)|  | 

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
**204** | Reference configuration updated successfully |  -  |
**400** | Bad Request - Attribute is not a Reference type |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attribute**
> update_attribute(id, update_attribute_request)

Update an attribute (full replacement)

Performs a full update of an existing attribute definition. Supports updating name, description, slug, template associations, reference configuration, and lossless data type transitions. Data type transitions are permitted only for Dimension (0) attributes and must follow lossless compatibility: Number(1) -> String(0), Boolean(2) -> String(0), Date(4) <-> Datetime(3), Date(4)/Datetime(3) -> String(0), and String(0) <-> Markdown(7). Non-lossless transitions or transitions on non-dimension attributes will return HTTP 422. Template associations preserve restricted templates the caller cannot see.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.update_attribute_request import UpdateAttributeRequest
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
    api_instance = omnismith_sdk.AttributesApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the attribute to update
    update_attribute_request = omnismith_sdk.UpdateAttributeRequest() # UpdateAttributeRequest | 

    try:
        # Update an attribute (full replacement)
        api_instance.update_attribute(id, update_attribute_request)
    except Exception as e:
        print("Exception when calling AttributesApi->update_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| UUID of the attribute to update | 
 **update_attribute_request** | [**UpdateAttributeRequest**](UpdateAttributeRequest.md)|  | 

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
**204** | Attribute updated successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attribute_item**
> update_attribute_item(id, item_id, update_list_item_request)

Update a list item of an attribute

Updates the display value and/or sort order of an existing list item belonging to a List-type (attribute_type = 2) attribute. Validates that the list item exists and belongs to the specified attribute.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.update_list_item_request import UpdateListItemRequest
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
    api_instance = omnismith_sdk.AttributesApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the parent List attribute
    item_id = UUID('019a6b2c-8c3a-7c2e-8b3f-6c8a1a2b3c4d') # UUID | UUID of the list item to update
    update_list_item_request = omnismith_sdk.UpdateListItemRequest() # UpdateListItemRequest | 

    try:
        # Update a list item of an attribute
        api_instance.update_attribute_item(id, item_id, update_list_item_request)
    except Exception as e:
        print("Exception when calling AttributesApi->update_attribute_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| UUID of the parent List attribute | 
 **item_id** | **UUID**| UUID of the list item to update | 
 **update_list_item_request** | [**UpdateListItemRequest**](UpdateListItemRequest.md)|  | 

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
**204** | List item updated successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found - List item or Attribute not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

