# omnismith_sdk.BIApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bi_schema**](BIApi.md#get_bi_schema) | **GET** /bi/schema | Get BI schema catalog
[**list_bi_template_rows**](BIApi.md#list_bi_template_rows) | **POST** /bi/templates/{template_id}/rows | List flattened template rows for BI integration
[**list_bi_template_time_series**](BIApi.md#list_bi_template_time_series) | **POST** /bi/templates/{template_id}/time-series | List aggregated time-series rows for BI integration


# **get_bi_schema**
> BiSchemaResponse get_bi_schema()

Get BI schema catalog

Returns a normalized metadata catalog of all template schemas and dynamic attribute definitions in the current workspace context.

### BI Tooling Compatibility
Designed for BI connectors (PowerBI, Tableau, Looker Studio, Metabase) and ETL ingestion pipelines. Translates dynamic template schemas into relational column definitions, data types (`string`, `number`, `boolean`, `datetime`, `date`), reference join keys, and allowed list options.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.bi_schema_response import BiSchemaResponse
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
    api_instance = omnismith_sdk.BIApi(api_client)

    try:
        # Get BI schema catalog
        api_response = api_instance.get_bi_schema()
        print("The response of BIApi->get_bi_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BIApi->get_bi_schema: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BiSchemaResponse**](BiSchemaResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Normalized BI schema catalog |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bi_template_rows**
> BiTemplateRowsResponse list_bi_template_rows(template_id, bi_list_template_rows_request, limit=limit, offset=offset, sort_field=sort_field, sort_direction=sort_direction)

List flattened template rows for BI integration

Returns a flattened, relational row-based live dataset for a template, optimized for BI dashboards, spreadsheets, and reporting tools.

### Tabular Data Model
Transforms dynamic entity records into flat rows where columns correspond to the attribute definitions retrieved from `GET /bi/schema`.

### Filter & Search Model
Supports structured `filters` (operators: `eq`, `neq`, `gt`, `lt`, `like`, `not-like`, `empty`, `not-empty`) and `global_search` text queries.

### Sorting & Pagination
- `sort_field`: Attribute UUID, slug, or standard column (`id`, `created_at`, `updated_at`, `deleted_at`).
- `sort_direction`: `asc` or `desc`.
- `limit` (max 100) and `offset` pagination.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.bi_list_template_rows_request import BiListTemplateRowsRequest
from omnismith_sdk.models.bi_template_rows_response import BiTemplateRowsResponse
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
    api_instance = omnismith_sdk.BIApi(api_client)
    template_id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010001') # UUID | Unique identifier (UUID) of the template schema to query
    bi_list_template_rows_request = omnismith_sdk.BiListTemplateRowsRequest() # BiListTemplateRowsRequest | 
    limit = 50 # int | Maximum number of rows to return per page (1-100) (optional) (default to 50)
    offset = 0 # int | Zero-based pagination offset (optional) (default to 0)
    sort_field = 'created_at' # str | Attribute UUID, slug, or standard field (id, created_at, updated_at, deleted_at) to sort by (optional)
    sort_direction = asc # str | Sort direction: \"asc\" (ascending) or \"desc\" (descending) (optional) (default to asc)

    try:
        # List flattened template rows for BI integration
        api_response = api_instance.list_bi_template_rows(template_id, bi_list_template_rows_request, limit=limit, offset=offset, sort_field=sort_field, sort_direction=sort_direction)
        print("The response of BIApi->list_bi_template_rows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BIApi->list_bi_template_rows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **UUID**| Unique identifier (UUID) of the template schema to query | 
 **bi_list_template_rows_request** | [**BiListTemplateRowsRequest**](BiListTemplateRowsRequest.md)|  | 
 **limit** | **int**| Maximum number of rows to return per page (1-100) | [optional] [default to 50]
 **offset** | **int**| Zero-based pagination offset | [optional] [default to 0]
 **sort_field** | **str**| Attribute UUID, slug, or standard field (id, created_at, updated_at, deleted_at) to sort by | [optional] 
 **sort_direction** | **str**| Sort direction: \&quot;asc\&quot; (ascending) or \&quot;desc\&quot; (descending) | [optional] [default to asc]

### Return type

[**BiTemplateRowsResponse**](BiTemplateRowsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flat dataset rows with column definitions |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bi_template_time_series**
> BiTimeSeriesResponse list_bi_template_time_series(template_id, attribute_ids, start, end, bi_list_template_rows_request, aggregate_func=aggregate_func, bucket_width=bucket_width)

List aggregated time-series rows for BI integration

Returns aggregated, time-bucketed metric data points across entities of a template schema for BI and analytical visualization tools.

### Combined Dimension Filtering & Metric Aggregation
Combines entity dimension filtering (scoped via the `filters` and `global_search` body payload) with time-series rollup across the specified `attribute_ids`.

### Aggregation Functions (`aggregate_func`)
- `avg` (default), `sum`, `min`, `max`, `count`, `first`, `last`.

### Bucket Intervals (`bucket_width`)
Values follow standard time interval notation: `1 second`, `5 seconds`, `10 seconds`, `1 minute` (1m), `5 minutes` (5m), `10 minutes`, `15 minutes`, `30 minutes`, `1 hour` (1h), `6 hours`, `12 hours`, `1 day` (1d), `1 week`, `1 month`.

### Query Window (`start` & `end`)
Specified as integer Unix epoch seconds bounding the telemetry observations.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.bi_list_template_rows_request import BiListTemplateRowsRequest
from omnismith_sdk.models.bi_time_series_response import BiTimeSeriesResponse
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
    api_instance = omnismith_sdk.BIApi(api_client)
    template_id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010001') # UUID | Unique identifier (UUID) of the template schema
    attribute_ids = '018b2f1b-8c1a-75b3-8000-7f0000010010,018b2f1b-8c1a-75b3-8000-7f0000010011' # str | Comma-separated metric attribute UUIDs to aggregate
    start = 1774396800 # int | Start timestamp as Unix epoch in seconds
    end = 1774483200 # int | End timestamp as Unix epoch in seconds
    bi_list_template_rows_request = omnismith_sdk.BiListTemplateRowsRequest() # BiListTemplateRowsRequest | 
    aggregate_func = avg # str | Aggregation function applied within each time bucket (optional) (default to avg)
    bucket_width = 1 hour # str | Time bucket width interval (e.g. 1 minute, 5 minutes, 1 hour, 1 day) (optional) (default to 1 hour)

    try:
        # List aggregated time-series rows for BI integration
        api_response = api_instance.list_bi_template_time_series(template_id, attribute_ids, start, end, bi_list_template_rows_request, aggregate_func=aggregate_func, bucket_width=bucket_width)
        print("The response of BIApi->list_bi_template_time_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BIApi->list_bi_template_time_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **UUID**| Unique identifier (UUID) of the template schema | 
 **attribute_ids** | **str**| Comma-separated metric attribute UUIDs to aggregate | 
 **start** | **int**| Start timestamp as Unix epoch in seconds | 
 **end** | **int**| End timestamp as Unix epoch in seconds | 
 **bi_list_template_rows_request** | [**BiListTemplateRowsRequest**](BiListTemplateRowsRequest.md)|  | 
 **aggregate_func** | **str**| Aggregation function applied within each time bucket | [optional] [default to avg]
 **bucket_width** | **str**| Time bucket width interval (e.g. 1 minute, 5 minutes, 1 hour, 1 day) | [optional] [default to 1 hour]

### Return type

[**BiTimeSeriesResponse**](BiTimeSeriesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flat time-series dataset |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

