# PMCore.Client.FileApi

All URIs are relative to *https://your.apiserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_create_folder**](FileApi.md#file_create_folder) | **POST** /File/{appKey}/CreateFolder | 创建文件夹
[**file_delete**](FileApi.md#file_delete) | **DELETE** /File/{appKey} | 删除文件
[**file_rename**](FileApi.md#file_rename) | **POST** /File/{appKey}/Rename | 重命名文件
[**file_upload**](FileApi.md#file_upload) | **POST** /File/{appKey}/Upload | 上传文件
[**files**](FileApi.md#files) | **GET** /File/{appKey} | 文件列表


# **file_create_folder**
> JObjectApiResult file_create_folder(app_key, path=path)

创建文件夹

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your.apiserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://your.apiserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.FileApi(api_client)
    app_key = 'app_key_example' # str | 
    path = 'path_example' # str |  (optional)

    try:
        # 创建文件夹
        api_response = api_instance.file_create_folder(app_key, path=path)
        print("The response of FileApi->file_create_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->file_create_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **path** | **str**|  | [optional] 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_delete**
> JObjectApiResult file_delete(app_key, path=path)

删除文件

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your.apiserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://your.apiserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.FileApi(api_client)
    app_key = 'app_key_example' # str | 
    path = 'path_example' # str | 文件路径 (optional)

    try:
        # 删除文件
        api_response = api_instance.file_delete(app_key, path=path)
        print("The response of FileApi->file_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->file_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **path** | **str**| 文件路径 | [optional] 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_rename**
> JObjectApiResult file_rename(app_key, source_name=source_name, dest_name=dest_name)

重命名文件

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your.apiserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://your.apiserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.FileApi(api_client)
    app_key = 'app_key_example' # str | 
    source_name = 'source_name_example' # str |  (optional)
    dest_name = 'dest_name_example' # str |  (optional)

    try:
        # 重命名文件
        api_response = api_instance.file_rename(app_key, source_name=source_name, dest_name=dest_name)
        print("The response of FileApi->file_rename:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->file_rename: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **source_name** | **str**|  | [optional] 
 **dest_name** | **str**|  | [optional] 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_upload**
> JObjectApiResult file_upload(app_key, path=path, file=file)

上传文件

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your.apiserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://your.apiserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.FileApi(api_client)
    app_key = 'app_key_example' # str | 
    path = 'path_example' # str | 文件夹路径 (optional)
    file = None # bytearray | 上传的文件 (optional)

    try:
        # 上传文件
        api_response = api_instance.file_upload(app_key, path=path, file=file)
        print("The response of FileApi->file_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->file_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **path** | **str**| 文件夹路径 | [optional] 
 **file** | **bytearray**| 上传的文件 | [optional] 

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files**
> JObjectApiResult files(app_key, path=path, skip=skip, take=take)

文件列表

### Example

* Bearer Authentication (Bearer):

```python
import PMCore.Client
from PMCore.Client.models.j_object_api_result import JObjectApiResult
from PMCore.Client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your.apiserver.com
# See configuration.py for a list of all supported configuration parameters.
configuration = PMCore.Client.Configuration(
    host = "https://your.apiserver.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = PMCore.Client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with PMCore.Client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = PMCore.Client.FileApi(api_client)
    app_key = 'app_key_example' # str | 
    path = 'path_example' # str |  (optional)
    skip = 0 # int |  (optional) (default to 0)
    take = 100 # int |  (optional) (default to 100)

    try:
        # 文件列表
        api_response = api_instance.files(app_key, path=path, skip=skip, take=take)
        print("The response of FileApi->files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_key** | **str**|  | 
 **path** | **str**|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **take** | **int**|  | [optional] [default to 100]

### Return type

[**JObjectApiResult**](JObjectApiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

