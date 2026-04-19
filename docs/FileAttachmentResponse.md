# FileAttachmentResponse

File attachment details after upload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**original_filename** | **str** |  | [optional] 
**mime_type** | **str** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from omnismith_sdk.models.file_attachment_response import FileAttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FileAttachmentResponse from a JSON string
file_attachment_response_instance = FileAttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(FileAttachmentResponse.to_json())

# convert the object into a dict
file_attachment_response_dict = file_attachment_response_instance.to_dict()
# create an instance of FileAttachmentResponse from a dict
file_attachment_response_from_dict = FileAttachmentResponse.from_dict(file_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


