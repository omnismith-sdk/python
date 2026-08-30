# omnismith_sdk.FileAttachmentApi

All URIs are relative to *https://api.omnismith.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file_attachment**](FileAttachmentApi.md#delete_file_attachment) | **DELETE** /file-attachments/{id} | Delete a file attachment
[**download_file_attachment**](FileAttachmentApi.md#download_file_attachment) | **GET** /file-attachments/{id} | Download a file attachment
[**get_file_attachment_metadata**](FileAttachmentApi.md#get_file_attachment_metadata) | **GET** /file-attachments/{id}/metadata | Get file metadata without downloading content
[**get_file_attachment_thumbnail**](FileAttachmentApi.md#get_file_attachment_thumbnail) | **GET** /file-attachments/{id}/thumbnail | Get image thumbnail
[**upload_file_attachment**](FileAttachmentApi.md#upload_file_attachment) | **POST** /file-attachments | Upload a file attachment


# **delete_file_attachment**
> delete_file_attachment(id)

Delete a file attachment

Permanently deletes a file attachment and its stored content from disk. If the file is referenced by entity attribute values (file or image data type), those references will become stale. Returns 204 on success.

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
    api_instance = omnismith_sdk.FileAttachmentApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | File attachment UUID to delete

    try:
        # Delete a file attachment
        api_instance.delete_file_attachment(id)
    except Exception as e:
        print("Exception when calling FileAttachmentApi->delete_file_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| File attachment UUID to delete | 

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
**204** | File deleted |  -  |
**404** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file_attachment**
> download_file_attachment(id)

Download a file attachment

Returns the raw binary file content for a given file attachment ID. The response Content-Type header matches the original uploaded file MIME type. The file must belong to the authenticated user's project.

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
    api_instance = omnismith_sdk.FileAttachmentApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | Unique UUID identifier of the file attachment to download

    try:
        # Download a file attachment
        api_instance.download_file_attachment(id)
    except Exception as e:
        print("Exception when calling FileAttachmentApi->download_file_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique UUID identifier of the file attachment to download | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File content |  -  |
**404** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_attachment_metadata**
> FileAttachmentResponse get_file_attachment_metadata(id)

Get file metadata without downloading content

Returns metadata for a file attachment (original filename, MIME type, file size in bytes, upload timestamp, context) without streaming the binary content. Use this to inspect file properties before deciding whether to download.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.file_attachment_response import FileAttachmentResponse
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
    api_instance = omnismith_sdk.FileAttachmentApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | Unique UUID identifier of the file attachment

    try:
        # Get file metadata without downloading content
        api_response = api_instance.get_file_attachment_metadata(id)
        print("The response of FileAttachmentApi->get_file_attachment_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileAttachmentApi->get_file_attachment_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique UUID identifier of the file attachment | 

### Return type

[**FileAttachmentResponse**](FileAttachmentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File metadata |  -  |
**404** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_attachment_thumbnail**
> get_file_attachment_thumbnail(id, width=width, height=height)

Get image thumbnail

Generates and returns a resized thumbnail for image-type file attachments (JPEG, PNG, WebP, GIF). Optional `width` and `height` query parameters control output dimensions (range 50–1000px, default 200×200). Returns 400 if the file is not an image type. The thumbnail is returned as JPEG binary.

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
    api_instance = omnismith_sdk.FileAttachmentApi(api_client)
    id = UUID('018b2f1b-8c1a-75b3-8000-7f0000010000') # UUID | Unique UUID identifier of the image file attachment
    width = 200 # int | Target thumbnail width in pixels (range 50 to 1000, default 200) (optional) (default to 200)
    height = 200 # int | Target thumbnail height in pixels (range 50 to 1000, default 200) (optional) (default to 200)

    try:
        # Get image thumbnail
        api_instance.get_file_attachment_thumbnail(id, width=width, height=height)
    except Exception as e:
        print("Exception when calling FileAttachmentApi->get_file_attachment_thumbnail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| Unique UUID identifier of the image file attachment | 
 **width** | **int**| Target thumbnail width in pixels (range 50 to 1000, default 200) | [optional] [default to 200]
 **height** | **int**| Target thumbnail height in pixels (range 50 to 1000, default 200) | [optional] [default to 200]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Thumbnail image |  -  |
**400** | Not an image or invalid dimensions |  -  |
**404** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_attachment**
> FileAttachmentResponse upload_file_attachment(file, id=id, context=context, ttl_hours=ttl_hours)

Upload a file attachment

Uploads a file as a multipart/form-data request. Supported MIME types include images (JPEG, PNG, WebP, GIF, SVG), documents (PDF), spreadsheets (CSV, XLSX), and structured data (JSON, YAML). An optional pre-generated UUIDv7 `id` can be supplied; otherwise the server generates one. The `context` field controls storage lifecycle: "entity" files are permanent, "chat" files are temporary with configurable `ttl_hours` (default 48h). Returns the file metadata including the assigned ID for use in entity attribute values.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import omnismith_sdk
from omnismith_sdk.models.file_attachment_response import FileAttachmentResponse
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
    api_instance = omnismith_sdk.FileAttachmentApi(api_client)
    file = None # bytes | 
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    context = entity # str |  (optional) (default to entity)
    ttl_hours = 56 # int |  (optional)

    try:
        # Upload a file attachment
        api_response = api_instance.upload_file_attachment(file, id=id, context=context, ttl_hours=ttl_hours)
        print("The response of FileAttachmentApi->upload_file_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileAttachmentApi->upload_file_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytes**|  | 
 **id** | **UUID**|  | [optional] 
 **context** | **str**|  | [optional] [default to entity]
 **ttl_hours** | **int**|  | [optional] 

### Return type

[**FileAttachmentResponse**](FileAttachmentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | File uploaded |  -  |
**400** | Bad request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

