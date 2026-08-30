# omnismith_sdk.MCPApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_attribute**](MCPApi.md#create_attribute) | **POST** /attributes | Create a new attribute
[**create_attribute_item**](MCPApi.md#create_attribute_item) | **POST** /attributes/{id}/items | Add a list item to an attribute
[**create_automation**](MCPApi.md#create_automation) | **POST** /automation/automations | Create an automation rule
[**create_dashboard**](MCPApi.md#create_dashboard) | **POST** /dashboards | Create a new dashboard
[**create_dashboard_block**](MCPApi.md#create_dashboard_block) | **POST** /dashboards/{dashboardId}/blocks | Create a new block in a dashboard
[**create_entity**](MCPApi.md#create_entity) | **POST** /entities | Create a new dynamic entity
[**create_notification_channel**](MCPApi.md#create_notification_channel) | **POST** /automation/notification-channels | Create a notification channel
[**create_template**](MCPApi.md#create_template) | **POST** /templates | Create a new template
[**create_workspace**](MCPApi.md#create_workspace) | **POST** /workspaces | Create a new workspace
[**create_workspace_view**](MCPApi.md#create_workspace_view) | **POST** /workspaces/{id}/views | Add a new view / pane to a workspace
[**delete_attribute**](MCPApi.md#delete_attribute) | **DELETE** /attributes/{id} | Delete an attribute
[**delete_attribute_reference_config**](MCPApi.md#delete_attribute_reference_config) | **DELETE** /attributes/{id}/reference | Delete reference configuration for an attribute
[**delete_automation**](MCPApi.md#delete_automation) | **DELETE** /automation/automations/{id} | Delete an automation
[**delete_dashboard**](MCPApi.md#delete_dashboard) | **DELETE** /dashboards/{id} | Delete a dashboard
[**delete_dashboard_block**](MCPApi.md#delete_dashboard_block) | **DELETE** /dashboards/{dashboardId}/blocks/{blockId} | Delete a dashboard block
[**delete_entity**](MCPApi.md#delete_entity) | **DELETE** /entities/{id} | Soft-delete an entity record
[**delete_notification_channel**](MCPApi.md#delete_notification_channel) | **DELETE** /automation/notification-channels/{id} | Delete a notification channel
[**delete_template**](MCPApi.md#delete_template) | **DELETE** /templates/{id} | Delete a template
[**delete_workspace**](MCPApi.md#delete_workspace) | **DELETE** /workspaces/{id} | Delete a workspace and its views
[**delete_workspace_view**](MCPApi.md#delete_workspace_view) | **DELETE** /workspaces/{id}/views/{viewId} | Delete a view / pane from a workspace
[**get_attribute**](MCPApi.md#get_attribute) | **GET** /attributes/{id} | Get an attribute by ID
[**get_attribute_reference_config**](MCPApi.md#get_attribute_reference_config) | **GET** /attributes/{id}/reference | Get reference configuration for an attribute
[**get_automation**](MCPApi.md#get_automation) | **GET** /automation/automations/{id} | Get an automation by ID
[**get_dashboard**](MCPApi.md#get_dashboard) | **GET** /dashboards/{id} | Get a dashboard by ID
[**get_dashboard_block**](MCPApi.md#get_dashboard_block) | **GET** /dashboards/{dashboardId}/blocks/{blockId} | Get a dashboard block by ID
[**get_entity**](MCPApi.md#get_entity) | **GET** /entities/{id} | Get an entity record by ID
[**get_entity_chart**](MCPApi.md#get_entity_chart) | **GET** /entities/{id}/chart | Get entity chart time-series data
[**get_entity_history**](MCPApi.md#get_entity_history) | **GET** /entities/{id}/history | Get entity dimension change history
[**get_marketplace_blueprint**](MCPApi.md#get_marketplace_blueprint) | **GET** /marketplace/blueprints/{id} | Get marketplace blueprint details
[**get_notification_channel**](MCPApi.md#get_notification_channel) | **GET** /automation/notification-channels/{id} | Get a notification channel by ID
[**get_project_schema**](MCPApi.md#get_project_schema) | **GET** /discovery/project-schema | Get complete project schema graph
[**get_template**](MCPApi.md#get_template) | **GET** /templates/{id} | Get a template by ID or slug
[**get_usage_insights**](MCPApi.md#get_usage_insights) | **GET** /billing/usage/insights | Get current tier usage insights
[**get_workspace**](MCPApi.md#get_workspace) | **GET** /workspaces/{id} | Get workspace details and its views
[**get_workspace_view**](MCPApi.md#get_workspace_view) | **GET** /workspaces/{id}/views/{viewId} | Get details of a workspace view / pane
[**ingest_entity_metrics**](MCPApi.md#ingest_entity_metrics) | **POST** /entities/{id}/metrics | Ingest high-frequency metric observations for an entity
[**install_marketplace_blueprint**](MCPApi.md#install_marketplace_blueprint) | **POST** /marketplace/blueprints/{id}/install | Install a marketplace blueprint into a project
[**list_attribute_items**](MCPApi.md#list_attribute_items) | **GET** /attributes/{id}/items | List items of an attribute
[**list_attributes**](MCPApi.md#list_attributes) | **GET** /attributes | List all attributes
[**list_audit_logs**](MCPApi.md#list_audit_logs) | **GET** /audit-logs | List project audit logs
[**list_automations**](MCPApi.md#list_automations) | **GET** /automation/automations | List project automations
[**list_dashboard_blocks**](MCPApi.md#list_dashboard_blocks) | **GET** /dashboards/{dashboardId}/blocks | List all blocks in a dashboard
[**list_dashboards**](MCPApi.md#list_dashboards) | **GET** /dashboards | List all dashboards
[**list_notification_channels**](MCPApi.md#list_notification_channels) | **GET** /automation/notification-channels | List notification channels
[**list_template_entity_counts**](MCPApi.md#list_template_entity_counts) | **GET** /templates/entity-counts | List entity counts per template
[**list_templates**](MCPApi.md#list_templates) | **GET** /templates | List all templates
[**list_workspaces**](MCPApi.md#list_workspaces) | **GET** /workspaces | List all workspaces for current project
[**patch_attribute**](MCPApi.md#patch_attribute) | **PATCH** /attributes/{id} | Patch an attribute (granular partial update)
[**patch_template**](MCPApi.md#patch_template) | **PATCH** /templates/{id} | Patch a template (granular partial update)
[**resolve_dashboard_block**](MCPApi.md#resolve_dashboard_block) | **GET** /dashboards/{dashboardId}/blocks/{blockId}/resolve | Resolve a dashboard block to its computed data
[**search_entities**](MCPApi.md#search_entities) | **POST** /entities/search/{template_id} | Search entities with filtering, sorting, and pagination
[**search_marketplace_blueprints**](MCPApi.md#search_marketplace_blueprints) | **GET** /marketplace/blueprints | Search marketplace blueprints
[**set_attribute_items**](MCPApi.md#set_attribute_items) | **PUT** /attributes/{id}/items | Set list items for an attribute (replaces all existing items)
[**set_attribute_reference_config**](MCPApi.md#set_attribute_reference_config) | **PUT** /attributes/{id}/reference | Set or update reference configuration for an attribute
[**test_notification_channel**](MCPApi.md#test_notification_channel) | **POST** /automation/notification-channels/{id}/test | Send a test notification message
[**toggle_automation**](MCPApi.md#toggle_automation) | **PATCH** /automation/automations/{id}/toggle | Toggle automation enabled status
[**update_attribute**](MCPApi.md#update_attribute) | **PUT** /attributes/{id} | Update an attribute (full replacement)
[**update_automation**](MCPApi.md#update_automation) | **PUT** /automation/automations/{id} | Update an automation
[**update_dashboard**](MCPApi.md#update_dashboard) | **PUT** /dashboards/{id} | Update a dashboard
[**update_dashboard_block**](MCPApi.md#update_dashboard_block) | **PUT** /dashboards/{dashboardId}/blocks/{blockId} | Update a dashboard block
[**update_entity**](MCPApi.md#update_entity) | **PATCH** /entities/{id} | Update entity attribute values
[**update_notification_channel**](MCPApi.md#update_notification_channel) | **PUT** /automation/notification-channels/{id} | Update a notification channel
[**update_template**](MCPApi.md#update_template) | **PUT** /templates/{id} | Update a template (full replacement)
[**update_workspace**](MCPApi.md#update_workspace) | **PUT** /workspaces/{id} | Update workspace metadata and layout
[**update_workspace_view**](MCPApi.md#update_workspace_view) | **PUT** /workspaces/{id}/views/{viewId} | Update workspace view / pane filters, sort, display mode, or columns


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
    api_instance = omnismith_sdk.MCPApi(api_client)
    create_attribute_request = omnismith_sdk.CreateAttributeRequest() # CreateAttributeRequest | 

    try:
        # Create a new attribute
        api_response = api_instance.create_attribute(create_attribute_request)
        print("The response of MCPApi->create_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->create_attribute: %s\n" % e)
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the List-type attribute
    add_list_item_request = omnismith_sdk.AddListItemRequest() # AddListItemRequest | 

    try:
        # Add a list item to an attribute
        api_response = api_instance.create_attribute_item(id, add_list_item_request)
        print("The response of MCPApi->create_attribute_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->create_attribute_item: %s\n" % e)
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

# **create_automation**
> CreateAutomation201Response create_automation(create_automation_request)

Create an automation rule

Creates a new event-driven automation rule within the current project. Configures event trigger criteria (such as `on_entity_created`, `on_entity_updated`, or `on_attribute_changed`), multi-condition filters evaluating attribute values (using operators `eq`, `neq`, `gt`, `gte`, `lt`, `lte`, `contains`, `not_contains`, `is_empty`, `is_not_empty` across current value or delta modes), automated action targets (`telegram`, `webhook`, `push`), and an optional cooldown window in seconds to throttle repeated firings for the same entity.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_automation201_response import CreateAutomation201Response
from omnismith_sdk.models.create_automation_request import CreateAutomationRequest
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    create_automation_request = omnismith_sdk.CreateAutomationRequest() # CreateAutomationRequest | 

    try:
        # Create an automation rule
        api_response = api_instance.create_automation(create_automation_request)
        print("The response of MCPApi->create_automation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->create_automation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_automation_request** | [**CreateAutomationRequest**](CreateAutomationRequest.md)|  | 

### Return type

[**CreateAutomation201Response**](CreateAutomation201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Automation successfully created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Tier quota exceeded |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dashboard**
> CreateDashboard201Response create_dashboard(create_dashboard_request)

Create a new dashboard

Creates a new analytics and telemetry dashboard canvas for organizing metric KPIs, charts, gauges, and entity tables within a customizable grid layout.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_dashboard201_response import CreateDashboard201Response
from omnismith_sdk.models.create_dashboard_request import CreateDashboardRequest
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    create_dashboard_request = omnismith_sdk.CreateDashboardRequest() # CreateDashboardRequest | Dashboard creation payload

    try:
        # Create a new dashboard
        api_response = api_instance.create_dashboard(create_dashboard_request)
        print("The response of MCPApi->create_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->create_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_dashboard_request** | [**CreateDashboardRequest**](CreateDashboardRequest.md)| Dashboard creation payload | 

### Return type

[**CreateDashboard201Response**](CreateDashboard201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Dashboard created successfully |  -  |
**401** | Unauthorized |  -  |
**402** | Tier quota exceeded |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dashboard_block**
> CreateDashboardBlock201Response create_dashboard_block(dashboard_id, create_dashboard_block_request)

Create a new block in a dashboard

Creates a new visualization block widget on a dashboard canvas. Supports four block types: stat (single KPI counter of matching entities), chart (time-series telemetry multi-line/bar graph aggregating metric data), gauge (metric threshold gauge with min/max bounds and percentage progress), and list (filtered and sorted entity table). Grid placement is defined via x, y, cols, rows layout parameters.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_dashboard_block201_response import CreateDashboardBlock201Response
from omnismith_sdk.models.create_dashboard_block_request import CreateDashboardBlockRequest
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    dashboard_id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Target dashboard unique identifier (UUID)
    create_dashboard_block_request = omnismith_sdk.CreateDashboardBlockRequest() # CreateDashboardBlockRequest | Dashboard block creation payload

    try:
        # Create a new block in a dashboard
        api_response = api_instance.create_dashboard_block(dashboard_id, create_dashboard_block_request)
        print("The response of MCPApi->create_dashboard_block:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->create_dashboard_block: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **UUID**| Target dashboard unique identifier (UUID) | 
 **create_dashboard_block_request** | [**CreateDashboardBlockRequest**](CreateDashboardBlockRequest.md)| Dashboard block creation payload | 

### Return type

[**CreateDashboardBlock201Response**](CreateDashboardBlock201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Dashboard block created successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = omnismith_sdk.MCPApi(api_client)
    create_entity_request = omnismith_sdk.CreateEntityRequest() # CreateEntityRequest | 

    try:
        # Create a new dynamic entity
        api_response = api_instance.create_entity(create_entity_request)
        print("The response of MCPApi->create_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->create_entity: %s\n" % e)
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    create_notification_channel_request = omnismith_sdk.CreateNotificationChannelRequest() # CreateNotificationChannelRequest | 

    try:
        # Create a notification channel
        api_response = api_instance.create_notification_channel(create_notification_channel_request)
        print("The response of MCPApi->create_notification_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->create_notification_channel: %s\n" % e)
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

# **create_template**
> CreateTemplate201Response create_template(create_template_request)

Create a new template

Creates a new dynamic schema template (content type) in the project. Accepts template name, optional description, category, unique slug, attribute bindings, and UI layout groups. Attribute bindings can be defined using structured `attributes` (with optional `default_value` validated against attribute kind/data type) or flat `attribute_ids` / `attribute_slugs`. Visual layout groups organize attributes into 1- or 2-column sections with optional icons. Creating templates is subject to tier quota limits.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_template201_response import CreateTemplate201Response
from omnismith_sdk.models.create_template_request import CreateTemplateRequest
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    create_template_request = omnismith_sdk.CreateTemplateRequest() # CreateTemplateRequest | 

    try:
        # Create a new template
        api_response = api_instance.create_template(create_template_request)
        print("The response of MCPApi->create_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->create_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_template_request** | [**CreateTemplateRequest**](CreateTemplateRequest.md)|  | 

### Return type

[**CreateTemplate201Response**](CreateTemplate201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Template successfully created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Tier quota exceeded |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace**
> CreateDashboard201Response create_workspace(create_workspace_request)

Create a new workspace

Creates a new workspace in the current project context with a specified multi-pane layout (single, split-v, split-h, quad), optional default workspace status, and initial template view bindings to automatically generate panes.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_dashboard201_response import CreateDashboard201Response
from omnismith_sdk.models.create_workspace_request import CreateWorkspaceRequest
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    create_workspace_request = omnismith_sdk.CreateWorkspaceRequest() # CreateWorkspaceRequest | Workspace creation payload

    try:
        # Create a new workspace
        api_response = api_instance.create_workspace(create_workspace_request)
        print("The response of MCPApi->create_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->create_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workspace_request** | [**CreateWorkspaceRequest**](CreateWorkspaceRequest.md)| Workspace creation payload | 

### Return type

[**CreateDashboard201Response**](CreateDashboard201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Workspace created successfully |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace_view**
> CreateDashboardBlock201Response create_workspace_view(id, create_workspace_view_request)

Add a new view / pane to a workspace

Creates and mounts a new view pane within an existing workspace bound to a specific entity schema template, configuring presentation mode (table, grid), visible columns, filter criteria, search queries (keyword or semantic), sorting preferences, and pane order.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.create_dashboard_block201_response import CreateDashboardBlock201Response
from omnismith_sdk.models.create_workspace_view_request import CreateWorkspaceViewRequest
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Target workspace unique identifier (UUID)
    create_workspace_view_request = omnismith_sdk.CreateWorkspaceViewRequest() # CreateWorkspaceViewRequest | Workspace view creation payload

    try:
        # Add a new view / pane to a workspace
        api_response = api_instance.create_workspace_view(id, create_workspace_view_request)
        print("The response of MCPApi->create_workspace_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->create_workspace_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Target workspace unique identifier (UUID) | 
 **create_workspace_view_request** | [**CreateWorkspaceViewRequest**](CreateWorkspaceViewRequest.md)| Workspace view creation payload | 

### Return type

[**CreateDashboardBlock201Response**](CreateDashboardBlock201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Workspace view created successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the attribute to delete

    try:
        # Delete an attribute
        api_instance.delete_attribute(id)
    except Exception as e:
        print("Exception when calling MCPApi->delete_attribute: %s\n" % e)
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the Reference attribute

    try:
        # Delete reference configuration for an attribute
        api_instance.delete_attribute_reference_config(id)
    except Exception as e:
        print("Exception when calling MCPApi->delete_attribute_reference_config: %s\n" % e)
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

# **delete_automation**
> delete_automation(id)

Delete an automation

Permanently deletes an automation rule by UUID, unbinding event listeners and stopping all future evaluations and action dispatches for that rule.

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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60001') # UUID | Unique automation UUID to delete

    try:
        # Delete an automation
        api_instance.delete_automation(id)
    except Exception as e:
        print("Exception when calling MCPApi->delete_automation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique automation UUID to delete | 

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
**204** | Automation successfully deleted |  -  |
**401** | Unauthorized |  -  |
**404** | Automation not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard**
> delete_dashboard(id)

Delete a dashboard

Permanently removes a dashboard and all attached visualization blocks, metric widgets, and configurations.

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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Dashboard unique identifier (UUID) to delete

    try:
        # Delete a dashboard
        api_instance.delete_dashboard(id)
    except Exception as e:
        print("Exception when calling MCPApi->delete_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Dashboard unique identifier (UUID) to delete | 

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
**204** | Dashboard deleted successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_block**
> delete_dashboard_block(dashboard_id, block_id)

Delete a dashboard block

Permanently removes a visualization block widget from the specified dashboard canvas.

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
    api_instance = omnismith_sdk.MCPApi(api_client)
    dashboard_id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Parent dashboard unique identifier (UUID)
    block_id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6c') # UUID | Dashboard block unique identifier (UUID) to delete

    try:
        # Delete a dashboard block
        api_instance.delete_dashboard_block(dashboard_id, block_id)
    except Exception as e:
        print("Exception when calling MCPApi->delete_dashboard_block: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **UUID**| Parent dashboard unique identifier (UUID) | 
 **block_id** | **UUID**| Dashboard block unique identifier (UUID) to delete | 

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
**204** | Dashboard block deleted successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | Unique entity identifier (UUID) to soft-delete

    try:
        # Soft-delete an entity record
        api_instance.delete_entity(id)
    except Exception as e:
        print("Exception when calling MCPApi->delete_entity: %s\n" % e)
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60002') # UUID | Unique notification channel UUID to delete

    try:
        # Delete a notification channel
        api_instance.delete_notification_channel(id)
    except Exception as e:
        print("Exception when calling MCPApi->delete_notification_channel: %s\n" % e)
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

# **delete_template**
> delete_template(id)

Delete a template

Soft-deletes a template definition by UUID or slug. Soft-deleted templates are hidden from normal listings, and entity creation under deleted templates is prevented.

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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = '018b2f1b-8c1a-75b3-8000-7f0000010010' # str | UUID or unique slug of the template to delete

    try:
        # Delete a template
        api_instance.delete_template(id)
    except Exception as e:
        print("Exception when calling MCPApi->delete_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UUID or unique slug of the template to delete | 

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
**204** | Template deleted successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace**
> delete_workspace(id)

Delete a workspace and its views

Permanently removes a workspace and all nested view pane configurations from the project.

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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Workspace unique identifier (UUID) to delete

    try:
        # Delete a workspace and its views
        api_instance.delete_workspace(id)
    except Exception as e:
        print("Exception when calling MCPApi->delete_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Workspace unique identifier (UUID) to delete | 

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
**204** | Workspace deleted successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_view**
> delete_workspace_view(id, view_id)

Delete a view / pane from a workspace

Permanently removes a view pane from a workspace.

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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Workspace unique identifier (UUID)
    view_id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6c') # UUID | Workspace view unique identifier (UUID) to delete

    try:
        # Delete a view / pane from a workspace
        api_instance.delete_workspace_view(id, view_id)
    except Exception as e:
        print("Exception when calling MCPApi->delete_workspace_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Workspace unique identifier (UUID) | 
 **view_id** | **UUID**| Workspace view unique identifier (UUID) to delete | 

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
**204** | Workspace view deleted successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the attribute to fetch

    try:
        # Get an attribute by ID
        api_response = api_instance.get_attribute(id)
        print("The response of MCPApi->get_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_attribute: %s\n" % e)
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the Reference attribute

    try:
        # Get reference configuration for an attribute
        api_response = api_instance.get_attribute_reference_config(id)
        print("The response of MCPApi->get_attribute_reference_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_attribute_reference_config: %s\n" % e)
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

# **get_automation**
> AutomationResponse get_automation(id)

Get an automation by ID

Retrieves the complete configuration of a specific automation rule by its UUID, including trigger event types, template/attribute references, condition comparison expressions, action payloads, execution cooldown interval, and the timestamp of its last execution.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.automation_response import AutomationResponse
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60001') # UUID | Unique automation UUID

    try:
        # Get an automation by ID
        api_response = api_instance.get_automation(id)
        print("The response of MCPApi->get_automation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_automation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique automation UUID | 

### Return type

[**AutomationResponse**](AutomationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Automation details |  -  |
**401** | Unauthorized |  -  |
**404** | Automation not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard**
> DashboardResponse get_dashboard(id)

Get a dashboard by ID

Retrieves metadata and top-level configuration for a specific dashboard by its unique identifier.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.dashboard_response import DashboardResponse
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Dashboard unique identifier (UUID)

    try:
        # Get a dashboard by ID
        api_response = api_instance.get_dashboard(id)
        print("The response of MCPApi->get_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Dashboard unique identifier (UUID) | 

### Return type

[**DashboardResponse**](DashboardResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dashboard details |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_block**
> DashboardBlockResponse get_dashboard_block(dashboard_id, block_id)

Get a dashboard block by ID

Retrieves the configuration details, grid coordinates, and data query definitions for an individual visualization block.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.dashboard_block_response import DashboardBlockResponse
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    dashboard_id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Parent dashboard unique identifier (UUID)
    block_id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6c') # UUID | Dashboard block unique identifier (UUID)

    try:
        # Get a dashboard block by ID
        api_response = api_instance.get_dashboard_block(dashboard_id, block_id)
        print("The response of MCPApi->get_dashboard_block:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_dashboard_block: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **UUID**| Parent dashboard unique identifier (UUID) | 
 **block_id** | **UUID**| Dashboard block unique identifier (UUID) | 

### Return type

[**DashboardBlockResponse**](DashboardBlockResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dashboard block details |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | Unique entity identifier (UUID)
    attribute_key = id # str | Format for attribute_values dictionary keys: \"id\" for attribute UUIDs or \"slug\" for human-readable attribute slugs (optional) (default to id)

    try:
        # Get an entity record by ID
        api_response = api_instance.get_entity(id, attribute_key=attribute_key)
        print("The response of MCPApi->get_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_entity: %s\n" % e)
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | Unique entity identifier (UUID)
    attribute_ids = '018b2f1b-8c1a-75b3-8000-7f0000010010,018b2f1b-8c1a-75b3-8000-7f0000010011' # str | Comma-separated metric attribute UUIDs to aggregate
    start = 1774396800 # int | Start timestamp as Unix epoch in seconds
    end = 1774483200 # int | End timestamp as Unix epoch in seconds
    aggregate_func = avg # str | Aggregation function applied within each bucket (optional) (default to avg)
    bucket_width = 1 hour # str | Time bucket width interval (e.g. 1 minute, 5 minutes, 1 hour, 1 day) (optional) (default to 1 hour)

    try:
        # Get entity chart time-series data
        api_response = api_instance.get_entity_chart(id, attribute_ids, start, end, aggregate_func=aggregate_func, bucket_width=bucket_width)
        print("The response of MCPApi->get_entity_chart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_entity_chart: %s\n" % e)
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
    api_instance = omnismith_sdk.MCPApi(api_client)
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
        print("The response of MCPApi->get_entity_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_entity_history: %s\n" % e)
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

# **get_marketplace_blueprint**
> GetMarketplaceBlueprint200Response get_marketplace_blueprint(id)

Get marketplace blueprint details

Retrieves complete information for a specific marketplace blueprint by its UUID. Returns full blueprint metadata, publisher details, popularity metrics, and packaged blueprint schema definition containing template schemas, attribute configurations, and optional demo entities.

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.get_marketplace_blueprint200_response import GetMarketplaceBlueprint200Response
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60003') # UUID | Unique marketplace blueprint UUID

    try:
        # Get marketplace blueprint details
        api_response = api_instance.get_marketplace_blueprint(id)
        print("The response of MCPApi->get_marketplace_blueprint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_marketplace_blueprint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique marketplace blueprint UUID | 

### Return type

[**GetMarketplaceBlueprint200Response**](GetMarketplaceBlueprint200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Marketplace blueprint details |  -  |
**404** | Blueprint not found |  -  |

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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60002') # UUID | Unique notification channel UUID

    try:
        # Get a notification channel by ID
        api_response = api_instance.get_notification_channel(id)
        print("The response of MCPApi->get_notification_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_notification_channel: %s\n" % e)
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

# **get_project_schema**
> ProjectSchemaResponse get_project_schema()

Get complete project schema graph

Retrieves the complete consolidated schema graph for the active project in a single payload. Includes all active attributes, templates (with attribute bindings and UI layout groups), list choice items, and foreign entity reference configurations. Ideal for AI agents, client initialization, metadata caching, and schema introspection.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.project_schema_response import ProjectSchemaResponse
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
    api_instance = omnismith_sdk.MCPApi(api_client)

    try:
        # Get complete project schema graph
        api_response = api_instance.get_project_schema()
        print("The response of MCPApi->get_project_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_project_schema: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProjectSchemaResponse**](ProjectSchemaResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consolidated project schema definition |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> TemplateResponse get_template(id)

Get a template by ID or slug

Retrieves complete template schema details by UUID or unique slug, including ordered attribute bindings, default values per attribute, and visual UI layout groups. Automatically filters out any restricted attributes the caller is not permitted to view.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.template_response import TemplateResponse
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = '018b2f1b-8c1a-75b3-8000-7f0000010010' # str | UUID or unique slug of the template to retrieve

    try:
        # Get a template by ID or slug
        api_response = api_instance.get_template(id)
        print("The response of MCPApi->get_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UUID or unique slug of the template to retrieve | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template details |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_insights**
> UsageInsightsResponse get_usage_insights()

Get current tier usage insights

Returns current resource consumption vs. tier limits for the authenticated user. Includes usage counts (attributes, templates, entities, dashboards, automations, channels, monthly metric ingestions, monthly dimension updates, disk usage, AI credits), corresponding tier limits, and percentage utilization for each resource category. Use this to check quota availability before performing operations.

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
    api_instance = omnismith_sdk.MCPApi(api_client)

    try:
        # Get current tier usage insights
        api_response = api_instance.get_usage_insights()
        print("The response of MCPApi->get_usage_insights:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_usage_insights: %s\n" % e)
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

# **get_workspace**
> WorkspaceDetailsResponse get_workspace(id)

Get workspace details and its views

Retrieves detailed information for a specific workspace, including its multi-pane layout configuration and all hydrated view panes with their associated template schemas, filter rules, search criteria, column selections, and ordering.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.workspace_details_response import WorkspaceDetailsResponse
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Workspace unique identifier (UUID)

    try:
        # Get workspace details and its views
        api_response = api_instance.get_workspace(id)
        print("The response of MCPApi->get_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Workspace unique identifier (UUID) | 

### Return type

[**WorkspaceDetailsResponse**](WorkspaceDetailsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace details with hydrated views |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_view**
> WorkspaceViewResponse get_workspace_view(id, view_id)

Get details of a workspace view / pane

Retrieves complete configuration details for a single workspace view pane, including its schema template binding, active filter rules, search parameters, column visibility, sort order, and layout positioning.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.workspace_view_response import WorkspaceViewResponse
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Workspace unique identifier (UUID)
    view_id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6c') # UUID | Workspace view unique identifier (UUID)

    try:
        # Get details of a workspace view / pane
        api_response = api_instance.get_workspace_view(id, view_id)
        print("The response of MCPApi->get_workspace_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_workspace_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Workspace unique identifier (UUID) | 
 **view_id** | **UUID**| Workspace view unique identifier (UUID) | 

### Return type

[**WorkspaceViewResponse**](WorkspaceViewResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace view details |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | Unique entity identifier (UUID)
    ingest_metrics_request = omnismith_sdk.IngestMetricsRequest() # IngestMetricsRequest | 

    try:
        # Ingest high-frequency metric observations for an entity
        api_instance.ingest_entity_metrics(id, ingest_metrics_request)
    except Exception as e:
        print("Exception when calling MCPApi->ingest_entity_metrics: %s\n" % e)
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

# **install_marketplace_blueprint**
> install_marketplace_blueprint(id, install_marketplace_blueprint_request)

Install a marketplace blueprint into a project

Installs a marketplace blueprint into the specified project context. Provisions all packaged templates, attributes, and relationships defined in the blueprint schema, and optionally populates sample demo entities. Automatically increments the installation count for the blueprint.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.install_marketplace_blueprint_request import InstallMarketplaceBlueprintRequest
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60003') # UUID | Unique UUID of the blueprint to install
    install_marketplace_blueprint_request = omnismith_sdk.InstallMarketplaceBlueprintRequest() # InstallMarketplaceBlueprintRequest | 

    try:
        # Install a marketplace blueprint into a project
        api_instance.install_marketplace_blueprint(id, install_marketplace_blueprint_request)
    except Exception as e:
        print("Exception when calling MCPApi->install_marketplace_blueprint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique UUID of the blueprint to install | 
 **install_marketplace_blueprint_request** | [**InstallMarketplaceBlueprintRequest**](InstallMarketplaceBlueprintRequest.md)|  | 

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
**204** | Blueprint successfully installed into the target project |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - Insufficient project permissions |  -  |
**404** | Blueprint not found |  -  |
**422** | Validation Error |  -  |

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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the List-type attribute

    try:
        # List items of an attribute
        api_response = api_instance.list_attribute_items(id)
        print("The response of MCPApi->list_attribute_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->list_attribute_items: %s\n" % e)
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
    api_instance = omnismith_sdk.MCPApi(api_client)

    try:
        # List all attributes
        api_response = api_instance.list_attributes()
        print("The response of MCPApi->list_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->list_attributes: %s\n" % e)
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
    api_instance = omnismith_sdk.MCPApi(api_client)
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
        print("The response of MCPApi->list_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->list_audit_logs: %s\n" % e)
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

# **list_automations**
> List[AutomationResponse] list_automations(template_id=template_id, is_enabled=is_enabled)

List project automations

Retrieves all automation rules configured within the current project context. Automations define event-driven workflows triggered by entity lifecycle events (such as entity creation, attribute updates, or metric threshold changes), evaluated against multi-attribute conditions, and dispatched to configured action channels (Telegram, webhooks, mobile push). Results can be filtered by entity template or active status.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.automation_response import AutomationResponse
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    template_id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60088') # UUID | Filter automations scoped to a specific entity template UUID (optional)
    is_enabled = true # bool | Filter automations by active enabled status (true for active rules, false for paused rules) (optional)

    try:
        # List project automations
        api_response = api_instance.list_automations(template_id=template_id, is_enabled=is_enabled)
        print("The response of MCPApi->list_automations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->list_automations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **UUID**| Filter automations scoped to a specific entity template UUID | [optional] 
 **is_enabled** | **bool**| Filter automations by active enabled status (true for active rules, false for paused rules) | [optional] 

### Return type

[**List[AutomationResponse]**](AutomationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of automation rules |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dashboard_blocks**
> ListDashboardBlocks200Response list_dashboard_blocks(dashboard_id)

List all blocks in a dashboard

Retrieves all visualization blocks mounted on a dashboard canvas, including widget types (stat KPI card, time-series chart, gauge meter, entity list), grid position coordinates (x, y, cols, rows), template filters, and aggregation configs.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_dashboard_blocks200_response import ListDashboardBlocks200Response
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    dashboard_id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Parent dashboard unique identifier (UUID)

    try:
        # List all blocks in a dashboard
        api_response = api_instance.list_dashboard_blocks(dashboard_id)
        print("The response of MCPApi->list_dashboard_blocks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->list_dashboard_blocks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **UUID**| Parent dashboard unique identifier (UUID) | 

### Return type

[**ListDashboardBlocks200Response**](ListDashboardBlocks200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of dashboard blocks |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dashboards**
> ListDashboards200Response list_dashboards()

List all dashboards

Retrieves all analytics dashboards configured within the authenticated project context, including dashboard metadata, layout settings, and visualization configurations.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_dashboards200_response import ListDashboards200Response
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
    api_instance = omnismith_sdk.MCPApi(api_client)

    try:
        # List all dashboards
        api_response = api_instance.list_dashboards()
        print("The response of MCPApi->list_dashboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->list_dashboards: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListDashboards200Response**](ListDashboards200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of dashboards |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

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
    api_instance = omnismith_sdk.MCPApi(api_client)

    try:
        # List notification channels
        api_response = api_instance.list_notification_channels()
        print("The response of MCPApi->list_notification_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->list_notification_channels: %s\n" % e)
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

# **list_template_entity_counts**
> ListTemplateEntityCounts200Response list_template_entity_counts()

List entity counts per template

Returns total entity record counts grouped by template UUID for all accessible templates in the current project context. Efficiently calculates counts and honors role-based resource access restrictions.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_template_entity_counts200_response import ListTemplateEntityCounts200Response
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
    api_instance = omnismith_sdk.MCPApi(api_client)

    try:
        # List entity counts per template
        api_response = api_instance.list_template_entity_counts()
        print("The response of MCPApi->list_template_entity_counts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->list_template_entity_counts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListTemplateEntityCounts200Response**](ListTemplateEntityCounts200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entity counts per template |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates**
> ListTemplates200Response list_templates()

List all templates

Retrieves all dynamic schema templates defined within the active project context. Templates represent content types grouping reusable attributes, establishing per-template default values, and organizing fields into visual layout groups for the UI workbench and entity forms.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_templates200_response import ListTemplates200Response
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
    api_instance = omnismith_sdk.MCPApi(api_client)

    try:
        # List all templates
        api_response = api_instance.list_templates()
        print("The response of MCPApi->list_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->list_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListTemplates200Response**](ListTemplates200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all project templates |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspaces**
> ListWorkspaces200Response list_workspaces()

List all workspaces for current project

Retrieves all workspaces configured within the authenticated project context, including multi-pane layout structures (single, split-v, split-h, quad), view pane counts, sort ordering, and default workspace indicators for workbench navigation.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.list_workspaces200_response import ListWorkspaces200Response
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
    api_instance = omnismith_sdk.MCPApi(api_client)

    try:
        # List all workspaces for current project
        api_response = api_instance.list_workspaces()
        print("The response of MCPApi->list_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->list_workspaces: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListWorkspaces200Response**](ListWorkspaces200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of workspaces |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the attribute to patch
    patch_attribute_request = omnismith_sdk.PatchAttributeRequest() # PatchAttributeRequest | 

    try:
        # Patch an attribute (granular partial update)
        api_instance.patch_attribute(id, patch_attribute_request)
    except Exception as e:
        print("Exception when calling MCPApi->patch_attribute: %s\n" % e)
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

# **patch_template**
> patch_template(id, patch_template_request)

Patch a template (granular partial update)

Applies partial modifications to an existing template by UUID or slug without overwriting omitted fields. Allows modifying name, description, category, slug, attribute associations (with validated default values), or visual layout groups independently. Safely merges and preserves any restricted attributes.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.patch_template_request import PatchTemplateRequest
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = '018b2f1b-8c1a-75b3-8000-7f0000010010' # str | UUID or unique slug of the template to patch
    patch_template_request = omnismith_sdk.PatchTemplateRequest() # PatchTemplateRequest | 

    try:
        # Patch a template (granular partial update)
        api_instance.patch_template(id, patch_template_request)
    except Exception as e:
        print("Exception when calling MCPApi->patch_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UUID or unique slug of the template to patch | 
 **patch_template_request** | [**PatchTemplateRequest**](PatchTemplateRequest.md)|  | 

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
**204** | Template patched successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_dashboard_block**
> ResolvedBlockResponse resolve_dashboard_block(dashboard_id, block_id)

Resolve a dashboard block to its computed data

Executes the underlying data query for a dashboard block and returns computed real-time aggregated metrics and time-series telemetry. Returns a typed payload matching the block type: stat (matching entity count), gauge (current metric value, min/max bounds, progress percentage), chart (time-series data point series bucketed by time intervals with aggregation functions), or list (hydrated entity items with dynamic attributes).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.resolved_block_response import ResolvedBlockResponse
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    dashboard_id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Parent dashboard unique identifier (UUID)
    block_id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6c') # UUID | Dashboard block unique identifier (UUID) to resolve and compute

    try:
        # Resolve a dashboard block to its computed data
        api_response = api_instance.resolve_dashboard_block(dashboard_id, block_id)
        print("The response of MCPApi->resolve_dashboard_block:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->resolve_dashboard_block: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **UUID**| Parent dashboard unique identifier (UUID) | 
 **block_id** | **UUID**| Dashboard block unique identifier (UUID) to resolve and compute | 

### Return type

[**ResolvedBlockResponse**](ResolvedBlockResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resolved block computed data payload |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

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
    api_instance = omnismith_sdk.MCPApi(api_client)
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
        print("The response of MCPApi->search_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->search_entities: %s\n" % e)
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

# **search_marketplace_blueprints**
> SearchMarketplaceBlueprints200Response search_marketplace_blueprints(search=search, keywords=keywords, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, featured=featured)

Search marketplace blueprints

Searches and lists public blueprints available in the marketplace catalog. Blueprints package reusable template schemas, attribute definitions, and sample data that users can install directly into their projects. Supports full-text search across titles and descriptions, keyword tag filtering, filtering by featured status, and sorting by creation date, install counts, or title.

### Example


```python
import omnismith_sdk
from omnismith_sdk.models.search_marketplace_blueprints200_response import SearchMarketplaceBlueprints200Response
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    search = 'crm pipeline' # str | Free-text search filter across blueprint title and description (optional)
    keywords = 'crm,sales,leads' # str | Comma-separated keywords or tags to filter blueprints (optional)
    limit = 20 # int | Number of blueprint records to return per page (max 100) (optional) (default to 20)
    offset = 0 # int | Number of blueprint records to skip for pagination (optional) (default to 0)
    sort_by = created_at # str | Field to sort blueprint results by (optional) (default to created_at)
    sort_direction = desc # str | Sort direction order (ascending or descending) (optional) (default to desc)
    featured = true # bool | Filter to return only curated and featured marketplace blueprints (optional)

    try:
        # Search marketplace blueprints
        api_response = api_instance.search_marketplace_blueprints(search=search, keywords=keywords, limit=limit, offset=offset, sort_by=sort_by, sort_direction=sort_direction, featured=featured)
        print("The response of MCPApi->search_marketplace_blueprints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->search_marketplace_blueprints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Free-text search filter across blueprint title and description | [optional] 
 **keywords** | **str**| Comma-separated keywords or tags to filter blueprints | [optional] 
 **limit** | **int**| Number of blueprint records to return per page (max 100) | [optional] [default to 20]
 **offset** | **int**| Number of blueprint records to skip for pagination | [optional] [default to 0]
 **sort_by** | **str**| Field to sort blueprint results by | [optional] [default to created_at]
 **sort_direction** | **str**| Sort direction order (ascending or descending) | [optional] [default to desc]
 **featured** | **bool**| Filter to return only curated and featured marketplace blueprints | [optional] 

### Return type

[**SearchMarketplaceBlueprints200Response**](SearchMarketplaceBlueprints200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of marketplace blueprints |  -  |

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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the List-type attribute
    set_list_items_request = omnismith_sdk.SetListItemsRequest() # SetListItemsRequest | 

    try:
        # Set list items for an attribute (replaces all existing items)
        api_instance.set_attribute_items(id, set_list_items_request)
    except Exception as e:
        print("Exception when calling MCPApi->set_attribute_items: %s\n" % e)
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the Reference attribute
    set_reference_config_request = omnismith_sdk.SetReferenceConfigRequest() # SetReferenceConfigRequest | 

    try:
        # Set or update reference configuration for an attribute
        api_instance.set_attribute_reference_config(id, set_reference_config_request)
    except Exception as e:
        print("Exception when calling MCPApi->set_attribute_reference_config: %s\n" % e)
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60002') # UUID | Unique notification channel UUID to test
    test_notification_channel_request = omnismith_sdk.TestNotificationChannelRequest() # TestNotificationChannelRequest | 

    try:
        # Send a test notification message
        api_response = api_instance.test_notification_channel(id, test_notification_channel_request)
        print("The response of MCPApi->test_notification_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->test_notification_channel: %s\n" % e)
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

# **toggle_automation**
> AutomationResponse toggle_automation(id, toggle_automation_request)

Toggle automation enabled status

Enables or pauses an automation rule without altering its trigger definitions, condition criteria, or action configurations. Paused automations are ignored during event processing.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.automation_response import AutomationResponse
from omnismith_sdk.models.toggle_automation_request import ToggleAutomationRequest
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60001') # UUID | Unique automation UUID to toggle
    toggle_automation_request = omnismith_sdk.ToggleAutomationRequest() # ToggleAutomationRequest | 

    try:
        # Toggle automation enabled status
        api_response = api_instance.toggle_automation(id, toggle_automation_request)
        print("The response of MCPApi->toggle_automation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->toggle_automation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique automation UUID to toggle | 
 **toggle_automation_request** | [**ToggleAutomationRequest**](ToggleAutomationRequest.md)|  | 

### Return type

[**AutomationResponse**](AutomationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Automation status successfully toggled |  -  |
**400** | Bad Request |  -  |
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | UUID of the attribute to update
    update_attribute_request = omnismith_sdk.UpdateAttributeRequest() # UpdateAttributeRequest | 

    try:
        # Update an attribute (full replacement)
        api_instance.update_attribute(id, update_attribute_request)
    except Exception as e:
        print("Exception when calling MCPApi->update_attribute: %s\n" % e)
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

# **update_automation**
> update_automation(id, update_automation_request)

Update an automation

Updates an existing automation rule by UUID. Supports modifying rule name, description, trigger event definitions, condition filter criteria, action dispatches, and cooldown throttle settings.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.update_automation_request import UpdateAutomationRequest
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60001') # UUID | Unique automation UUID to update
    update_automation_request = omnismith_sdk.UpdateAutomationRequest() # UpdateAutomationRequest | 

    try:
        # Update an automation
        api_instance.update_automation(id, update_automation_request)
    except Exception as e:
        print("Exception when calling MCPApi->update_automation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique automation UUID to update | 
 **update_automation_request** | [**UpdateAutomationRequest**](UpdateAutomationRequest.md)|  | 

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
**204** | Automation successfully updated |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Automation not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard**
> update_dashboard(id, update_dashboard_request)

Update a dashboard

Updates dashboard metadata including its display name, description, and canvas layout settings.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.update_dashboard_request import UpdateDashboardRequest
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Dashboard unique identifier (UUID) to update
    update_dashboard_request = omnismith_sdk.UpdateDashboardRequest() # UpdateDashboardRequest | Dashboard update payload

    try:
        # Update a dashboard
        api_instance.update_dashboard(id, update_dashboard_request)
    except Exception as e:
        print("Exception when calling MCPApi->update_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Dashboard unique identifier (UUID) to update | 
 **update_dashboard_request** | [**UpdateDashboardRequest**](UpdateDashboardRequest.md)| Dashboard update payload | 

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
**204** | Dashboard updated successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard_block**
> update_dashboard_block(dashboard_id, block_id, update_dashboard_block_request)

Update a dashboard block

Updates the display title, grid placement (x, y, cols, rows), metric queries, time-series aggregation buckets, gauge bounds, or filtering rules of an existing visualization block.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.update_dashboard_block_request import UpdateDashboardBlockRequest
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    dashboard_id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Parent dashboard unique identifier (UUID)
    block_id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6c') # UUID | Dashboard block unique identifier (UUID) to update
    update_dashboard_block_request = omnismith_sdk.UpdateDashboardBlockRequest() # UpdateDashboardBlockRequest | Dashboard block update payload

    try:
        # Update a dashboard block
        api_instance.update_dashboard_block(dashboard_id, block_id, update_dashboard_block_request)
    except Exception as e:
        print("Exception when calling MCPApi->update_dashboard_block: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **UUID**| Parent dashboard unique identifier (UUID) | 
 **block_id** | **UUID**| Dashboard block unique identifier (UUID) to update | 
 **update_dashboard_block_request** | [**UpdateDashboardBlockRequest**](UpdateDashboardBlockRequest.md)| Dashboard block update payload | 

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
**204** | Dashboard block updated successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | Unique entity identifier (UUID)
    update_entity_request = omnismith_sdk.UpdateEntityRequest() # UpdateEntityRequest | 

    try:
        # Update entity attribute values
        api_instance.update_entity(id, update_entity_request)
    except Exception as e:
        print("Exception when calling MCPApi->update_entity: %s\n" % e)
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('01912ecb-4654-7890-a1b2-c3d4e5f60002') # UUID | Unique notification channel UUID to update
    update_notification_channel_request = omnismith_sdk.UpdateNotificationChannelRequest() # UpdateNotificationChannelRequest | 

    try:
        # Update a notification channel
        api_instance.update_notification_channel(id, update_notification_channel_request)
    except Exception as e:
        print("Exception when calling MCPApi->update_notification_channel: %s\n" % e)
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

# **update_template**
> update_template(id, update_template_request)

Update a template (full replacement)

Performs a full update of an existing template definition by UUID or slug. Replaces name, description, category, slug, attribute associations (with validated per-attribute default values), and UI layout groups. If the caller lacks permissions to certain restricted attributes, those restricted attributes are automatically preserved in the template.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.update_template_request import UpdateTemplateRequest
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = '018b2f1b-8c1a-75b3-8000-7f0000010010' # str | UUID or unique slug of the template to update
    update_template_request = omnismith_sdk.UpdateTemplateRequest() # UpdateTemplateRequest | 

    try:
        # Update a template (full replacement)
        api_instance.update_template(id, update_template_request)
    except Exception as e:
        print("Exception when calling MCPApi->update_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UUID or unique slug of the template to update | 
 **update_template_request** | [**UpdateTemplateRequest**](UpdateTemplateRequest.md)|  | 

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
**204** | Template updated successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace**
> update_workspace(id, update_workspace_request)

Update workspace metadata and layout

Updates workspace attributes including display name, description, multi-pane layout arrangement (single, split-v, split-h, quad), sort order sequence, and default workspace status.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.update_workspace_request import UpdateWorkspaceRequest
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Workspace unique identifier (UUID) to update
    update_workspace_request = omnismith_sdk.UpdateWorkspaceRequest() # UpdateWorkspaceRequest | Workspace update payload

    try:
        # Update workspace metadata and layout
        api_instance.update_workspace(id, update_workspace_request)
    except Exception as e:
        print("Exception when calling MCPApi->update_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Workspace unique identifier (UUID) to update | 
 **update_workspace_request** | [**UpdateWorkspaceRequest**](UpdateWorkspaceRequest.md)| Workspace update payload | 

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
**204** | Workspace updated successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace_view**
> update_workspace_view(id, view_id, update_workspace_view_request)

Update workspace view / pane filters, sort, display mode, or columns

Updates the configuration of a specific workspace view pane, modifying its title, filtering rules, search query and mode, sorting preferences, presentation display mode (table or grid), column visibility lists, or pane display sequence.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.update_workspace_view_request import UpdateWorkspaceViewRequest
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
    api_instance = omnismith_sdk.MCPApi(api_client)
    id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6b') # UUID | Workspace unique identifier (UUID)
    view_id = UUID('0190a1b2-c3d4-7e8f-9a0b-1c2d3e4f5a6c') # UUID | Workspace view unique identifier (UUID) to update
    update_workspace_view_request = omnismith_sdk.UpdateWorkspaceViewRequest() # UpdateWorkspaceViewRequest | Workspace view update payload

    try:
        # Update workspace view / pane filters, sort, display mode, or columns
        api_instance.update_workspace_view(id, view_id, update_workspace_view_request)
    except Exception as e:
        print("Exception when calling MCPApi->update_workspace_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Workspace unique identifier (UUID) | 
 **view_id** | **UUID**| Workspace view unique identifier (UUID) to update | 
 **update_workspace_view_request** | [**UpdateWorkspaceViewRequest**](UpdateWorkspaceViewRequest.md)| Workspace view update payload | 

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
**204** | Workspace view updated successfully |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

