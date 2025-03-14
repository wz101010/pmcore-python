# JObjectApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | 业务状态码 | [optional] [default to 200]
**err** | **str** | 错误消息 | [optional] [default to '']
**data** | **Dict[str, List[object]]** | 业务数据 | [optional] 

## Example

```python
from PMCore.Client.models.j_object_api_result import JObjectApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of JObjectApiResult from a JSON string
j_object_api_result_instance = JObjectApiResult.from_json(json)
# print the JSON string representation of the object
print(JObjectApiResult.to_json())

# convert the object into a dict
j_object_api_result_dict = j_object_api_result_instance.to_dict()
# create an instance of JObjectApiResult from a dict
j_object_api_result_from_dict = JObjectApiResult.from_dict(j_object_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


