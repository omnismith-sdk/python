# omnismith_sdk.AuditLogApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_audit_logs**](AuditLogApi.md#list_audit_logs) | **GET** /audit-logs | List project audit logs


# **list_audit_logs**
> ListAuditLogs200Response list_audit_logs(page=page, limit=limit, sort_by=sort_by, sort_direction=sort_direction, search=search, event_type=event_type, resource_type=resource_type, resource_id=resource_id, author_email=author_email, start=start, end=end)

List project audit logs

Returns an immutable, time-ordered audit trail of user and system events for the current project context.

### Security & Authorization
Restricted to authenticated users holding the Project Owner role.

### Comprehensive Filtering & Search
- `event_type`: Filter by single or comma-separated event types (e.g. `entity.created`, `entity.updated`, `entity.deleted`, `template.created`).
- `resource_type`: Filter by domain target (e.g. `entity`, `template`, `attribute`, `project`).
- `resource_id`: Filter by exact resource UUID.
- `author_email`: Filter by the actor email address.
- `start` and `end`: Date-time window bounding event occurrence (ISO 8601 or `YYYY-MM-DD HH:MM:SS`).
- `search`: Text search across event types, resource types, resource IDs, author emails, and value summaries.

### Pagination & Sorting
Supports 1-indexed pagination (`page`, `limit` up to 100) and sorting by `occurred_at`, `event_type`, `resource_type`, `resource_id`, or `author_email` (`asc`/`desc`).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_audit_logs200_response import ListAuditLogs200Response
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
    api_instance = omnismith_sdk.AuditLogApi(api_client)
    page = 1 # int | 1-based page number for pagination (optional) (default to 1)
    limit = 20 # int | Number of audit log records per page (1-100) (optional) (default to 20)
    sort_by = occurred_at # str | Field to sort audit log entries by (optional) (default to occurred_at)
    sort_direction = desc # str | Sort direction: \"asc\" (ascending) or \"desc\" (descending) (optional) (default to desc)
    search = 'entity.created' # str | Text search filter across event_type, resource_type, resource_id, author_email, and value (optional)
    event_type = 'entity.created' # str | Filter by single or comma-separated event types (e.g. \"entity.created,entity.updated\") (optional)
    resource_type = 'entity' # str | Filter by single or comma-separated resource types (e.g. \"entity,template,attribute\") (optional)
    resource_id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | Filter by exact resource unique identifier (UUID) (optional)
    author_email = 'demo@omnismith.io' # str | Filter by actor or author email address (optional)
    start = '2026-08-01T00:00:00Z' # datetime | Filter audit records occurring on or after this timestamp (ISO 8601 format) (optional)
    end = '2026-08-26T23:59:59Z' # datetime | Filter audit records occurring on or before this timestamp (ISO 8601 format) (optional)

    try:
        # List project audit logs
        api_response = api_instance.list_audit_logs(page=page, limit=limit, sort_by=sort_by, sort_direction=sort_direction, search=search, event_type=event_type, resource_type=resource_type, resource_id=resource_id, author_email=author_email, start=start, end=end)
        print("The response of AuditLogApi->list_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->list_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| 1-based page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of audit log records per page (1-100) | [optional] [default to 20]
 **sort_by** | **str**| Field to sort audit log entries by | [optional] [default to occurred_at]
 **sort_direction** | **str**| Sort direction: \&quot;asc\&quot; (ascending) or \&quot;desc\&quot; (descending) | [optional] [default to desc]
 **search** | **str**| Text search filter across event_type, resource_type, resource_id, author_email, and value | [optional] 
 **event_type** | **str**| Filter by single or comma-separated event types (e.g. \&quot;entity.created,entity.updated\&quot;) | [optional] 
 **resource_type** | **str**| Filter by single or comma-separated resource types (e.g. \&quot;entity,template,attribute\&quot;) | [optional] 
 **resource_id** | **UUID**| Filter by exact resource unique identifier (UUID) | [optional] 
 **author_email** | **str**| Filter by actor or author email address | [optional] 
 **start** | **datetime**| Filter audit records occurring on or after this timestamp (ISO 8601 format) | [optional] 
 **end** | **datetime**| Filter audit records occurring on or before this timestamp (ISO 8601 format) | [optional] 

### Return type

[**ListAuditLogs200Response**](ListAuditLogs200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of audit log records |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

