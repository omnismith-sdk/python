# omnismith_sdk.EntityApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate_entities**](EntityApi.md#aggregate_entities) | **POST** /entities/aggregate/{template_id} | Count, sum, average, min or max entities, optionally grouped by attributes
[**batch_execute_entity_action**](EntityApi.md#batch_execute_entity_action) | **POST** /entities/batch/actions/{slug} | Execute an action on a selection of entities
[**batch_write_entities**](EntityApi.md#batch_write_entities) | **POST** /entities/batch | Apply a batch of mixed entity creates, updates, replaces, and deletes
[**create_entity**](EntityApi.md#create_entity) | **POST** /entities/template/{template} | Create a new dynamic entity
[**delete_entity**](EntityApi.md#delete_entity) | **DELETE** /entities/{id} | Soft-delete an entity record
[**execute_entity_action**](EntityApi.md#execute_entity_action) | **POST** /entities/{id}/actions/{slug} | Execute an action on an entity
[**export_entities**](EntityApi.md#export_entities) | **POST** /entities/export/{template_id} | Export entities to structured CSV file
[**get_entity**](EntityApi.md#get_entity) | **GET** /entities/{id} | Get an entity record by ID
[**get_entity_chart**](EntityApi.md#get_entity_chart) | **GET** /entities/{id}/chart | Get entity chart time-series data
[**get_entity_history**](EntityApi.md#get_entity_history) | **GET** /entities/{id}/history | Get entity dimension change history
[**import_entities**](EntityApi.md#import_entities) | **POST** /entities/import/{template_id} | Import entities from structured CSV file
[**ingest_entity_metrics**](EntityApi.md#ingest_entity_metrics) | **POST** /entities/{id}/metrics | Ingest high-frequency metric observations for an entity
[**list_entity_actions**](EntityApi.md#list_entity_actions) | **GET** /entities/{id}/actions | List the actions available on an entity
[**replace_entity**](EntityApi.md#replace_entity) | **PUT** /entities/{id} | Replace all non-metric attributes of an entity
[**search_entities**](EntityApi.md#search_entities) | **POST** /entities/search/{template_id} | Search entities with filtering, sorting, and pagination
[**semantic_search_entities**](EntityApi.md#semantic_search_entities) | **POST** /entities/semantic-search | Perform semantic vector similarity search on entities
[**update_entity**](EntityApi.md#update_entity) | **PATCH** /entities/{id} | Update entity attribute values


# **aggregate_entities**
> AggregateEntities200Response aggregate_entities(template_id, aggregate_entities_request, x_omnismith_project_id=x_omnismith_project_id)

Count, sum, average, min or max entities, optionally grouped by attributes

Answers "how many", "how much" and "broken down by" questions in one call, computed by the database. Use it instead of paginating `searchEntities` and tallying rows: a count or a per-status breakdown of a 10,000-record template is one small response.

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

### Grouping
`group_by` takes up to 3 attribute slugs or UUIDs. Lists, references, strings, numbers, booleans and dates can be keys. Each group's `key` mirrors `group_by` in order: `value` is the stored value (a list item id, an entity id, a scalar) and `custom_value` is the list item label or the referenced record's display value. A `null` value groups the records that have no value for that attribute. With no `group_by` the whole filtered set is one group.

### Aggregations
`aggregations` takes 1 to 10 `{op, field}` entries and each group's `aggregates` mirrors them in order.
- `count` — number of matching records. Takes no field; to count records that have a value, filter with `not-empty`.
- `sum`, `avg` — a number attribute.
- `min`, `max` — a number, date or datetime attribute.

Numbers come back as floats, dates as RFC 3339 strings, and `null` when no record in the group has a value. Metric attributes are rejected with a 400: they are time series and are reduced over a time window with `getEntityChart`; this endpoint reduces the current dimension values of records.

### Ordering and limits
Groups are ordered by the first aggregation descending (nulls last), then by key, so `[{"op": "count"}]` first gives a top-N breakdown. `limit` (1-100, default 50) caps the groups returned; `truncated: true` means more groups exist — narrow with `filter_groups` or group by fewer fields.

### Example
```json
{"filter_groups": [[{"field": "status", "operator": "eq", "value": "018b…0020"}]],
 "group_by": ["tier"],
 "aggregations": [{"op": "count"}, {"op": "sum", "field": "mrr"}]}
```
returns
```json
{"data": [{"key": [{"field": "tier", "value": "018b…0031", "custom_value": "Team"}],
           "aggregates": [{"op": "count", "field": null, "value": 12}, {"op": "sum", "field": "mrr", "value": 3400.5}]}],
 "limit": 50, "truncated": false}
```

Read-only. Applies the caller's template access and row scopes exactly as search does; restricted attributes are not valid fields.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.aggregate_entities200_response import AggregateEntities200Response
from omnismith_sdk.models.aggregate_entities_request import AggregateEntitiesRequest
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
    template_id = 'tenant_user' # str | Template UUID or human-readable template slug
    aggregate_entities_request = omnismith_sdk.AggregateEntitiesRequest() # AggregateEntitiesRequest | 
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Count, sum, average, min or max entities, optionally grouped by attributes
        api_response = api_instance.aggregate_entities(template_id, aggregate_entities_request, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of EntityApi->aggregate_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->aggregate_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Template UUID or human-readable template slug | 
 **aggregate_entities_request** | [**AggregateEntitiesRequest**](AggregateEntitiesRequest.md)|  | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**AggregateEntities200Response**](AggregateEntities200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Groups with their aggregates, ordered by the first aggregation descending |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_execute_entity_action**
> BatchExecuteEntityActionResponse batch_execute_entity_action(slug, batch_execute_entity_action_request, x_omnismith_project_id=x_omnismith_project_id)

Execute an action on a selection of entities

Runs one named action on many records in a single call — "confirm these forty". Each record goes through exactly what `POST /entities/{id}/actions/{slug}` (`execute_entity_action`) does: precondition, field matching, presets, type validation and the template's rules, with history attributed to the action. `values` are the same for every record.

The action is resolved per record on its template, so the selection may span templates that each define the slug; a record whose template does not is reported as `failed` with a 404 body.

At most 100 records per call; page a larger selection.

### Outcomes
By default (`atomic: false`) every record is attempted and the response is `200` with one outcome per record — `executed` with a receipt, or `precondition_failed` / `rule_violated` / `failed` with the error body the single-record endpoint would have returned. Read the counters, then `results` for the records that did not run.

With `atomic: true` the batch runs in one transaction and the first record that does not execute rolls all of it back. That case answers with that record's own error status and body plus `failed_entity_id`, not with a results list.

### Quotas
The dimension-update quota is checked for the whole selection before any record is written.

### Errors
- `400` — the body is not the documented shape, or lists an entity twice.
- `402` — the selection would cross the tier's update quota.
- `422` — a submitted value does not fit the action (only when nothing could run).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.batch_execute_entity_action_request import BatchExecuteEntityActionRequest
from omnismith_sdk.models.batch_execute_entity_action_response import BatchExecuteEntityActionResponse
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
    slug = 'confirm_attendance' # str | Action slug, as listed by `GET /templates/{templateId}/actions` or `GET /entities/{id}/actions`
    batch_execute_entity_action_request = omnismith_sdk.BatchExecuteEntityActionRequest() # BatchExecuteEntityActionRequest | 
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Execute an action on a selection of entities
        api_response = api_instance.batch_execute_entity_action(slug, batch_execute_entity_action_request, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of EntityApi->batch_execute_entity_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->batch_execute_entity_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Action slug, as listed by &#x60;GET /templates/{templateId}/actions&#x60; or &#x60;GET /entities/{id}/actions&#x60; | 
 **batch_execute_entity_action_request** | [**BatchExecuteEntityActionRequest**](BatchExecuteEntityActionRequest.md)|  | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**BatchExecuteEntityActionResponse**](BatchExecuteEntityActionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Batch applied. One outcome per record in &#x60;results&#x60;; the counters say how many ran. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Tier quota exceeded |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | An atomic batch stopped at a record whose precondition does not hold (&#x60;type: error/action-unavailable&#x60;, with &#x60;failed_entity_id&#x60;), or no project is selected |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_write_entities**
> BatchWriteEntitiesResponse batch_write_entities(batch_write_entities_request, x_omnismith_project_id=x_omnismith_project_id)

Apply a batch of mixed entity creates, updates, replaces, and deletes

Applies an ordered, heterogeneous list of entity writes in a single call: update these twenty, create three, replace two, delete one.

This is distinct from CSV import, which moves a homogeneous set of new rows. Use this endpoint when the set of edits is already computed and addresses known records.

### Operations
Every entry names an `op` and carries exactly the fields for it — nothing more, nothing less:
- `create`  — `{ "op": "create", "template": "<slug|uuid>", "id"?: "<uuidv7>", "attributes": { ... } }` (`attributes` may be `{}`)
- `update`  — `{ "op": "update", "id": "<uuid>", "attributes": { ... } }` (non-empty; partial, like PATCH)
- `replace` — `{ "op": "replace", "id": "<uuid>", "attributes": { ... } }` (like PUT: **attributes absent from the map are cleared**; `{}` clears all; metrics rejected)
- `delete`  — `{ "op": "delete", "id": "<uuid>" }` (soft delete)

`id` always means the entity id; `template` always means the template slug or UUID.

### `attributes`
An object keyed by attribute **slug or UUID** — mix them freely. Each value is a plain scalar, a backfill object `{ "value": ..., "updated_at": "<RFC 3339>" }`, or an operation object `{ "op": "increment", "value": <number> }`:

```json
{
  "hostname": "edge-fra-01",
  "cpu_cores": 8,
  "is_active": true,
  "notes": null,
  "01a094f1-24be-7154-a5bd-3b5c33c930fb": "01a094f1-4c1d-7498-b73b-48ae46da900b",
  "operational_status": { "value": "Active", "updated_at": "2026-09-12T12:23:52Z" },
  "restart_count": { "op": "increment", "value": 1 }
}
```

`null` clears an attribute. `{ "op": "increment", "value": n }` adds `n` to the stored number without you reading it first (number attributes and metrics only; concurrent increments never lose an update). Every attribute must belong to the entity's template and may appear only once (the same attribute as slug *and* UUID is rejected). Full value rules are on the `EntityAttributesInput` schema.

At most 100 operations per call. Larger sets must be split.

### Failure handling
By default (`atomic: false`) every operation is attempted, successes stand, and each failure is reported against its index with the same error body the single-entity endpoint would have returned. The response is `200` regardless of how many entries failed; read `failed` and the per-item `status`.

With `atomic: true` the whole batch runs in one transaction and the first failure rolls all of it back. That case answers with the failing operation's own error status and body plus `failed_index`, not with a results list. Atomic batches reject metric attribute values, because metric telemetry is published outside the transaction and cannot be rolled back.

### Quotas
Tier quotas are evaluated for the whole batch before any of it is applied, so a batch that would cross the limit is refused as a unit rather than applied halfway.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.batch_write_entities_request import BatchWriteEntitiesRequest
from omnismith_sdk.models.batch_write_entities_response import BatchWriteEntitiesResponse
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
    batch_write_entities_request = omnismith_sdk.BatchWriteEntitiesRequest() # BatchWriteEntitiesRequest | 
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Apply a batch of mixed entity creates, updates, replaces, and deletes
        api_response = api_instance.batch_write_entities(batch_write_entities_request, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of EntityApi->batch_write_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->batch_write_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_write_entities_request** | [**BatchWriteEntitiesRequest**](BatchWriteEntitiesRequest.md)|  | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**BatchWriteEntitiesResponse**](BatchWriteEntitiesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Batch applied. Per-item outcomes are in &#x60;results&#x60;; check &#x60;failed&#x60; for partial failure. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Tier quota exceeded |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entity**
> CreateEntity201Response create_entity(template, x_omnismith_project_id=x_omnismith_project_id, create_entity_request=create_entity_request)

Create a new dynamic entity

Creates one entity of the template named in the path — `{template}` is the template's slug or UUID — and returns its id. Pass `id` to choose the entity's UUIDv7 yourself (cross-system keys); otherwise one is generated. An `id` that already exists — even a soft-deleted entity's — is rejected with `409` rather than overwritten: if a retry might be hitting this because an earlier call's response was lost, `GET /entities/{id}` first to check whether it already carries what you meant to write, rather than retrying blindly.

### `attributes`
An object keyed by attribute **slug or UUID** — mix them freely. Each value is a plain scalar, a backfill object `{ "value": ..., "updated_at": "<RFC 3339>" }`, or an operation object `{ "op": "increment", "value": <number> }`:

```json
{
  "hostname": "edge-fra-01",
  "cpu_cores": 8,
  "is_active": true,
  "notes": null,
  "01a094f1-24be-7154-a5bd-3b5c33c930fb": "01a094f1-4c1d-7498-b73b-48ae46da900b",
  "operational_status": { "value": "Active", "updated_at": "2026-09-12T12:23:52Z" },
  "restart_count": { "op": "increment", "value": 1 }
}
```

`null` clears an attribute. `{ "op": "increment", "value": n }` adds `n` to the stored number without you reading it first (number attributes and metrics only; concurrent increments never lose an update). Every attribute must belong to the entity's template and may appear only once (the same attribute as slug *and* UUID is rejected). Full value rules are on the `EntityAttributesInput` schema.

`attributes` is required; send `{}` to create an entity with no values yet. Metric attributes in the map are appended to the entity's time series; everything else becomes the entity's initial state and is recorded in its history. Operation objects (`{ "op": ... }`) are rejected on create: there is no stored value to operate on yet, so send the initial number as a literal.

### Errors
- `400` — the body is not the documented shape (missing `attributes`, a list instead of an object, unknown fields, wrong types).
- `422` — the shape is right but the content is not: unknown attribute, attribute not on the template, duplicate attribute, bad `updated_at`, a value that fails its attribute type, or an operation on an attribute that is not a number. `errors` names the exact field, e.g. `attributes.status`.
- `404` — no template with that slug or UUID in this project.
- `409` — the given `id` already exists.

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
    template = 'article' # str | Template UUID or human-readable slug
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)
    create_entity_request = omnismith_sdk.CreateEntityRequest() # CreateEntityRequest |  (optional)

    try:
        # Create a new dynamic entity
        api_response = api_instance.create_entity(template, x_omnismith_project_id=x_omnismith_project_id, create_entity_request=create_entity_request)
        print("The response of EntityApi->create_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->create_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | **str**| Template UUID or human-readable slug | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 
 **create_entity_request** | [**CreateEntityRequest**](CreateEntityRequest.md)|  | [optional] 

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
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**409** | The given &#x60;id&#x60; already exists (&#x60;type: error/conflict&#x60;), or no project is selected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity**
> delete_entity(id, x_omnismith_project_id=x_omnismith_project_id)

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
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Soft-delete an entity record
        api_instance.delete_entity(id, x_omnismith_project_id=x_omnismith_project_id)
    except Exception as e:
        print("Exception when calling EntityApi->delete_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique entity identifier (UUID) to soft-delete | 
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
**204** | Entity soft-deleted successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_entity_action**
> ExecuteEntityActionResponse execute_entity_action(id, slug, x_omnismith_project_id=x_omnismith_project_id, execute_entity_action_request=execute_entity_action_request)

Execute an action on an entity

Runs one named action on one record as a single atomic write. Prefer this over a plain update (`PATCH /entities/{id}`, the `update_entity` tool) whenever `GET /entities/{id}/actions` (`list_entity_actions`) lists an action for what you intend: the action's presets are applied for you and its required fields are enforced.

### What happens
1. The action's precondition is checked against the record's current values — `409` if it does not hold, with the reason.
2. `values` are matched to the action's `fields`; an attribute the action does not ask for, or an empty required field, is `422` keyed by `attributes.<slug>`.
3. Presets are merged on top of `values` (presets win) and the result is written exactly like an entity update: attribute types are validated and the template's rules are enforced (`422` on a violation, in the same `attributes.<slug>` shape).

The response is a receipt naming what was written — for a number field sent as `{ "op": "increment", "value": n }` that is the operation itself; the resolved number lands in the record and its history. History rows produced by the write carry the action's slug.

### Errors
- `400` — the body is not the documented shape.
- `403` — the caller may not edit this record.
- `404` — no such entity, or the template has no enabled action with this slug.
- `409` — the precondition does not hold; `detail` says which attribute and why.
- `422` — a required field is empty, a value fails its attribute type, or a rule refuses the write.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.execute_entity_action_request import ExecuteEntityActionRequest
from omnismith_sdk.models.execute_entity_action_response import ExecuteEntityActionResponse
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
    slug = 'confirm_attendance' # str | Action slug, as listed by `GET /entities/{id}/actions`
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)
    execute_entity_action_request = omnismith_sdk.ExecuteEntityActionRequest() # ExecuteEntityActionRequest |  (optional)

    try:
        # Execute an action on an entity
        api_response = api_instance.execute_entity_action(id, slug, x_omnismith_project_id=x_omnismith_project_id, execute_entity_action_request=execute_entity_action_request)
        print("The response of EntityApi->execute_entity_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->execute_entity_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique entity identifier (UUID) | 
 **slug** | **str**| Action slug, as listed by &#x60;GET /entities/{id}/actions&#x60; | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 
 **execute_entity_action_request** | [**ExecuteEntityActionRequest**](ExecuteEntityActionRequest.md)|  | [optional] 

### Return type

[**ExecuteEntityActionResponse**](ExecuteEntityActionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The action ran; the receipt lists what was written |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Tier quota exceeded |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | The precondition does not hold for this record (&#x60;type: error/action-unavailable&#x60;), or no project is selected |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_entities**
> bytes export_entities(template_id, export_entities_request, x_omnismith_project_id=x_omnismith_project_id, sort_field=sort_field, sort_direction=sort_direction)

Export entities to structured CSV file

Exports entity records of a template schema matching filter criteria as a streaming CSV download.

### Re-importable CSV Schema Format
The generated CSV conforms to the Omnismith two-row metadata specification, making it directly compatible with `POST /entities/import/{template_id}`:
- **Row 1**: Display column names and attribute aliases.
- **Row 2**: Metadata row prefixed with `#` containing attribute UUIDs and column IDs (e.g. `#id`, `#018b2f1b-8c1a...`).
- **Row 3+**: Entity data records.

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
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)
    sort_field = 'created_at' # str | Attribute UUID, attribute slug, or standard field (id, created_at, updated_at, deleted_at) to sort by (optional)
    sort_direction = asc # str | Sort direction: \"asc\" (ascending) or \"desc\" (descending) (optional) (default to asc)

    try:
        # Export entities to structured CSV file
        api_response = api_instance.export_entities(template_id, export_entities_request, x_omnismith_project_id=x_omnismith_project_id, sort_field=sort_field, sort_direction=sort_direction)
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
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 
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
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity**
> EntityResponse get_entity(id, x_omnismith_project_id=x_omnismith_project_id, verbose=verbose, fields=fields)

Get an entity record by ID

Retrieves the full hydrated record for a dynamic entity by its unique identifier (UUID).

### Attribute Values Shape (`verbose`)
By default `attribute_values` is a compact object mapping each attribute slug to its display value (e.g. `{"title": "Fix login", "status": "Open", "assignee": "Jane Doe"}`). Attributes without a slug are keyed by their UUID; attributes whose value is empty are omitted. List, reference and file attributes show their label; the ids behind those labels come alongside in `list_item_ids`, `reference_entity_ids` and `file_ids` (same keys) — use those ids for writes and filters, which take ids rather than labels.
Pass `verbose=true` to receive an array of `EntityAttributeValue` items instead, each carrying the attribute `id`, `slug`, raw `value`, resolved display label (`custom_value`) and `reference_entity_id`; the id maps are then omitted.

### Selective Field Projection (`fields`)
By default, all dynamic attributes defined on the entity's template are hydrated and returned.
To optimize performance and minimize response payload volume, supply the `fields` query parameter as a comma-separated list of attribute slugs, attribute UUIDs, or root fields (e.g. `?fields=title,status`).
- **Selective Hydration**: Non-requested attribute values are excluded from database queries and omitted from `attribute_values`.
- **Root Metadata Guaranteed**: Essential entity identifiers and timestamps (`id`, `template_id`, `template_slug`, `created_at`, `updated_at`) are always returned regardless of the projection.
- **Strict Validation**: Requesting unknown field names returns HTTP 400 Bad Request naming all valid attribute slugs and standard fields for the template.

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
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)
    verbose = False # bool | When true, attribute_values is an array of EntityAttributeValue items with attribute id, slug, raw value, resolved custom_value and reference_entity_id. When false (default), attribute_values is a compact object mapping attribute slug to display value, with the ids behind list, reference and file labels in list_item_ids, reference_entity_ids and file_ids. (optional) (default to False)
    fields = ['[\"title\",\"status\"]'] # List[str] | Comma-separated list of attribute slugs, attribute UUIDs, or root fields to project (e.g. \"title,status\"). When specified, only the requested attributes are fetched and returned in attribute_values, avoiding database hydration for unneeded attributes and significantly reducing response payload size. If omitted, all attributes defined on the template are returned. (optional)

    try:
        # Get an entity record by ID
        api_response = api_instance.get_entity(id, x_omnismith_project_id=x_omnismith_project_id, verbose=verbose, fields=fields)
        print("The response of EntityApi->get_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->get_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique entity identifier (UUID) | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 
 **verbose** | **bool**| When true, attribute_values is an array of EntityAttributeValue items with attribute id, slug, raw value, resolved custom_value and reference_entity_id. When false (default), attribute_values is a compact object mapping attribute slug to display value, with the ids behind list, reference and file labels in list_item_ids, reference_entity_ids and file_ids. | [optional] [default to False]
 **fields** | [**List[str]**](str.md)| Comma-separated list of attribute slugs, attribute UUIDs, or root fields to project (e.g. \&quot;title,status\&quot;). When specified, only the requested attributes are fetched and returned in attribute_values, avoiding database hydration for unneeded attributes and significantly reducing response payload size. If omitted, all attributes defined on the template are returned. | [optional] 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_chart**
> GetEntityChart200Response get_entity_chart(id, attribute_ids, start, end, x_omnismith_project_id=x_omnismith_project_id, aggregate_func=aggregate_func, bucket_width=bucket_width)

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
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)
    aggregate_func = avg # str | Aggregation function applied within each bucket (optional) (default to avg)
    bucket_width = 1 hour # str | Time bucket width interval (e.g. 1 minute, 5 minutes, 1 hour, 1 day) (optional) (default to 1 hour)

    try:
        # Get entity chart time-series data
        api_response = api_instance.get_entity_chart(id, attribute_ids, start, end, x_omnismith_project_id=x_omnismith_project_id, aggregate_func=aggregate_func, bucket_width=bucket_width)
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
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 
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
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_history**
> GetEntityHistory200Response get_entity_history(id, x_omnismith_project_id=x_omnismith_project_id, page=page, limit=limit, sort_by=sort_by, sort_direction=sort_direction, search=search, attribute_ids=attribute_ids, start=start, end=end, author_email=author_email)

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
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)
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
        api_response = api_instance.get_entity_history(id, x_omnismith_project_id=x_omnismith_project_id, page=page, limit=limit, sort_by=sort_by, sort_direction=sort_direction, search=search, attribute_ids=attribute_ids, start=start, end=end, author_email=author_email)
        print("The response of EntityApi->get_entity_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->get_entity_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique entity identifier (UUID) | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 
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
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_entities**
> ImportEntities200Response import_entities(template_id, file, x_omnismith_project_id=x_omnismith_project_id)

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
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Import entities from structured CSV file
        api_response = api_instance.import_entities(template_id, file, x_omnismith_project_id=x_omnismith_project_id)
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
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

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
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ingest_entity_metrics**
> ingest_entity_metrics(id, ingest_metrics_request, x_omnismith_project_id=x_omnismith_project_id)

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
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Ingest high-frequency metric observations for an entity
        api_instance.ingest_entity_metrics(id, ingest_metrics_request, x_omnismith_project_id=x_omnismith_project_id)
    except Exception as e:
        print("Exception when calling EntityApi->ingest_entity_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique entity identifier (UUID) | 
 **ingest_metrics_request** | [**IngestMetricsRequest**](IngestMetricsRequest.md)|  | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

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
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entity_actions**
> ListEntityActions200Response list_entity_actions(id, x_omnismith_project_id=x_omnismith_project_id)

List the actions available on an entity

The enabled actions of the entity's template, each evaluated against the record's current values.

Call this before changing a record: when an action exists for what you intend (a status transition, a hand-off), run it with `POST /entities/{id}/actions/{slug}` (the `execute_entity_action` tool) instead of a plain update (`update_entity`), so its presets and required fields apply.

Each entry says whether the action is `available` now and, if not, `unavailable_reason` names the attribute, the expectation and the current value. `fields` are the values to submit (keyed by `slug` in the execute body), with the list choices and reference target resolved; `presets` are what the action will set on its own.

Disabled actions are not listed. Read-only: nothing is written.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_entity_actions200_response import ListEntityActions200Response
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
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # List the actions available on an entity
        api_response = api_instance.list_entity_actions(id, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of EntityApi->list_entity_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->list_entity_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique entity identifier (UUID) | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

### Return type

[**ListEntityActions200Response**](ListEntityActions200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Actions of the entity&#39;s template with per-record availability, in display order |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_entity**
> replace_entity(id, replace_entity_request, x_omnismith_project_id=x_omnismith_project_id)

Replace all non-metric attributes of an entity

Full replacement: after this call the entity's dimension attributes are exactly the map you sent. Every non-metric attribute of the template that is **absent from the map is cleared**. Use PATCH unless you really mean "make the record look exactly like this".

### `attributes`
An object keyed by attribute **slug or UUID** — mix them freely. Each value is a plain scalar, a backfill object `{ "value": ..., "updated_at": "<RFC 3339>" }`, or an operation object `{ "op": "increment", "value": <number> }`:

```json
{
  "hostname": "edge-fra-01",
  "cpu_cores": 8,
  "is_active": true,
  "notes": null,
  "01a094f1-24be-7154-a5bd-3b5c33c930fb": "01a094f1-4c1d-7498-b73b-48ae46da900b",
  "operational_status": { "value": "Active", "updated_at": "2026-09-12T12:23:52Z" },
  "restart_count": { "op": "increment", "value": 1 }
}
```

`null` clears an attribute. `{ "op": "increment", "value": n }` adds `n` to the stored number without you reading it first (number attributes and metrics only; concurrent increments never lose an update). Every attribute must belong to the entity's template and may appear only once (the same attribute as slug *and* UUID is rejected). Full value rules are on the `EntityAttributesInput` schema.

`attributes` is required; an explicit `{}` clears every non-metric attribute. Metric attributes are append-only telemetry and cannot be replaced — including one in the map is a `422`; send it via PATCH or `/entities/{id}/metrics`.

### Errors
- `400` — the body is not the documented shape (missing `attributes`, a list instead of an object, unknown fields, wrong types).
- `422` — the shape is right but the content is not: unknown attribute, attribute not on the template, duplicate attribute, bad `updated_at`, a value that fails its attribute type, or an operation on an attribute that is not a number. `errors` names the exact field, e.g. `attributes.status`.
- `404` — no entity with that id.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.replace_entity_request import ReplaceEntityRequest
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
    replace_entity_request = omnismith_sdk.ReplaceEntityRequest() # ReplaceEntityRequest | 
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Replace all non-metric attributes of an entity
        api_instance.replace_entity(id, replace_entity_request, x_omnismith_project_id=x_omnismith_project_id)
    except Exception as e:
        print("Exception when calling EntityApi->replace_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique entity identifier (UUID) | 
 **replace_entity_request** | [**ReplaceEntityRequest**](ReplaceEntityRequest.md)|  | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

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
**204** | Entity attributes replaced successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Tier quota exceeded |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_entities**
> SearchEntities200Response search_entities(template_id, search_entities_request, x_omnismith_project_id=x_omnismith_project_id, limit=limit, offset=offset, sort_field=sort_field, sort_direction=sort_direction)

Search entities with filtering, sorting, and pagination

Executes structured queries, full-text searches, and sorting across dynamic entities of a specified template schema.

### Template Targeting (`template_id`)
Accepts either a canonical template UUID (e.g. `018b2f1b-8c1a...`) or a human-readable template slug (e.g. `product_catalog`).

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

### Global Search (`global_search`)
Performs accelerated full-text and GIN trigram matching across all string dimension attributes defined on the template.

### Sorting & Pagination
- **`sort_field`**: Attribute UUID, attribute slug, or standard entity fields (`id`, `created_at`, `updated_at`, `deleted_at`).
- **`sort_direction`**: `asc` or `desc` (default: `asc` when `sort_field` is set, otherwise default sort is `created_at` DESC).
- **`limit`** and **`offset`**: Bounded pagination (max 100 per page).

### Attribute Values Shape (`verbose`)
By default each record's `attribute_values` is a compact object mapping attribute slug to display value (UUID key when the attribute has no slug; empty values omitted). List, reference and file attributes show their label; the ids behind those labels come alongside in `list_item_ids`, `reference_entity_ids` and `file_ids` — filters and writes take those ids, not labels.
Set `"verbose": true` in the request body to receive an array of `EntityAttributeValue` items with attribute `id`, `slug`, raw `value`, resolved `custom_value` and `reference_entity_id` instead.

### Selective Field Projection (`fields`)
By default, every matched entity is fully hydrated with all its attribute values.
When querying large result sets or when only a subset of attributes is required, supply the `fields` array in the request body (e.g. `{"fields": ["title", "status"]}`).
- **Selective Hydration**: Skips database value retrieval, reference lookups, list label resolution, and serialization for omitted attributes.
- **Minimal Payload Volume**: Substantially reduces response payload size and network transfer overhead when reading multiple records.
- **Root Metadata Guaranteed**: Essential entity identifiers and timestamps (`id`, `template_id`, `template_slug`, `created_at`, `updated_at`) are always preserved on every record.
- **Self-Correcting Validation**: If an unrecognized field name is requested, the endpoint returns HTTP 400 Bad Request enumerating all valid attribute slugs and standard fields for the template.

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
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)
    limit = 50 # int | Maximum number of entity records to return (1-100) (optional) (default to 50)
    offset = 0 # int | Zero-based pagination offset (optional) (default to 0)
    sort_field = 'created_at' # str | Attribute UUID, attribute slug, or standard field (id, created_at, updated_at, deleted_at) to sort by (optional)
    sort_direction = asc # str | Sort direction: \"asc\" (ascending) or \"desc\" (descending) (optional) (default to asc)

    try:
        # Search entities with filtering, sorting, and pagination
        api_response = api_instance.search_entities(template_id, search_entities_request, x_omnismith_project_id=x_omnismith_project_id, limit=limit, offset=offset, sort_field=sort_field, sort_direction=sort_direction)
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
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 
 **limit** | **int**| Maximum number of entity records to return (1-100) | [optional] [default to 50]
 **offset** | **int**| Zero-based pagination offset | [optional] [default to 0]
 **sort_field** | **str**| Attribute UUID, attribute slug, or standard field (id, created_at, updated_at, deleted_at) to sort by | [optional] 
 **sort_direction** | **str**| Sort direction: \&quot;asc\&quot; (ascending) or \&quot;desc\&quot; (descending) | [optional] [default to asc]

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **semantic_search_entities**
> List[SemanticSearchResultItem] semantic_search_entities(semantic_search_entities_request, x_omnismith_project_id=x_omnismith_project_id)

Perform semantic vector similarity search on entities

Executes an approximate nearest neighbors (ANN) vector similarity search across entity dimension embeddings.

### 768-Dimensional Embedding Vectors
Requires a 768-dimensional float embedding array (`query_vector`) representing the query text or multimodal vector (e.g. generated by Google `text-embedding-004` or similar models).

### Scoping & Filtering (`template_id`)
Pass an optional `template_id` (UUID) or template slug to constrain the semantic search to records belonging to a specific template schema.

### Cosine Similarity Threshold & Ranking (`threshold`)
- `threshold`: Minimum cosine similarity score threshold (range `0.0` to `1.0`, default `0.5`). Observations below this similarity cutoff are discarded.
- Matches are returned strictly ranked in descending order of `similarity_score`.

### Attribute Values Shape (`verbose`)
By default each nested entity's `attribute_values` is a compact object mapping attribute slug to display value, with the ids behind list, reference and file labels in `list_item_ids`, `reference_entity_ids` and `file_ids`. Set `"verbose": true` to receive an array of `EntityAttributeValue` items with attribute `id`, `slug`, raw `value`, resolved `custom_value` and `reference_entity_id` instead.

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
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Perform semantic vector similarity search on entities
        api_response = api_instance.semantic_search_entities(semantic_search_entities_request, x_omnismith_project_id=x_omnismith_project_id)
        print("The response of EntityApi->semantic_search_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->semantic_search_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **semantic_search_entities_request** | [**SemanticSearchEntitiesRequest**](SemanticSearchEntitiesRequest.md)|  | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

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
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity**
> update_entity(id, update_entity_request, x_omnismith_project_id=x_omnismith_project_id)

Update entity attribute values

Partial update: writes the attributes in the map and leaves every other attribute untouched. This is the default way to change an entity.

### `attributes`
An object keyed by attribute **slug or UUID** — mix them freely. Each value is a plain scalar, a backfill object `{ "value": ..., "updated_at": "<RFC 3339>" }`, or an operation object `{ "op": "increment", "value": <number> }`:

```json
{
  "hostname": "edge-fra-01",
  "cpu_cores": 8,
  "is_active": true,
  "notes": null,
  "01a094f1-24be-7154-a5bd-3b5c33c930fb": "01a094f1-4c1d-7498-b73b-48ae46da900b",
  "operational_status": { "value": "Active", "updated_at": "2026-09-12T12:23:52Z" },
  "restart_count": { "op": "increment", "value": 1 }
}
```

`null` clears an attribute. `{ "op": "increment", "value": n }` adds `n` to the stored number without you reading it first (number attributes and metrics only; concurrent increments never lose an update). Every attribute must belong to the entity's template and may appear only once (the same attribute as slug *and* UUID is rejected). Full value rules are on the `EntityAttributesInput` schema.

`attributes` is required and must not be empty. Dimension changes are appended to the entity's history (unchanged values cost nothing); metric attributes are appended to the entity's time series.

### Errors
- `400` — the body is not the documented shape (missing `attributes`, a list instead of an object, unknown fields, wrong types).
- `422` — the shape is right but the content is not: unknown attribute, attribute not on the template, duplicate attribute, bad `updated_at`, a value that fails its attribute type, or an operation on an attribute that is not a number. `errors` names the exact field, e.g. `attributes.status`.
- `404` — no entity with that id.

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
    x_omnismith_project_id = UUID('018b2f1b-7c3a-7d2e-8f1a-2b3c4d5e6f7d') # UUID | The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential's `projects` claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code `stale_project_grant`; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 `no_project_selected`. Two clients holding the same credential may send different values at the same time. (optional)

    try:
        # Update entity attribute values
        api_instance.update_entity(id, update_entity_request, x_omnismith_project_id=x_omnismith_project_id)
    except Exception as e:
        print("Exception when calling EntityApi->update_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique entity identifier (UUID) | 
 **update_entity_request** | [**UpdateEntityRequest**](UpdateEntityRequest.md)|  | 
 **x_omnismith_project_id** | **UUID**| The project this call acts on. A credential proves identity and grants a set of projects; it never selects one, so every tenant-scoped call names its target here. The value must be one of the projects in the credential&#39;s &#x60;projects&#x60; claim and must still be reachable — a project the caller is not a member of, or one that has been deleted, is rejected with 403 rather than silently ignored. A project the caller *is* a member of but which the credential predates is also rejected with 403, carrying the code &#x60;stale_project_grant&#x60;; that one is answered by refreshing the credential once and retrying, and is the only 403 here worth retrying. Omitting the header is not an error: the caller is simply acting with no project selected, and a tenant-scoped operation then answers 409 &#x60;no_project_selected&#x60;. Two clients holding the same credential may send different values at the same time. | [optional] 

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
**409** | No project is selected. The caller is authenticated but the request is tenant-scoped, so a project must be selected before it can be answered. The response body carries &#x60;\&quot;code\&quot;: \&quot;no_project_selected\&quot;&#x60;, which clients branch on to offer a project picker rather than an access-denied message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

