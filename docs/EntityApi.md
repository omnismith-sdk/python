# omnismith_sdk.EntityApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity**](EntityApi.md#create_entity) | **POST** /entities | Create a new dynamic entity
[**delete_entity**](EntityApi.md#delete_entity) | **DELETE** /entities/{id} | Soft-delete an entity record
[**export_entities**](EntityApi.md#export_entities) | **POST** /entities/export/{template_id} | Export entities to structured CSV file
[**get_entity**](EntityApi.md#get_entity) | **GET** /entities/{id} | Get an entity record by ID
[**get_entity_chart**](EntityApi.md#get_entity_chart) | **GET** /entities/{id}/chart | Get entity chart time-series data
[**get_entity_history**](EntityApi.md#get_entity_history) | **GET** /entities/{id}/history | Get entity dimension change history
[**import_entities**](EntityApi.md#import_entities) | **POST** /entities/import/{template_id} | Import entities from structured CSV file
[**ingest_entity_metrics**](EntityApi.md#ingest_entity_metrics) | **POST** /entities/{id}/metrics | Ingest high-frequency metric observations for an entity
[**search_entities**](EntityApi.md#search_entities) | **POST** /entities/search/{template_id} | Search entities with filtering, sorting, and pagination
[**semantic_search_entities**](EntityApi.md#semantic_search_entities) | **POST** /entities/semantic-search | Perform semantic vector similarity search on entities
[**update_entity**](EntityApi.md#update_entity) | **PATCH** /entities/{id} | Update entity attribute values


# **create_entity**
> CreateEntity201Response create_entity(create_entity_request)

Create a new dynamic entity

Creates a new dynamic entity record conforming to a template schema.

### Template Association
Specify the target schema via either `template_id` (UUID) or `template_slug` (human-readable slug).

### Dynamic Attribute Values (`attribute_values`)
Each attribute entry supports identifier resolution and accepts either:
- `attribute_id`: Canonical attribute UUID
- `attribute_slug`: Attribute slug identifier (e.g. `price`, `sku`, `status`)

### Value Formatting Rules
- **Dimension - Text / Markdown**: UTF-8 string value (e.g., `"Wireless Headphones"`)
- **Dimension - Number**: Numeric string representation (e.g., `"129.99"`, `"42"`)
- **Dimension - Boolean**: Strict boolean representation: `"true"`, `"false"`, `"1"`, or `"0"`
- **Dimension - Date & Datetime**: Formatted as `YYYY-MM-DD` (date) or `YYYY-MM-DD HH:MM:SS` / ISO 8601 `YYYY-MM-DDTHH:MM:SSZ` (datetime)
- **Dimension - File & Image**: UUID string of a pre-uploaded workspace file asset
- **List Attribute**: Must provide the exact UUID string of a valid defined `ListItem` option
- **Reference Attribute**: Must provide the exact UUID string of an existing referenced `Entity`

### Metric Telemetry Persistence
Any metric attributes included in `attribute_values` are published directly to the metric ingestion pipeline and recorded in time-series telemetry storage.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_entity201_response import CreateEntity201Response
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
        # Create a new dynamic entity
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

[**CreateEntity201Response**](CreateEntity201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Entity created successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Tier quota exceeded |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity**
> delete_entity(id)

Soft-delete an entity record

Marks an entity record as soft-deleted by setting its `deleted_at` timestamp.

Soft-deleted entities are immediately excluded from standard entity searches, BI row queries, and direct retrieval endpoints. Associated historical change logs and time-series telemetry remain preserved for audit compliance.

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
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | Unique entity identifier (UUID) to soft-delete

    try:
        # Soft-delete an entity record
        api_instance.delete_entity(id)
    except Exception as e:
        print("Exception when calling EntityApi->delete_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique entity identifier (UUID) to soft-delete | 

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
**204** | Entity soft-deleted successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_entities**
> bytes export_entities(template_id, export_entities_request, sort_field=sort_field, sort_direction=sort_direction)

Export entities to structured CSV file

Exports entity records of a template schema matching filter criteria as a streaming CSV download.

### Re-importable CSV Schema Format
The generated CSV conforms to the Omnismith two-row metadata specification, making it directly compatible with `POST /entities/import/{template_id}`:
- **Row 1**: Display column names and attribute aliases.
- **Row 2**: Metadata row prefixed with `#` containing attribute UUIDs and column IDs (e.g. `#id`, `#018b2f1b-8c1a...`).
- **Row 3+**: Entity data records.

### Filter & Search Model
Accepts the same filtering payload as `SearchEntities`: structured `filters` (supporting `eq`, `neq`, `gt`, `lt`, `like`, `not-like`, `empty`, `not-empty`) and `global_search` text queries.

### Sorting
Sort results via `sort_field` (attribute UUID, slug, or standard timestamp) and `sort_direction` (`asc`/`desc`).

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
    template_id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010001') # UUID | Unique identifier (UUID) of the template schema to export
    export_entities_request = omnismith_sdk.ExportEntitiesRequest() # ExportEntitiesRequest | 
    sort_field = 'created_at' # str | Attribute UUID, attribute slug, or standard field (id, created_at, updated_at, deleted_at) to sort by (optional)
    sort_direction = asc # str | Sort direction: \"asc\" (ascending) or \"desc\" (descending) (optional) (default to asc)

    try:
        # Export entities to structured CSV file
        api_response = api_instance.export_entities(template_id, export_entities_request, sort_field=sort_field, sort_direction=sort_direction)
        print("The response of EntityApi->export_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->export_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **UUID**| Unique identifier (UUID) of the template schema to export | 
 **export_entities_request** | [**ExportEntitiesRequest**](ExportEntitiesRequest.md)|  | 
 **sort_field** | **str**| Attribute UUID, attribute slug, or standard field (id, created_at, updated_at, deleted_at) to sort by | [optional] 
 **sort_direction** | **str**| Sort direction: \&quot;asc\&quot; (ascending) or \&quot;desc\&quot; (descending) | [optional] [default to asc]

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
**200** | CSV file download stream |  * Content-Disposition - Attachment header with dynamic filename <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity**
> EntityResponse get_entity(id, attribute_key=attribute_key)

Get an entity record by ID

Retrieves the full hydrated record for a dynamic entity by its unique identifier (UUID).

### Attribute Key Formatting (`attribute_key`)
The `attribute_key` query parameter controls the dictionary keys in `attribute_values`:
- `"id"` (default): Keys are canonical attribute UUIDs (e.g. `018b2f1b-8c1a...`).
- `"slug"`: Keys are human-readable attribute slugs (e.g. `price`, `sku`, `category`), which is recommended for API consumers and AI agent workflows.

### Hydrated Attribute Values
The returned `attribute_values` object includes both raw serialized values and resolved display labels (`custom_value`) for references and list options.

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
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | Unique entity identifier (UUID)
    attribute_key = id # str | Format for attribute_values dictionary keys: \"id\" for attribute UUIDs or \"slug\" for human-readable attribute slugs (optional) (default to id)

    try:
        # Get an entity record by ID
        api_response = api_instance.get_entity(id, attribute_key=attribute_key)
        print("The response of EntityApi->get_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->get_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique entity identifier (UUID) | 
 **attribute_key** | **str**| Format for attribute_values dictionary keys: \&quot;id\&quot; for attribute UUIDs or \&quot;slug\&quot; for human-readable attribute slugs | [optional] [default to id]

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
**200** | Hydrated entity details |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_chart**
> GetEntityChart200Response get_entity_chart(id, attribute_ids, start, end, aggregate_func=aggregate_func, bucket_width=bucket_width)

Get entity chart time-series data

Retrieves aggregated, time-bucketed metric time-series data for an entity.

### Metric Attribute Filtering (`attribute_ids`)
Pass one or more comma-separated metric attribute UUIDs to aggregate across the query window.

### Aggregation Functions (`aggregate_func`)
Supported aggregation operations within each bucket:
- `avg` (default): Arithmetic mean of values
- `sum`: Sum total of values
- `min` / `max`: Minimum / Maximum observed value
- `count`: Number of recorded observations
- `first` / `last`: Earliest / Latest observation within the time bucket

### Time Intervals & Bucket Widths (`bucket_width`)
Values follow standard time interval notation: `1 second`, `5 seconds`, `10 seconds`, `1 minute` (1m), `5 minutes` (5m), `10 minutes`, `15 minutes`, `30 minutes`, `1 hour` (1h), `6 hours`, `12 hours`, `1 day` (1d), `1 week`, `1 month`.

### Query Window (`start` & `end`)
Query range is defined by `start` and `end` timestamps supplied as integer Unix epoch seconds.

### Example

* Bearer (JWT) Authentication (bearerAuth):

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
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | Unique entity identifier (UUID)
    attribute_ids = '018b2f1b-8c1a-75b3-8000-7f0000010010,018b2f1b-8c1a-75b3-8000-7f0000010011' # str | Comma-separated metric attribute UUIDs to aggregate
    start = 1774396800 # int | Start timestamp as Unix epoch in seconds
    end = 1774483200 # int | End timestamp as Unix epoch in seconds
    aggregate_func = avg # str | Aggregation function applied within each bucket (optional) (default to avg)
    bucket_width = 1 hour # str | Time bucket width interval (e.g. 1 minute, 5 minutes, 1 hour, 1 day) (optional) (default to 1 hour)

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
 **id** | **UUID**| Unique entity identifier (UUID) | 
 **attribute_ids** | **str**| Comma-separated metric attribute UUIDs to aggregate | 
 **start** | **int**| Start timestamp as Unix epoch in seconds | 
 **end** | **int**| End timestamp as Unix epoch in seconds | 
 **aggregate_func** | **str**| Aggregation function applied within each bucket | [optional] [default to avg]
 **bucket_width** | **str**| Time bucket width interval (e.g. 1 minute, 5 minutes, 1 hour, 1 day) | [optional] [default to 1 hour]

### Return type

[**GetEntityChart200Response**](GetEntityChart200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chart time-series data grouped by attribute |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_history**
> GetEntityHistory200Response get_entity_history(id, page=page, limit=limit, sort_by=sort_by, sort_direction=sort_direction, search=search, attribute_ids=attribute_ids, start=start, end=end, author_email=author_email)

Get entity dimension change history

Retrieves the immutable change audit log for an entity's dimension attribute mutations.

### Dedicated Dimension Audit Log
Records all historical mutations to dimension, list, and reference attribute values. High-volume metric telemetry observations bypass this log and are stored in dedicated time-series storage, keeping the audit log clean and performant.

### Filtering & Search
- `attribute_ids`: Filter by one or more comma-separated attribute UUIDs.
- `search`: Text search matching historical serialized values.
- `start` and `end`: Filter history records within a timestamp window (ISO 8601 or `YYYY-MM-DD HH:MM:SS`).
- `author_email`: Filter by the actor who performed the mutation.

### Pagination & Sorting
Supports 1-indexed pagination (`page`, `limit` up to 100) and sorting by `created_at`, `attribute_id`, or `value` (`asc`/`desc`).

### Example

* Bearer (JWT) Authentication (bearerAuth):

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
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | Unique entity identifier (UUID)
    page = 1 # int | 1-based page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of history records per page (1-100) (optional) (default to 20)
    sort_by = created_at # str | Field to sort change logs by (optional) (default to created_at)
    sort_direction = desc # str | Sort direction: \"asc\" (ascending) or \"desc\" (descending) (optional) (default to desc)
    search = 'Electronics' # str | Free-text search filter matching against old and new attribute values (optional)
    attribute_ids = '018b2f1b-8c1a-75b3-8000-7f0000010002,018b2f1b-8c1a-75b3-8000-7f0000010003' # str | Comma-separated attribute UUIDs to filter change history (optional)
    start = '2026-08-01T00:00:00Z' # datetime | Filter change records occurring on or after this timestamp (ISO 8601 or YYYY-MM-DD HH:MM:SS format) (optional)
    end = '2026-08-26T23:59:59Z' # datetime | Filter change records occurring on or before this timestamp (ISO 8601 or YYYY-MM-DD HH:MM:SS format) (optional)
    author_email = 'demo@omnismith.io' # str | Filter change records by author or actor email (optional)

    try:
        # Get entity dimension change history
        api_response = api_instance.get_entity_history(id, page=page, limit=limit, sort_by=sort_by, sort_direction=sort_direction, search=search, attribute_ids=attribute_ids, start=start, end=end, author_email=author_email)
        print("The response of EntityApi->get_entity_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->get_entity_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique entity identifier (UUID) | 
 **page** | **int**| 1-based page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of history records per page (1-100) | [optional] [default to 20]
 **sort_by** | **str**| Field to sort change logs by | [optional] [default to created_at]
 **sort_direction** | **str**| Sort direction: \&quot;asc\&quot; (ascending) or \&quot;desc\&quot; (descending) | [optional] [default to desc]
 **search** | **str**| Free-text search filter matching against old and new attribute values | [optional] 
 **attribute_ids** | **str**| Comma-separated attribute UUIDs to filter change history | [optional] 
 **start** | **datetime**| Filter change records occurring on or after this timestamp (ISO 8601 or YYYY-MM-DD HH:MM:SS format) | [optional] 
 **end** | **datetime**| Filter change records occurring on or before this timestamp (ISO 8601 or YYYY-MM-DD HH:MM:SS format) | [optional] 
 **author_email** | **str**| Filter change records by author or actor email | [optional] 

### Return type

[**GetEntityHistory200Response**](GetEntityHistory200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated entity dimension change history |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_entities**
> ImportEntities200Response import_entities(template_id, file)

Import entities from structured CSV file

Bulk imports entity records into a template schema from a structured CSV file.

### Upsert Semantics
- **Update existing**: If a data row includes an `id` matching an existing entity UUID, that entity is updated.
- **Create new**: If the `id` column is empty, omitted, or contains a new UUID, a new entity record is created.

### Required 2-Row CSV Header Format
The CSV file must follow the Omnismith two-row header format (identical to the output of `POST /entities/export/{template_id}`):
- **Row 1 (Display Header)**: Human-readable attribute names or aliases (e.g. `ID`, `SKU`, `Price`, `Category`).
- **Row 2 (Metadata Marker)**: Canonical attribute identifiers prefixed by `#` (e.g. `#id`, `#018b2f1b-8c1a...`, `#018b2f1b-8c1b...`).
- **Row 3+ (Data Rows)**: Serialized entity values conforming to the template's attribute data types.

### Attribute Value Validation
- List attributes require valid `ListItem` option UUIDs.
- Reference attributes require existing target `Entity` UUIDs.
- Number/Date/Boolean fields must match required format syntax.

### Execution Summary
Returns an execution report detailing counts of created, updated, skipped, and failed rows, along with granular row/column error messages.

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
    template_id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010001') # UUID | Unique identifier (UUID) of the template schema to import entities into
    file = None # bytes | CSV file exported from the export endpoint or matching its format

    try:
        # Import entities from structured CSV file
        api_response = api_instance.import_entities(template_id, file)
        print("The response of EntityApi->import_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->import_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **UUID**| Unique identifier (UUID) of the template schema to import entities into | 
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

# **ingest_entity_metrics**
> ingest_entity_metrics(id, ingest_metrics_request)

Ingest high-frequency metric observations for an entity

Ingests time-series metric observations for an entity record.

### Batch Telemetry Ingestion
Accepts a batch array of metric observations (`metric_values`). Each observation targets a metric attribute by `attribute_id` (UUID) or `attribute_slug` and specifies a numeric `value`.

### High-Throughput Streaming Architecture
Metric ingestion calls stream directly into the high-throughput telemetry ingestion pipeline. Asynchronous background consumers persist data points into tenant-scoped time-series storage configured with automated retention and continuous aggregation rollups.

### Strict Metric Attribute Constraint
Only attributes defined with `attribute_type: Metric` are accepted by this endpoint. Mutations to dimension, list, or reference attributes must use `PATCH /entities/{id}` instead.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.ingest_metrics_request import IngestMetricsRequest
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
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | Unique entity identifier (UUID)
    ingest_metrics_request = omnismith_sdk.IngestMetricsRequest() # IngestMetricsRequest | 

    try:
        # Ingest high-frequency metric observations for an entity
        api_instance.ingest_entity_metrics(id, ingest_metrics_request)
    except Exception as e:
        print("Exception when calling EntityApi->ingest_entity_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique entity identifier (UUID) | 
 **ingest_metrics_request** | [**IngestMetricsRequest**](IngestMetricsRequest.md)|  | 

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
**202** | Metrics accepted for ingestion and time-series persistence |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_entities**
> SearchEntities200Response search_entities(template_id, search_entities_request, limit=limit, offset=offset, sort_field=sort_field, sort_direction=sort_direction, attribute_key=attribute_key)

Search entities with filtering, sorting, and pagination

Executes structured queries, full-text searches, and sorting across dynamic entities of a specified template schema.

### Template Targeting (`template_id`)
Accepts either a canonical template UUID (e.g. `018b2f1b-8c1a...`) or a human-readable template slug (e.g. `product_catalog`).

### Structured Filters (`filters`)
Filter conditions are specified in the request body as an array of filter objects:
```json
[
  {"field": "status", "operator": "eq", "value": "018b2f1b-8c1a-75b3-8000-7f0000010020"},
  {"field": "price", "operator": "gt", "value": "100"},
  {"field": "name", "operator": "like", "value": "Pro"}
]
```
- **`field`**: Target attribute UUID, attribute slug, or standard field (`id`, `created_at`, `updated_at`).
- **`operator`**: Comparison operator: `eq` (equals), `neq` (not equals), `gt` (greater than), `lt` (less than), `like` (substring / trigram match), `not-like` (does not match), `empty` (is null or empty), `not-empty` (has value).
- **`value`**: Target comparison value serialized as string.

### Global Search (`global_search`)
Performs accelerated full-text and GIN trigram matching across all string dimension attributes defined on the template.

### Sorting & Pagination
- **`sort_field`**: Attribute UUID, attribute slug, or standard entity fields (`id`, `created_at`, `updated_at`, `deleted_at`).
- **`sort_direction`**: `asc` or `desc` (default: `asc` when `sort_field` is set, otherwise default sort is `created_at` DESC).
- **`limit`** and **`offset`**: Bounded pagination (max 100 per page).

### Attribute Key Formatting (`attribute_key`)
Passing `attribute_key="slug"` formats the returned `attribute_values` dictionary keys using human-readable attribute slugs instead of raw UUIDs.

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
    template_id = 'product_catalog' # str | Template UUID or human-readable template slug
    search_entities_request = omnismith_sdk.SearchEntitiesRequest() # SearchEntitiesRequest | 
    limit = 50 # int | Maximum number of entity records to return (1-100) (optional) (default to 50)
    offset = 0 # int | Zero-based pagination offset (optional) (default to 0)
    sort_field = 'created_at' # str | Attribute UUID, attribute slug, or standard field (id, created_at, updated_at, deleted_at) to sort by (optional)
    sort_direction = asc # str | Sort direction: \"asc\" (ascending) or \"desc\" (descending) (optional) (default to asc)
    attribute_key = id # str | Format for attribute_values dictionary keys: \"id\" for attribute UUIDs or \"slug\" for human-readable attribute slugs (optional) (default to id)

    try:
        # Search entities with filtering, sorting, and pagination
        api_response = api_instance.search_entities(template_id, search_entities_request, limit=limit, offset=offset, sort_field=sort_field, sort_direction=sort_direction, attribute_key=attribute_key)
        print("The response of EntityApi->search_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->search_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template UUID or human-readable template slug | 
 **search_entities_request** | [**SearchEntitiesRequest**](SearchEntitiesRequest.md)|  | 
 **limit** | **int**| Maximum number of entity records to return (1-100) | [optional] [default to 50]
 **offset** | **int**| Zero-based pagination offset | [optional] [default to 0]
 **sort_field** | **str**| Attribute UUID, attribute slug, or standard field (id, created_at, updated_at, deleted_at) to sort by | [optional] 
 **sort_direction** | **str**| Sort direction: \&quot;asc\&quot; (ascending) or \&quot;desc\&quot; (descending) | [optional] [default to asc]
 **attribute_key** | **str**| Format for attribute_values dictionary keys: \&quot;id\&quot; for attribute UUIDs or \&quot;slug\&quot; for human-readable attribute slugs | [optional] [default to id]

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
**200** | Search results matching criteria |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **semantic_search_entities**
> List[SemanticSearchResultItem] semantic_search_entities(semantic_search_entities_request)

Perform semantic vector similarity search on entities

Executes an approximate nearest neighbors (ANN) vector similarity search across entity dimension embeddings.

### 768-Dimensional Embedding Vectors
Requires a 768-dimensional float embedding array (`query_vector`) representing the query text or multimodal vector (e.g. generated by Google `text-embedding-004` or similar models).

### Scoping & Filtering (`template_id`)
Pass an optional `template_id` (UUID) or template slug to constrain the semantic search to records belonging to a specific template schema.

### Cosine Similarity Threshold & Ranking (`threshold`)
- `threshold`: Minimum cosine similarity score threshold (range `0.0` to `1.0`, default `0.5`). Observations below this similarity cutoff are discarded.
- Matches are returned strictly ranked in descending order of `similarity_score`.

### Attribute Key Formatting (`attribute_key`)
Set `attribute_key="slug"` to format the nested entity `attribute_values` dictionary keys as human-readable slugs instead of raw attribute UUIDs.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.semantic_search_entities_request import SemanticSearchEntitiesRequest
from omnismith_sdk.models.semantic_search_result_item import SemanticSearchResultItem
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
    semantic_search_entities_request = omnismith_sdk.SemanticSearchEntitiesRequest() # SemanticSearchEntitiesRequest | 

    try:
        # Perform semantic vector similarity search on entities
        api_response = api_instance.semantic_search_entities(semantic_search_entities_request)
        print("The response of EntityApi->semantic_search_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->semantic_search_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **semantic_search_entities_request** | [**SemanticSearchEntitiesRequest**](SemanticSearchEntitiesRequest.md)|  | 

### Return type

[**List[SemanticSearchResultItem]**](SemanticSearchResultItem.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Matching entities ranked by semantic similarity score |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity**
> update_entity(id, update_entity_request)

Update entity attribute values

Updates specific dynamic attribute values for an existing entity record.

### Dynamic Attribute Values (`attribute_values`)
Submit one or more attribute value updates. Each entry supports identifier resolution via:
- `attribute_id`: Canonical attribute UUID
- `attribute_slug`: Attribute slug identifier (e.g. `price`, `sku`, `status`)

### Value Formatting Rules
- **Dimension - Text / Markdown**: UTF-8 string value
- **Dimension - Number**: Numeric string representation (e.g. `"149.99"`)
- **Dimension - Boolean**: Boolean representation: `"true"`, `"false"`, `"1"`, or `"0"`
- **Dimension - Date & Datetime**: Formatted as `YYYY-MM-DD` or `YYYY-MM-DD HH:MM:SS` / ISO 8601 `YYYY-MM-DDTHH:MM:SSZ`
- **Dimension - File & Image**: UUID string of a pre-uploaded workspace file asset
- **List Attribute**: Must provide the exact UUID string of a valid defined `ListItem` option
- **Reference Attribute**: Must provide the exact UUID string of an existing referenced `Entity`

### Audit Trail & Metrics
- Dimension updates are recorded in the append-only entity dimension change history log.
- Metric attribute values submitted here are dispatched to the metric streaming pipeline for time-series aggregation.

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
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | Unique entity identifier (UUID)
    update_entity_request = omnismith_sdk.UpdateEntityRequest() # UpdateEntityRequest | 

    try:
        # Update entity attribute values
        api_instance.update_entity(id, update_entity_request)
    except Exception as e:
        print("Exception when calling EntityApi->update_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique entity identifier (UUID) | 
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
**204** | Entity attributes updated successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Tier quota exceeded |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

