# isi_sdk_8_0_1.StatisticsApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statistics_current**](StatisticsApi.md#get_statistics_current) | **GET** /platform/1/statistics/current | 
[**get_statistics_history**](StatisticsApi.md#get_statistics_history) | **GET** /platform/1/statistics/history | 
[**get_statistics_key**](StatisticsApi.md#get_statistics_key) | **GET** /platform/1/statistics/keys/{StatisticsKeyId} | 
[**get_statistics_keys**](StatisticsApi.md#get_statistics_keys) | **GET** /platform/1/statistics/keys | 
[**get_statistics_operations**](StatisticsApi.md#get_statistics_operations) | **GET** /platform/3/statistics/operations | 
[**get_statistics_protocols**](StatisticsApi.md#get_statistics_protocols) | **GET** /platform/1/statistics/protocols | 
[**get_summary_client**](StatisticsApi.md#get_summary_client) | **GET** /platform/3/statistics/summary/client | 
[**get_summary_drive**](StatisticsApi.md#get_summary_drive) | **GET** /platform/3/statistics/summary/drive | 
[**get_summary_heat**](StatisticsApi.md#get_summary_heat) | **GET** /platform/3/statistics/summary/heat | 
[**get_summary_protocol**](StatisticsApi.md#get_summary_protocol) | **GET** /platform/3/statistics/summary/protocol | 
[**get_summary_protocol_stats**](StatisticsApi.md#get_summary_protocol_stats) | **GET** /platform/3/statistics/summary/protocol-stats | 
[**get_summary_system**](StatisticsApi.md#get_summary_system) | **GET** /platform/3/statistics/summary/system | 
[**get_summary_workload**](StatisticsApi.md#get_summary_workload) | **GET** /platform/4/statistics/summary/workload | 


# **get_statistics_current**
> StatisticsCurrent get_statistics_current(key=key, keys=keys, devid=devid, substr=substr, timeout=timeout, degraded=degraded)



Retrieve stats.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0_1
from isi_sdk_8_0_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0_1.StatisticsApi(isi_sdk_8_0_1.ApiClient(configuration))
key = ['key_example'] # list[str] | One key name. Can be used more than one time to query multiple keys. Also works with 'keys' arguments. (optional)
keys = ['keys_example'] # list[str] | Multiple key names. May request matching keys or request 'all' keys. Can be comma separated list or can be used more than one time to make queries for multiple keys. May be used in conjunction with 'substr'. Also works with 'key' arguments. (optional)
devid = ['devid_example'] # list[str] | Node devid to query. Either an <integer> or \"all\". Can be used more than one time to query multiple nodes. \"all\" queries all up nodes. 0 means query the local node. For \"cluster\" scoped keys, in any devid including 0 can be used. (optional)
substr = true # bool | Used in conjunction with the 'keys' argument, alters the behavior of keys. Makes the 'keys' arg perform a partial match. Defaults to false. (optional)
timeout = 56 # int | Time in seconds to wait for results from remote nodes. (optional)
degraded = true # bool | If true, try to continue even if some stats are unavailable. In this case, errors will be present in the per-key returned data. (optional)

try:
    api_response = api_instance.get_statistics_current(key=key, keys=keys, devid=devid, substr=substr, timeout=timeout, degraded=degraded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_statistics_current: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | [**list[str]**](str.md)| One key name. Can be used more than one time to query multiple keys. Also works with &#39;keys&#39; arguments. | [optional] 
 **keys** | [**list[str]**](str.md)| Multiple key names. May request matching keys or request &#39;all&#39; keys. Can be comma separated list or can be used more than one time to make queries for multiple keys. May be used in conjunction with &#39;substr&#39;. Also works with &#39;key&#39; arguments. | [optional] 
 **devid** | [**list[str]**](str.md)| Node devid to query. Either an &lt;integer&gt; or \&quot;all\&quot;. Can be used more than one time to query multiple nodes. \&quot;all\&quot; queries all up nodes. 0 means query the local node. For \&quot;cluster\&quot; scoped keys, in any devid including 0 can be used. | [optional] 
 **substr** | **bool**| Used in conjunction with the &#39;keys&#39; argument, alters the behavior of keys. Makes the &#39;keys&#39; arg perform a partial match. Defaults to false. | [optional] 
 **timeout** | **int**| Time in seconds to wait for results from remote nodes. | [optional] 
 **degraded** | **bool**| If true, try to continue even if some stats are unavailable. In this case, errors will be present in the per-key returned data. | [optional] 

### Return type

[**StatisticsCurrent**](StatisticsCurrent.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_history**
> StatisticsHistory get_statistics_history(begin=begin, interval=interval, end=end, timeout=timeout, substr=substr, keys=keys, devid=devid, memory_only=memory_only, key=key, degraded=degraded, resolution=resolution)



Retrieve stats.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0_1
from isi_sdk_8_0_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0_1.StatisticsApi(isi_sdk_8_0_1.ApiClient(configuration))
begin = 56 # int | Earliest time (Unix epoch seconds) of interest. Negative times are interpreted as relative (before) now. (optional)
interval = 56 # int | Minimum sampling interval time in seconds. If native statistics are higher resolution, data will be down-sampled. (optional)
end = 56 # int | Latest time (Unix epoch seconds) of interest. Negative times are interpreted as relative (before) now. If not supplied, use now as the end time. (optional)
timeout = 56 # int | Time in seconds to wait for results from remote nodes. (optional)
substr = true # bool | Used in conjunction with the 'keys' argument, alters the behavior of keys. Makes the 'keys' arg perform a partial match. Defaults to false. (optional)
keys = ['keys_example'] # list[str] | Multiple key names. May request matching keys or request 'all' keys. Can be comma separated list or can be used more than one time to make queries for multiple keys. May be used in conjunction with 'substr'. Also works with 'key' arguments. (optional)
devid = ['devid_example'] # list[str] | Node devid to query. Either an <integer> or \"all\". Can be used more than one time to query multiple nodes. \"all\" queries all up nodes. 0 means query the local node. For \"cluster\" scoped keys, in any devid including 0 can be used. (optional)
memory_only = true # bool | Only use statistics sources that reside in memory (faster, but with less retention). (optional)
key = ['key_example'] # list[str] | One key name. Can be used more than one time to query multiple keys. Also works with 'keys' arguments. (optional)
degraded = true # bool | If true, try to continue even if some stats are unavailable. In this case, errors will be present in the per-key returned data. (optional)
resolution = 56 # int | Synonymous with 'interval', if supplied supersedes interval. (optional)

try:
    api_response = api_instance.get_statistics_history(begin=begin, interval=interval, end=end, timeout=timeout, substr=substr, keys=keys, devid=devid, memory_only=memory_only, key=key, degraded=degraded, resolution=resolution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_statistics_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin** | **int**| Earliest time (Unix epoch seconds) of interest. Negative times are interpreted as relative (before) now. | [optional] 
 **interval** | **int**| Minimum sampling interval time in seconds. If native statistics are higher resolution, data will be down-sampled. | [optional] 
 **end** | **int**| Latest time (Unix epoch seconds) of interest. Negative times are interpreted as relative (before) now. If not supplied, use now as the end time. | [optional] 
 **timeout** | **int**| Time in seconds to wait for results from remote nodes. | [optional] 
 **substr** | **bool**| Used in conjunction with the &#39;keys&#39; argument, alters the behavior of keys. Makes the &#39;keys&#39; arg perform a partial match. Defaults to false. | [optional] 
 **keys** | [**list[str]**](str.md)| Multiple key names. May request matching keys or request &#39;all&#39; keys. Can be comma separated list or can be used more than one time to make queries for multiple keys. May be used in conjunction with &#39;substr&#39;. Also works with &#39;key&#39; arguments. | [optional] 
 **devid** | [**list[str]**](str.md)| Node devid to query. Either an &lt;integer&gt; or \&quot;all\&quot;. Can be used more than one time to query multiple nodes. \&quot;all\&quot; queries all up nodes. 0 means query the local node. For \&quot;cluster\&quot; scoped keys, in any devid including 0 can be used. | [optional] 
 **memory_only** | **bool**| Only use statistics sources that reside in memory (faster, but with less retention). | [optional] 
 **key** | [**list[str]**](str.md)| One key name. Can be used more than one time to query multiple keys. Also works with &#39;keys&#39; arguments. | [optional] 
 **degraded** | **bool**| If true, try to continue even if some stats are unavailable. In this case, errors will be present in the per-key returned data. | [optional] 
 **resolution** | **int**| Synonymous with &#39;interval&#39;, if supplied supersedes interval. | [optional] 

### Return type

[**StatisticsHistory**](StatisticsHistory.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_key**
> StatisticsKeys get_statistics_key(statistics_key_id)



List key meta-data.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0_1
from isi_sdk_8_0_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0_1.StatisticsApi(isi_sdk_8_0_1.ApiClient(configuration))
statistics_key_id = 'statistics_key_id_example' # str | List key meta-data.

try:
    api_response = api_instance.get_statistics_key(statistics_key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_statistics_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statistics_key_id** | **str**| List key meta-data. | 

### Return type

[**StatisticsKeys**](StatisticsKeys.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_keys**
> StatisticsKeysExtended get_statistics_keys(count=count, limit=limit, queryable=queryable, resume=resume)



List meta-data for matching keys.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0_1
from isi_sdk_8_0_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0_1.StatisticsApi(isi_sdk_8_0_1.ApiClient(configuration))
count = true # bool | Only count matching keys, do not return meta-data. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
queryable = true # bool | Only list keys that can/cannot be queries. Default is true. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_statistics_keys(count=count, limit=limit, queryable=queryable, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_statistics_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **bool**| Only count matching keys, do not return meta-data. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **queryable** | **bool**| Only list keys that can/cannot be queries. Default is true. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**StatisticsKeysExtended**](StatisticsKeysExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_operations**
> StatisticsOperations get_statistics_operations(protocols=protocols)



Retrieve operations list.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0_1
from isi_sdk_8_0_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0_1.StatisticsApi(isi_sdk_8_0_1.ApiClient(configuration))
protocols = ['protocols_example'] # list[str] | A comma separated list. Only report operations for specified protocol(s). Default is all. (optional)

try:
    api_response = api_instance.get_statistics_operations(protocols=protocols)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_statistics_operations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocols** | [**list[str]**](str.md)| A comma separated list. Only report operations for specified protocol(s). Default is all. | [optional] 

### Return type

[**StatisticsOperations**](StatisticsOperations.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_protocols**
> StatisticsProtocols get_statistics_protocols(type=type)



Retrieve protocol list.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0_1
from isi_sdk_8_0_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0_1.StatisticsApi(isi_sdk_8_0_1.ApiClient(configuration))
type = 'type_example' # str | Specifies whether internal, external, or all protocols should be returned. (optional)

try:
    api_response = api_instance.get_statistics_protocols(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_statistics_protocols: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Specifies whether internal, external, or all protocols should be returned. | [optional] 

### Return type

[**StatisticsProtocols**](StatisticsProtocols.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_client**
> SummaryClient get_summary_client(sort=sort, totalby=totalby, user_names=user_names, remote_addresses=remote_addresses, numeric=numeric, local_names=local_names, user_ids=user_ids, classes=classes, timeout=timeout, local_addresses=local_addresses, degraded=degraded, remote_names=remote_names, nodes=nodes, protocols=protocols)





### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0_1
from isi_sdk_8_0_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0_1.StatisticsApi(isi_sdk_8_0_1.ApiClient(configuration))
sort = 'sort_example' # str | Sort data by the specified comma-separated field(s). (num_operations | operation_rate | in_max | in_min | in | in_avg | out_max | out_min | out | out_avg | time_max | time_min | time_avg | node | protocol | class | user_id | user_name | local_addr | local_name | remote_addr | remote_name) Prepend 'asc:' or 'desc:' to a field to change the sort direction.  (optional)
totalby = 'totalby_example' # str | A comma separated list specifying what should be unique. (node | protocol | class | local_addr | local_name | remote_addr | remote_name | user_id | user_name | devid). Aggregation is performed over all the fields not specified in the list. (optional)
user_names = 'user_names_example' # str | A comma separated list. Only report statistics for operations requested by users with resolved names enumerated.  (optional)
remote_addresses = 'remote_addresses_example' # str | A comma separated list. Only report statistics for operations requested by the remote clients with dotted-quad IP addresses enumerated.  (optional)
numeric = true # bool | Do not resolve hostnames and usernames to their human readable form(s). Default is false.  (optional)
local_names = 'local_names_example' # str | A comma separated list. Only report statistics for operations handled by the local hosts with resolved names enumerated.  (optional)
user_ids = 'user_ids_example' # str | A comma separated list. Only report statistics for operations requested by users with numeric UIDs enumerated.  (optional)
classes = 'classes_example' # str | A comma separated list. Default is all. (other | write | read | namespace_read | namespace_write) (optional)
timeout = 56 # int | Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. (optional)
local_addresses = 'local_addresses_example' # str | A comma separated list. Only report statistics for operations handled by the local hosts with dotted-quad IP addresses enumerated.  (optional)
degraded = true # bool | Continue to report if some nodes do not respond. (optional)
remote_names = 'remote_names_example' # str | A comma separated list. Only report statistics for operations requested by the remote clients with resolved names enumerated.  (optional)
nodes = 'nodes_example' # str | A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. (optional)
protocols = 'protocols_example' # str | A comma separated list. Default is all. (nfs3 | smb1 | nlm | ftp | http | siq | smb2 | nfs4 | papi | jobd | irp | lsass_in | lsass_out | hdfs | internal | external) (optional)

try:
    api_response = api_instance.get_summary_client(sort=sort, totalby=totalby, user_names=user_names, remote_addresses=remote_addresses, numeric=numeric, local_names=local_names, user_ids=user_ids, classes=classes, timeout=timeout, local_addresses=local_addresses, degraded=degraded, remote_names=remote_names, nodes=nodes, protocols=protocols)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_summary_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Sort data by the specified comma-separated field(s). (num_operations | operation_rate | in_max | in_min | in | in_avg | out_max | out_min | out | out_avg | time_max | time_min | time_avg | node | protocol | class | user_id | user_name | local_addr | local_name | remote_addr | remote_name) Prepend &#39;asc:&#39; or &#39;desc:&#39; to a field to change the sort direction.  | [optional] 
 **totalby** | **str**| A comma separated list specifying what should be unique. (node | protocol | class | local_addr | local_name | remote_addr | remote_name | user_id | user_name | devid). Aggregation is performed over all the fields not specified in the list. | [optional] 
 **user_names** | **str**| A comma separated list. Only report statistics for operations requested by users with resolved names enumerated.  | [optional] 
 **remote_addresses** | **str**| A comma separated list. Only report statistics for operations requested by the remote clients with dotted-quad IP addresses enumerated.  | [optional] 
 **numeric** | **bool**| Do not resolve hostnames and usernames to their human readable form(s). Default is false.  | [optional] 
 **local_names** | **str**| A comma separated list. Only report statistics for operations handled by the local hosts with resolved names enumerated.  | [optional] 
 **user_ids** | **str**| A comma separated list. Only report statistics for operations requested by users with numeric UIDs enumerated.  | [optional] 
 **classes** | **str**| A comma separated list. Default is all. (other | write | read | namespace_read | namespace_write) | [optional] 
 **timeout** | **int**| Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. | [optional] 
 **local_addresses** | **str**| A comma separated list. Only report statistics for operations handled by the local hosts with dotted-quad IP addresses enumerated.  | [optional] 
 **degraded** | **bool**| Continue to report if some nodes do not respond. | [optional] 
 **remote_names** | **str**| A comma separated list. Only report statistics for operations requested by the remote clients with resolved names enumerated.  | [optional] 
 **nodes** | **str**| A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. | [optional] 
 **protocols** | **str**| A comma separated list. Default is all. (nfs3 | smb1 | nlm | ftp | http | siq | smb2 | nfs4 | papi | jobd | irp | lsass_in | lsass_out | hdfs | internal | external) | [optional] 

### Return type

[**SummaryClient**](SummaryClient.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_drive**
> SummaryDrive get_summary_drive(sort=sort, degraded=degraded, type=type, nodes=nodes, timeout=timeout)





### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0_1
from isi_sdk_8_0_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0_1.StatisticsApi(isi_sdk_8_0_1.ApiClient(configuration))
sort = 'sort_example' # str | Sort data by the specified comma-separated field(s). (drive_id | type | xfers_in | bytes_in | xfer_size_in | xfers_out | bytes_out | xfer_size_out | access_latency | access_slow | iosched_latency | iosched_queue | busy | used_bytes_percent | used_inodes). Prepend 'asc:' or 'desc:' to a field to change the sort direction.  (optional)
degraded = true # bool | Continue to report if some nodes do not respond. (optional)
type = 'type_example' # str | Specify drive type(s) for which statistics should be reported. (optional)
nodes = 'nodes_example' # str | A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. (optional)
timeout = 56 # int | Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. (optional)

try:
    api_response = api_instance.get_summary_drive(sort=sort, degraded=degraded, type=type, nodes=nodes, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_summary_drive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Sort data by the specified comma-separated field(s). (drive_id | type | xfers_in | bytes_in | xfer_size_in | xfers_out | bytes_out | xfer_size_out | access_latency | access_slow | iosched_latency | iosched_queue | busy | used_bytes_percent | used_inodes). Prepend &#39;asc:&#39; or &#39;desc:&#39; to a field to change the sort direction.  | [optional] 
 **degraded** | **bool**| Continue to report if some nodes do not respond. | [optional] 
 **type** | **str**| Specify drive type(s) for which statistics should be reported. | [optional] 
 **nodes** | **str**| A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. | [optional] 
 **timeout** | **int**| Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. | [optional] 

### Return type

[**SummaryDrive**](SummaryDrive.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_heat**
> SummaryHeat get_summary_heat(sort=sort, convertlin=convertlin, totalby=totalby, pathdepth=pathdepth, numeric=numeric, events=events, maxpath=maxpath, classes=classes, timeout=timeout, nodes=nodes, degraded=degraded)



File heat map, i.e. rate of file operations, and the type of operation listed by path/lin(s).

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0_1
from isi_sdk_8_0_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0_1.StatisticsApi(isi_sdk_8_0_1.ApiClient(configuration))
sort = 'sort_example' # str | Sort data by the specified comma-separated field(s). (operation_rate | node | event_name | class_name | lin | path). Prepend 'asc:' or 'desc:' to a field to change the sort direction.  (optional)
convertlin = true # bool | Convert lin to hex. Default is true.  (optional)
totalby = 'totalby_example' # str | A comma separated list specifying what should be unique. (node | event_name | event_class | operation_rate | path | lin). Aggregation is performed over all the fields not specified in the list. (optional)
pathdepth = 56 # int | Squash paths to this directory depth. Defaults to none, ie. the paths are not limited (Subject to the system limits.) (optional)
numeric = true # bool | Do not resolve LINs into filenames. Default is false.  (optional)
events = 'events_example' # str | A comma separated list. Default is all. Only report specified event types(s). (blocked | contended | deadlocked | getattr | link | lock | lookup | read | rename | setattr | unlink | write). (optional)
maxpath = 56 # int | Maximum bytes allocated for looking up a path. An ASCII character is 1 byte (It may be more for other types of encoding). The default is 1024 bytes. Zero (0) means unlimited (Subject to the system limits.) (optional)
classes = 'classes_example' # str | A comma separated list. Default is all. (other | write | read | namespace_read | namespace_write). (optional)
timeout = 56 # int | Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. (optional)
nodes = 'nodes_example' # str | A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. (optional)
degraded = true # bool | Continue to report if some nodes do not respond. (optional)

try:
    api_response = api_instance.get_summary_heat(sort=sort, convertlin=convertlin, totalby=totalby, pathdepth=pathdepth, numeric=numeric, events=events, maxpath=maxpath, classes=classes, timeout=timeout, nodes=nodes, degraded=degraded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_summary_heat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Sort data by the specified comma-separated field(s). (operation_rate | node | event_name | class_name | lin | path). Prepend &#39;asc:&#39; or &#39;desc:&#39; to a field to change the sort direction.  | [optional] 
 **convertlin** | **bool**| Convert lin to hex. Default is true.  | [optional] 
 **totalby** | **str**| A comma separated list specifying what should be unique. (node | event_name | event_class | operation_rate | path | lin). Aggregation is performed over all the fields not specified in the list. | [optional] 
 **pathdepth** | **int**| Squash paths to this directory depth. Defaults to none, ie. the paths are not limited (Subject to the system limits.) | [optional] 
 **numeric** | **bool**| Do not resolve LINs into filenames. Default is false.  | [optional] 
 **events** | **str**| A comma separated list. Default is all. Only report specified event types(s). (blocked | contended | deadlocked | getattr | link | lock | lookup | read | rename | setattr | unlink | write). | [optional] 
 **maxpath** | **int**| Maximum bytes allocated for looking up a path. An ASCII character is 1 byte (It may be more for other types of encoding). The default is 1024 bytes. Zero (0) means unlimited (Subject to the system limits.) | [optional] 
 **classes** | **str**| A comma separated list. Default is all. (other | write | read | namespace_read | namespace_write). | [optional] 
 **timeout** | **int**| Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. | [optional] 
 **nodes** | **str**| A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. | [optional] 
 **degraded** | **bool**| Continue to report if some nodes do not respond. | [optional] 

### Return type

[**SummaryHeat**](SummaryHeat.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_protocol**
> SummaryProtocol get_summary_protocol(operations=operations, sort=sort, totalby=totalby, zero=zero, classes=classes, timeout=timeout, degraded=degraded, nodes=nodes, protocols=protocols)





### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0_1
from isi_sdk_8_0_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0_1.StatisticsApi(isi_sdk_8_0_1.ApiClient(configuration))
operations = 'operations_example' # str | Specify operation(s) for which statistics should be reported (See the cli command: 'isi statistics list operations', for a total list). Default is all.  (optional)
sort = 'sort_example' # str | Sort data by the specified comma-separated field(s). (time | operation_count | operation_rate | in_max | in_min | in | in_avg | in_standard_dev | out_max | out_min | out | out_avg | out_standard_dev | time_max | time_min | time_avg | time_standard_dev | node | protocol | class | operation). Prepend 'asc:' or 'desc:' to a field to change the sort direction.  (optional)
totalby = 'totalby_example' # str | A comma separated list specifying what should be unique. (node | protocol | class | operation). Aggregation is performed over all the fields not specified in the list. (optional)
zero = true # bool | Show table entries with no values. (optional)
classes = 'classes_example' # str | A comma separated list. Default is all. (other | write | read | create | delete | namespace_read | namespace_write | file_state | session_state). (optional)
timeout = 56 # int | Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. (optional)
degraded = true # bool | Continue to report if some nodes do not respond. (optional)
nodes = 'nodes_example' # str | A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. (optional)
protocols = 'protocols_example' # str | A comma separated list. Default is all. (nfs3 | smb1 | nlm | ftp | http | siq | smb2 | nfs4 | papi | jobd | irp | lsass_in | lsass_out | hdfs | all | internal | external) (optional)

try:
    api_response = api_instance.get_summary_protocol(operations=operations, sort=sort, totalby=totalby, zero=zero, classes=classes, timeout=timeout, degraded=degraded, nodes=nodes, protocols=protocols)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_summary_protocol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operations** | **str**| Specify operation(s) for which statistics should be reported (See the cli command: &#39;isi statistics list operations&#39;, for a total list). Default is all.  | [optional] 
 **sort** | **str**| Sort data by the specified comma-separated field(s). (time | operation_count | operation_rate | in_max | in_min | in | in_avg | in_standard_dev | out_max | out_min | out | out_avg | out_standard_dev | time_max | time_min | time_avg | time_standard_dev | node | protocol | class | operation). Prepend &#39;asc:&#39; or &#39;desc:&#39; to a field to change the sort direction.  | [optional] 
 **totalby** | **str**| A comma separated list specifying what should be unique. (node | protocol | class | operation). Aggregation is performed over all the fields not specified in the list. | [optional] 
 **zero** | **bool**| Show table entries with no values. | [optional] 
 **classes** | **str**| A comma separated list. Default is all. (other | write | read | create | delete | namespace_read | namespace_write | file_state | session_state). | [optional] 
 **timeout** | **int**| Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. | [optional] 
 **degraded** | **bool**| Continue to report if some nodes do not respond. | [optional] 
 **nodes** | **str**| A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. | [optional] 
 **protocols** | **str**| A comma separated list. Default is all. (nfs3 | smb1 | nlm | ftp | http | siq | smb2 | nfs4 | papi | jobd | irp | lsass_in | lsass_out | hdfs | all | internal | external) | [optional] 

### Return type

[**SummaryProtocol**](SummaryProtocol.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_protocol_stats**
> SummaryProtocolStats get_summary_protocol_stats(degraded=degraded, protocol=protocol, nodes=nodes, timeout=timeout)





### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0_1
from isi_sdk_8_0_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0_1.StatisticsApi(isi_sdk_8_0_1.ApiClient(configuration))
degraded = true # bool | Continue to report if some nodes do not respond. (optional)
protocol = 'protocol_example' # str | A comma separated list. Default is all external protocols. (nfs3 | smb1 | nlm | ftp | http | siq | smb2 | nfs4 | papi | jobd | irp | lsass_in | lsass_out | hdfs) (optional)
nodes = 'nodes_example' # str | A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. (optional)
timeout = 56 # int | Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. (optional)

try:
    api_response = api_instance.get_summary_protocol_stats(degraded=degraded, protocol=protocol, nodes=nodes, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_summary_protocol_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **degraded** | **bool**| Continue to report if some nodes do not respond. | [optional] 
 **protocol** | **str**| A comma separated list. Default is all external protocols. (nfs3 | smb1 | nlm | ftp | http | siq | smb2 | nfs4 | papi | jobd | irp | lsass_in | lsass_out | hdfs) | [optional] 
 **nodes** | **str**| A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. | [optional] 
 **timeout** | **int**| Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. | [optional] 

### Return type

[**SummaryProtocolStats**](SummaryProtocolStats.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_system**
> SummarySystem get_summary_system(sort=sort, oprates=oprates, degraded=degraded, nodes=nodes, timeout=timeout)





### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0_1
from isi_sdk_8_0_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0_1.StatisticsApi(isi_sdk_8_0_1.ApiClient(configuration))
sort = 'sort_example' # str | Sort data by the specified comma-separated field(s). (time | node | cpu | smb | ftp | http | nfs | hdfs | total | net_in | net_out | disk_in). Prepend 'asc:' or 'desc:' to a field to change the sort direction.  (optional)
oprates = true # bool | Display protocol operation rate statistics rather than the default throughput statistics. (optional)
degraded = true # bool | Continue to report if some nodes do not respond. (optional)
nodes = 'nodes_example' # str | A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. (optional)
timeout = 56 # int | Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. (optional)

try:
    api_response = api_instance.get_summary_system(sort=sort, oprates=oprates, degraded=degraded, nodes=nodes, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_summary_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Sort data by the specified comma-separated field(s). (time | node | cpu | smb | ftp | http | nfs | hdfs | total | net_in | net_out | disk_in). Prepend &#39;asc:&#39; or &#39;desc:&#39; to a field to change the sort direction.  | [optional] 
 **oprates** | **bool**| Display protocol operation rate statistics rather than the default throughput statistics. | [optional] 
 **degraded** | **bool**| Continue to report if some nodes do not respond. | [optional] 
 **nodes** | **str**| A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. | [optional] 
 **timeout** | **int**| Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. | [optional] 

### Return type

[**SummarySystem**](SummarySystem.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_workload**
> SummaryWorkload get_summary_workload(sort=sort, totalby=totalby, job_type=job_type, timeout=timeout, degraded=degraded, nodes=nodes, system_names=system_names)





### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0_1
from isi_sdk_8_0_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0_1.StatisticsApi(isi_sdk_8_0_1.ApiClient(configuration))
sort = 'sort_example' # str | Sort data by the specified comma-separated field(s). (node | system_name | job_type | cpu | reads | writes | l2 | l3). Prepend 'asc:' or 'desc:' to a field to change the sort direction.  (optional)
totalby = 'totalby_example' # str | A comma separated list specifying what should be unique. (node | system_name | job_type). Aggregation is performed over all the fields not specified in the list. (optional)
job_type = 'job_type_example' # str | Only report statistics for a job specified by type, if configured.  (optional)
timeout = 56 # int | Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. (optional)
degraded = true # bool | Continue to report if some nodes do not respond. (optional)
nodes = 'nodes_example' # str | A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. (optional)
system_names = 'system_names_example' # str | A comma separated list. Only report statistics for workloads specified by system names. (optional)

try:
    api_response = api_instance.get_summary_workload(sort=sort, totalby=totalby, job_type=job_type, timeout=timeout, degraded=degraded, nodes=nodes, system_names=system_names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_summary_workload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Sort data by the specified comma-separated field(s). (node | system_name | job_type | cpu | reads | writes | l2 | l3). Prepend &#39;asc:&#39; or &#39;desc:&#39; to a field to change the sort direction.  | [optional] 
 **totalby** | **str**| A comma separated list specifying what should be unique. (node | system_name | job_type). Aggregation is performed over all the fields not specified in the list. | [optional] 
 **job_type** | **str**| Only report statistics for a job specified by type, if configured.  | [optional] 
 **timeout** | **int**| Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. | [optional] 
 **degraded** | **bool**| Continue to report if some nodes do not respond. | [optional] 
 **nodes** | **str**| A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. | [optional] 
 **system_names** | **str**| A comma separated list. Only report statistics for workloads specified by system names. | [optional] 

### Return type

[**SummaryWorkload**](SummaryWorkload.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

