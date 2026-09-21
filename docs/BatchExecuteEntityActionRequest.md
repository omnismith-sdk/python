# BatchExecuteEntityActionRequest

The records to run the action on and the values for its fields, shared by every record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_ids** | **List[UUID]** | Distinct entity identifiers, at most 100 per call. Every record must belong to a template that defines the action. | 
**values** | [**Dict[str, EntityAttributesInputValue]**](EntityAttributesInputValue.md) | Map of attribute slug or UUID → value. Keys may be mixed freely in one request; each attribute may appear once.  ### Values - **Plain scalar** — &#x60;\&quot;text\&quot;&#x60;, &#x60;42&#x60;, &#x60;129.99&#x60;, &#x60;true&#x60;, or &#x60;null&#x60;. Numbers and booleans are serialized for you (&#x60;42&#x60; → &#x60;\&quot;42\&quot;&#x60;, &#x60;true&#x60; → &#x60;\&quot;true\&quot;&#x60;); floats keep exactly the digits you sent. - **&#x60;null&#x60;** — clears the attribute. - **Backfill object** — &#x60;{ \&quot;value\&quot;: &lt;scalar|null&gt;, \&quot;updated_at\&quot;: \&quot;2026-09-12T12:23:52Z\&quot; }&#x60; records the value as observed at that moment (history import). &#x60;updated_at&#x60; must be RFC 3339 with an explicit offset (&#x60;Z&#x60; or &#x60;±HH:MM&#x60;); it defaults to now when omitted. - **Operation object** — &#x60;{ \&quot;op\&quot;: \&quot;increment\&quot;, \&quot;value\&quot;: 1 }&#x60; adds the number to the stored value instead of overwriting it: you never need to read the current value, and concurrent increments are serialized so none is lost. Allowed on **Number** attributes and **Metrics** only (a metric increment appends &#x60;latest + value&#x60; as a new observation); a never-set attribute counts as &#x60;0&#x60;; a negative &#x60;value&#x60; subtracts. &#x60;op&#x60; cannot be combined with &#x60;updated_at&#x60;. Not accepted on create. The change log records the resolved value, never the operand.  ### Value format by attribute type - **Text / Markdown**: UTF-8 string - **Number**: number or numeric string (&#x60;129.99&#x60;, &#x60;\&quot;42\&quot;&#x60;) - **Boolean**: &#x60;true&#x60; / &#x60;false&#x60; (or &#x60;\&quot;true\&quot;&#x60; / &#x60;\&quot;false\&quot;&#x60;, &#x60;\&quot;1\&quot;&#x60; / &#x60;\&quot;0\&quot;&#x60;) - **Date**: &#x60;YYYY-MM-DD&#x60;; **Datetime**: &#x60;YYYY-MM-DD HH:MM:SS&#x60; or ISO 8601 &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; - **File / Image**: UUID of a previously uploaded file asset - **List**: UUID of one of the attribute&#39;s list items - **Reference**: UUID of the referenced entity - **Metric**: numeric observation; appended to the time series (never overwritten)  ### Example &#x60;&#x60;&#x60;json {   \&quot;hostname\&quot;: \&quot;edge-fra-01\&quot;,   \&quot;cpu_cores\&quot;: 8,   \&quot;notes\&quot;: null,   \&quot;operational_status\&quot;: { \&quot;value\&quot;: \&quot;Active\&quot;, \&quot;updated_at\&quot;: \&quot;2026-09-12T12:23:52Z\&quot; },   \&quot;restart_count\&quot;: { \&quot;op\&quot;: \&quot;increment\&quot;, \&quot;value\&quot;: 1 } } &#x60;&#x60;&#x60; | [optional] 
**atomic** | **bool** | When false (the default) every record is attempted and its outcome reported. When true the batch runs in one transaction and the first record that does not execute rolls all of it back. | [optional] [default to False]

## Example

```python
from omnismith_sdk.models.batch_execute_entity_action_request import BatchExecuteEntityActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchExecuteEntityActionRequest from a JSON string
batch_execute_entity_action_request_instance = BatchExecuteEntityActionRequest.from_json(json)
# print the JSON string representation of the object
print(BatchExecuteEntityActionRequest.to_json())

# convert the object into a dict
batch_execute_entity_action_request_dict = batch_execute_entity_action_request_instance.to_dict()
# create an instance of BatchExecuteEntityActionRequest from a dict
batch_execute_entity_action_request_from_dict = BatchExecuteEntityActionRequest.from_dict(batch_execute_entity_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


