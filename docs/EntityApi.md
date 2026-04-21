# omnismith_sdk.EntityApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity**](EntityApi.md#create_entity) | **POST** /entities | Create a new entity
[**delete_entity**](EntityApi.md#delete_entity) | **DELETE** /entities/{id} | Delete an entity
[**export_entities**](EntityApi.md#export_entities) | **POST** /entities/export/{template_id} | Export entities to CSV
[**get_entity**](EntityApi.md#get_entity) | **GET** /entities/{id} | Get an entity
[**get_entity_chart**](EntityApi.md#get_entity_chart) | **GET** /entities/{id}/chart | Get entity chart time-series data
[**get_entity_history**](EntityApi.md#get_entity_history) | **GET** /entities/{id}/history | Get entity history
[**import_entities**](EntityApi.md#import_entities) | **POST** /entities/import/{template_id} | Import entities from CSV
[**search_entities**](EntityApi.md#search_entities) | **POST** /entities/search/{template_id} | Search entities
[**update_entity**](EntityApi.md#update_entity) | **PUT** /entities/{id} | Update an entity


# **create_entity**
> CreateAttributeItem201Response create_entity(create_entity_request)

Create a new entity

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_attribute_item201_response import CreateAttributeItem201Response
from omnismith_sdk.models.create_entity_request import CreateEntityRequest
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
    api_instance = omnismith_sdk.EntityApi(api_client)
    create_entity_request = omnismith_sdk.CreateEntityRequest() # CreateEntityRequest | 

    try:
        # Create a new entity
        api_response = api_instance.create_entity(create_entity_request)
        print("The response of EntityApi->create_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->create_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_entity_request** | [**CreateEntityRequest**](CreateEntityRequest.md)|  | 

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
**201** | Entity created |  -  |
**401** | Unauthorized |  -  |
**402** | Tier quota exceeded |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity**
> delete_entity(id)

Delete an entity

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
    api_instance = omnismith_sdk.EntityApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete an entity
        api_instance.delete_entity(id)
    except Exception as e:
        print("Exception when calling EntityApi->delete_entity: %s\n" % e)
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
**204** | Entity deleted |  -  |
**404** | Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_entities**
> bytes export_entities(template_id, export_entities_request, sort_field=sort_field, sort_direction=sort_direction)

Export entities to CSV

Export entities matching the given filters to a CSV file. Uses the same filters as the search endpoint.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.export_entities_request import ExportEntitiesRequest
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
    api_instance = omnismith_sdk.EntityApi(api_client)
    template_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Template ID
    export_entities_request = omnismith_sdk.ExportEntitiesRequest() # ExportEntitiesRequest | 
    sort_field = 'sort_field_example' # str | Attribute ID to sort by (UUID) OR one of: id, created_at, updated_at, deleted_at (optional)
    sort_direction = asc # str | Sort direction (only used when sort_field is provided) (optional) (default to asc)

    try:
        # Export entities to CSV
        api_response = api_instance.export_entities(template_id, export_entities_request, sort_field=sort_field, sort_direction=sort_direction)
        print("The response of EntityApi->export_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->export_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **UUID**| Template ID | 
 **export_entities_request** | [**ExportEntitiesRequest**](ExportEntitiesRequest.md)|  | 
 **sort_field** | **str**| Attribute ID to sort by (UUID) OR one of: id, created_at, updated_at, deleted_at | [optional] 
 **sort_direction** | **str**| Sort direction (only used when sort_field is provided) | [optional] [default to asc]

### Return type

**bytes**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/csv, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CSV file download |  * Content-Disposition - Attachment filename <br>  |
**422** | Validation Error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity**
> EntityResponse get_entity(id)

Get an entity

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.entity_response import EntityResponse
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
    api_instance = omnismith_sdk.EntityApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get an entity
        api_response = api_instance.get_entity(id)
        print("The response of EntityApi->get_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->get_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

[**EntityResponse**](EntityResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entity details |  -  |
**404** | Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_chart**
> GetEntityChart200Response get_entity_chart(id, attribute_ids, start, end, aggregate_func=aggregate_func, bucket_width=bucket_width)

Get entity chart time-series data

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.get_entity_chart200_response import GetEntityChart200Response
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
    api_instance = omnismith_sdk.EntityApi(api_client)
    id = 'id_example' # str | Entity ID
    attribute_ids = 'attribute_ids_example' # str | Comma-separated attribute IDs
    start = 56 # int | Start timestamp (Unix seconds)
    end = 56 # int | End timestamp (Unix seconds)
    aggregate_func = avg # str | Aggregate function (optional) (default to avg)
    bucket_width = 1 hour # str | Time bucket width (PostgreSQL interval) (optional) (default to 1 hour)

    try:
        # Get entity chart time-series data
        api_response = api_instance.get_entity_chart(id, attribute_ids, start, end, aggregate_func=aggregate_func, bucket_width=bucket_width)
        print("The response of EntityApi->get_entity_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->get_entity_chart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entity ID | 
 **attribute_ids** | **str**| Comma-separated attribute IDs | 
 **start** | **int**| Start timestamp (Unix seconds) | 
 **end** | **int**| End timestamp (Unix seconds) | 
 **aggregate_func** | **str**| Aggregate function | [optional] [default to avg]
 **bucket_width** | **str**| Time bucket width (PostgreSQL interval) | [optional] [default to 1 hour]

### Return type

[**GetEntityChart200Response**](GetEntityChart200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chart time-series data grouped by attribute |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_history**
> GetEntityHistory200Response get_entity_history(id, page=page, limit=limit, sort_by=sort_by, sort_direction=sort_direction, search=search, attribute_ids=attribute_ids, start=start, end=end, author_email=author_email)

Get entity history

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.get_entity_history200_response import GetEntityHistory200Response
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
    api_instance = omnismith_sdk.EntityApi(api_client)
    id = 'id_example' # str | Entity ID
    page = 1 # int |  (optional) (default to 1)
    limit = 20 # int |  (optional) (default to 20)
    sort_by = created_at # str |  (optional) (default to created_at)
    sort_direction = desc # str |  (optional) (default to desc)
    search = 'search_example' # str |  (optional)
    attribute_ids = 'attribute_ids_example' # str |  (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime | Filter logs created after this timestamp (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime | Filter logs created before this timestamp (optional)
    author_email = 'author_email_example' # str | Filter logs by author email (optional)

    try:
        # Get entity history
        api_response = api_instance.get_entity_history(id, page=page, limit=limit, sort_by=sort_by, sort_direction=sort_direction, search=search, attribute_ids=attribute_ids, start=start, end=end, author_email=author_email)
        print("The response of EntityApi->get_entity_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->get_entity_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Entity ID | 
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 20]
 **sort_by** | **str**|  | [optional] [default to created_at]
 **sort_direction** | **str**|  | [optional] [default to desc]
 **search** | **str**|  | [optional] 
 **attribute_ids** | **str**|  | [optional] 
 **start** | **datetime**| Filter logs created after this timestamp | [optional] 
 **end** | **datetime**| Filter logs created before this timestamp | [optional] 
 **author_email** | **str**| Filter logs by author email | [optional] 

### Return type

[**GetEntityHistory200Response**](GetEntityHistory200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entity history |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_entities**
> ImportEntities200Response import_entities(template_id, file)

Import entities from CSV

Import entities from a CSV file. Supports upsert: creates new entities or updates existing ones based on the ID column. The CSV must include a metadata row (row 2) with attribute IDs prefixed by #.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.import_entities200_response import ImportEntities200Response
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
    api_instance = omnismith_sdk.EntityApi(api_client)
    template_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Template ID
    file = None # bytes | CSV file exported from the export endpoint or matching its format

    try:
        # Import entities from CSV
        api_response = api_instance.import_entities(template_id, file)
        print("The response of EntityApi->import_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->import_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **UUID**| Template ID | 
 **file** | **bytes**| CSV file exported from the export endpoint or matching its format | 

### Return type

[**ImportEntities200Response**](ImportEntities200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Import completed |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_entities**
> SearchEntities200Response search_entities(template_id, search_entities_request, limit=limit, offset=offset, sort_field=sort_field, sort_direction=sort_direction)

Search entities

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.search_entities200_response import SearchEntities200Response
from omnismith_sdk.models.search_entities_request import SearchEntitiesRequest
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
    api_instance = omnismith_sdk.EntityApi(api_client)
    template_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Template ID
    search_entities_request = omnismith_sdk.SearchEntitiesRequest() # SearchEntitiesRequest | 
    limit = 50 # int | Number of results (optional) (default to 50)
    offset = 0 # int | Pagination offset (optional) (default to 0)
    sort_field = 'sort_field_example' # str | Attribute ID to sort by (UUID) OR one of: id, created_at, updated_at, deleted_at (optional)
    sort_direction = asc # str | Sort direction (only used when sort_field is provided) (optional) (default to asc)

    try:
        # Search entities
        api_response = api_instance.search_entities(template_id, search_entities_request, limit=limit, offset=offset, sort_field=sort_field, sort_direction=sort_direction)
        print("The response of EntityApi->search_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->search_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **UUID**| Template ID | 
 **search_entities_request** | [**SearchEntitiesRequest**](SearchEntitiesRequest.md)|  | 
 **limit** | **int**| Number of results | [optional] [default to 50]
 **offset** | **int**| Pagination offset | [optional] [default to 0]
 **sort_field** | **str**| Attribute ID to sort by (UUID) OR one of: id, created_at, updated_at, deleted_at | [optional] 
 **sort_direction** | **str**| Sort direction (only used when sort_field is provided) | [optional] [default to asc]

### Return type

[**SearchEntities200Response**](SearchEntities200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search results |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity**
> update_entity(id, update_entity_request)

Update an entity

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.update_entity_request import UpdateEntityRequest
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
    api_instance = omnismith_sdk.EntityApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    update_entity_request = omnismith_sdk.UpdateEntityRequest() # UpdateEntityRequest | 

    try:
        # Update an entity
        api_instance.update_entity(id, update_entity_request)
    except Exception as e:
        print("Exception when calling EntityApi->update_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **update_entity_request** | [**UpdateEntityRequest**](UpdateEntityRequest.md)|  | 

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
**204** | Entity updated |  -  |
**402** | Tier quota exceeded |  -  |
**422** | Validation Error |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

