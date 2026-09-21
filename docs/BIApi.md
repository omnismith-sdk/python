# omnismith_sdk.BIApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bi_schema**](BIApi.md#get_bi_schema) | **GET** /bi/schema | Get BI schema catalog
[**list_bi_template_rows**](BIApi.md#list_bi_template_rows) | **POST** /bi/templates/{template_id}/rows | List flattened template rows for BI integration
[**list_bi_template_time_series**](BIApi.md#list_bi_template_time_series) | **POST** /bi/templates/{template_id}/time-series | List aggregated time-series rows for BI integration


# **get_bi_schema**
> BiSchemaResponse get_bi_schema(x_omnismith_project_id=x_omnismith_project_id)

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
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Get BI schema catalog
        api_response = api_instance.get_bi_schema(x_omnismith_project_id=x_omnismith_project_id)
        print("The response of BIApi->get_bi_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BIApi->get_bi_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

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
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bi_template_rows**
> BiTemplateRowsResponse list_bi_template_rows(template_id, bi_list_template_rows_request, x_omnismith_project_id=x_omnismith_project_id, limit=limit, offset=offset, sort_field=sort_field, sort_direction=sort_direction)

List flattened template rows for BI integration

Returns a flattened, relational row-based live dataset for a template, optimized for BI dashboards, spreadsheets, and reporting tools.

### Tabular Data Model
Transforms dynamic entity records into flat rows where columns correspond to the attribute definitions retrieved from `GET /bi/schema`.

### Filter & Search Model
Accepts the same `filter_groups` and `global_search` payload as `searchEntities`.

### Filters (`filter_groups`)
A list of groups; clauses inside a group are AND-ed, groups are OR-ed. `[[a, b]]` is `a AND b`; `[[a], [b, c]]` is `a OR (b AND c)`; `[]` applies no filter.
```json
[
  [
    {"field": "status", "operator": "in", "value": ["018b…0020", "018b…0021"]},
    {"field": "created_at", "operator": "between", "value": ["2026-01-01", "2026-03-31"]},
    {"field": "customer.tier", "operator": "eq", "value": "018b…0042"}
  ],
  [{"field": "priority", "operator": "eq", "value": "018b…0007"}]
]
```
- **`field`**: attribute slug or UUID, a standard field (`id`, `created_at`, `updated_at`), or a one-hop path `<reference>.<attribute>` that filters on an attribute of the referenced record (e.g. `customer.tier`). One hop only.
- **`operator`** and **`value`**: `eq`, `neq`, `gt`, `lt`, `like` (case-insensitive substring), `not-like` take a string; `in`, `not-in` take a non-empty list of strings; `between` takes `[lower, upper]` (inclusive; number, date, datetime attributes and `created_at` / `updated_at`); `empty`, `not-empty` take no value.
- List and reference attributes compare the stored id (from `list_item_ids` / `reference_entity_ids` or the schema), never the label.
- Unknown fields, operators that do not fit the field, malformed values and paths that do not traverse a reference are refused with 400 naming the valid fields; a path into a template the caller may not view is 403.

### Sorting & Pagination
- `sort_field`: Attribute UUID, slug, or standard column (`id`, `created_at`, `updated_at`, `deleted_at`).
- `sort_direction`: `asc` or `desc`.
- `limit` (max 100) and `offset` pagination.

### Column Projection (`fields`)
Supply an optional `fields` array in the request body to project specific columns (e.g. `{"fields": ["price", "sku"]}`). Non-projected dynamic attribute columns are excluded from both the schema `columns` and row data, eliminating unnecessary attribute hydration and reducing tabular payload size.

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
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)
    limit = 50 # int | Maximum number of rows to return per page (1-100) (optional) (default to 50)
    offset = 0 # int | Zero-based pagination offset (optional) (default to 0)
    sort_field = 'created_at' # str | Attribute UUID, slug, or standard field (id, created_at, updated_at, deleted_at) to sort by (optional)
    sort_direction = asc # str | Sort direction: \"asc\" (ascending) or \"desc\" (descending) (optional) (default to asc)

    try:
        # List flattened template rows for BI integration
        api_response = api_instance.list_bi_template_rows(template_id, bi_list_template_rows_request, x_omnismith_project_id=x_omnismith_project_id, limit=limit, offset=offset, sort_field=sort_field, sort_direction=sort_direction)
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
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 
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
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bi_template_time_series**
> BiTimeSeriesResponse list_bi_template_time_series(template_id, attribute_ids, start, end, bi_list_template_rows_request, x_omnismith_project_id=x_omnismith_project_id, aggregate_func=aggregate_func, bucket_width=bucket_width)

List aggregated time-series rows for BI integration

Returns aggregated, time-bucketed metric data points across entities of a template schema for BI and analytical visualization tools.

### Combined Dimension Filtering & Metric Aggregation
Combines entity dimension filtering (scoped via the `filter_groups` and `global_search` body payload, same grammar as `searchEntities`) with time-series rollup across the specified `attribute_ids`.

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
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)
    aggregate_func = avg # str | Aggregation function applied within each time bucket (optional) (default to avg)
    bucket_width = 1 hour # str | Time bucket width interval (e.g. 1 minute, 5 minutes, 1 hour, 1 day) (optional) (default to 1 hour)

    try:
        # List aggregated time-series rows for BI integration
        api_response = api_instance.list_bi_template_time_series(template_id, attribute_ids, start, end, bi_list_template_rows_request, x_omnismith_project_id=x_omnismith_project_id, aggregate_func=aggregate_func, bucket_width=bucket_width)
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
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 
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
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

