# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 2
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isi_sdk_7_2.api_client import ApiClient


class StatisticsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_statistics_current(self, **kwargs):  # noqa: E501
        """get_statistics_current  # noqa: E501

        Retrieve stats.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statistics_current(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int timeout: Time in seconds to wait for results from remote nodes.
        :param bool degraded: If true, try to continue even if some stats are unavailable. In this case, errors will be present in the per-key returned data.
        :param list[str] devid: Node devid to query.  Either an <integer> or \"all\".  Can be used more than one time to query multiple nodes.  \"all\" queries all up nodes. 0 means query the local node. For \"cluster\" scoped keys, in any devid including 0 can be used.
        :param list[str] key: Key names. Can be used more than one time to query multiple keys.
        :param bool expand_clientid: If true, use name resolution to expand client addresses and other IDs.
        :return: StatisticsCurrent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_statistics_current_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_statistics_current_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_statistics_current_with_http_info(self, **kwargs):  # noqa: E501
        """get_statistics_current  # noqa: E501

        Retrieve stats.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statistics_current_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int timeout: Time in seconds to wait for results from remote nodes.
        :param bool degraded: If true, try to continue even if some stats are unavailable. In this case, errors will be present in the per-key returned data.
        :param list[str] devid: Node devid to query.  Either an <integer> or \"all\".  Can be used more than one time to query multiple nodes.  \"all\" queries all up nodes. 0 means query the local node. For \"cluster\" scoped keys, in any devid including 0 can be used.
        :param list[str] key: Key names. Can be used more than one time to query multiple keys.
        :param bool expand_clientid: If true, use name resolution to expand client addresses and other IDs.
        :return: StatisticsCurrent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['timeout', 'degraded', 'devid', 'key', 'expand_clientid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_statistics_current" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'timeout' in params:
            query_params.append(('timeout', params['timeout']))  # noqa: E501
        if 'degraded' in params:
            query_params.append(('degraded', params['degraded']))  # noqa: E501
        if 'devid' in params:
            query_params.append(('devid', params['devid']))  # noqa: E501
            collection_formats['devid'] = 'csv'  # noqa: E501
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501
            collection_formats['key'] = 'csv'  # noqa: E501
        if 'expand_clientid' in params:
            query_params.append(('expand_clientid', params['expand_clientid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/statistics/current', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatisticsCurrent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_statistics_history(self, **kwargs):  # noqa: E501
        """get_statistics_history  # noqa: E501

        Retrieve stats.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statistics_history(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int begin: Earliest time (Unix epoch seconds) of interest. Negative times are interpreted as relative (before) now.
        :param int interval: Minimum sampling interval time in seconds.  If native statistics are higher resolution, data will be down-sampled.
        :param int end: Latest time (Unix epoch seconds) of interest. Negative times are interpreted as relative (before) now. If not supplied, use now as the end time.
        :param int timeout: Time in seconds to wait for results from remote nodes.
        :param list[str] devid: Node devid to query.  Either an <integer> or \"all\".  Can be used more than one time to query multiple nodes.  \"all\" queries all up nodes. 0 means query the local node. For \"cluster\" scoped keys, in any devid including 0 can be used.
        :param bool memory_only: Only use statistics sources that reside in memory (faster, but with less retention).
        :param list[str] key: Key names. Can be used more than one time to query multiple keys.
        :param bool degraded: If true, try to continue even if some stats are unavailable. In this case, errors will be present in the per-key returned data.
        :param bool expand_clientid: If true, use name resolution to expand client addresses and other IDs.
        :return: StatisticsHistory
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_statistics_history_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_statistics_history_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_statistics_history_with_http_info(self, **kwargs):  # noqa: E501
        """get_statistics_history  # noqa: E501

        Retrieve stats.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statistics_history_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int begin: Earliest time (Unix epoch seconds) of interest. Negative times are interpreted as relative (before) now.
        :param int interval: Minimum sampling interval time in seconds.  If native statistics are higher resolution, data will be down-sampled.
        :param int end: Latest time (Unix epoch seconds) of interest. Negative times are interpreted as relative (before) now. If not supplied, use now as the end time.
        :param int timeout: Time in seconds to wait for results from remote nodes.
        :param list[str] devid: Node devid to query.  Either an <integer> or \"all\".  Can be used more than one time to query multiple nodes.  \"all\" queries all up nodes. 0 means query the local node. For \"cluster\" scoped keys, in any devid including 0 can be used.
        :param bool memory_only: Only use statistics sources that reside in memory (faster, but with less retention).
        :param list[str] key: Key names. Can be used more than one time to query multiple keys.
        :param bool degraded: If true, try to continue even if some stats are unavailable. In this case, errors will be present in the per-key returned data.
        :param bool expand_clientid: If true, use name resolution to expand client addresses and other IDs.
        :return: StatisticsHistory
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['begin', 'interval', 'end', 'timeout', 'devid', 'memory_only', 'key', 'degraded', 'expand_clientid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_statistics_history" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'begin' in params:
            query_params.append(('begin', params['begin']))  # noqa: E501
        if 'interval' in params:
            query_params.append(('interval', params['interval']))  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
        if 'timeout' in params:
            query_params.append(('timeout', params['timeout']))  # noqa: E501
        if 'devid' in params:
            query_params.append(('devid', params['devid']))  # noqa: E501
            collection_formats['devid'] = 'csv'  # noqa: E501
        if 'memory_only' in params:
            query_params.append(('memory_only', params['memory_only']))  # noqa: E501
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501
            collection_formats['key'] = 'csv'  # noqa: E501
        if 'degraded' in params:
            query_params.append(('degraded', params['degraded']))  # noqa: E501
        if 'expand_clientid' in params:
            query_params.append(('expand_clientid', params['expand_clientid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/statistics/history', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatisticsHistory',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_statistics_key(self, statistics_key_id, **kwargs):  # noqa: E501
        """get_statistics_key  # noqa: E501

        List key meta-data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statistics_key(statistics_key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str statistics_key_id: List key meta-data. (required)
        :return: StatisticsKeys
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_statistics_key_with_http_info(statistics_key_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_statistics_key_with_http_info(statistics_key_id, **kwargs)  # noqa: E501
            return data

    def get_statistics_key_with_http_info(self, statistics_key_id, **kwargs):  # noqa: E501
        """get_statistics_key  # noqa: E501

        List key meta-data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statistics_key_with_http_info(statistics_key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str statistics_key_id: List key meta-data. (required)
        :return: StatisticsKeys
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['statistics_key_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_statistics_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'statistics_key_id' is set
        if ('statistics_key_id' not in params or
                params['statistics_key_id'] is None):
            raise ValueError("Missing the required parameter `statistics_key_id` when calling `get_statistics_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'statistics_key_id' in params:
            path_params['StatisticsKeyId'] = params['statistics_key_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/statistics/keys/{StatisticsKeyId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatisticsKeys',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_statistics_keys(self, **kwargs):  # noqa: E501
        """get_statistics_keys  # noqa: E501

        List meta-data for matching keys.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statistics_keys(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool count: Only count matching keys, do not return meta-data.
        :param int limit: Return no more than this many results at once (see resume).
        :param bool queryable: Only list keys that can/cannot be queries. Default is true.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: StatisticsKeysExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_statistics_keys_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_statistics_keys_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_statistics_keys_with_http_info(self, **kwargs):  # noqa: E501
        """get_statistics_keys  # noqa: E501

        List meta-data for matching keys.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statistics_keys_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool count: Only count matching keys, do not return meta-data.
        :param int limit: Return no more than this many results at once (see resume).
        :param bool queryable: Only list keys that can/cannot be queries. Default is true.
        :param str resume: Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).
        :return: StatisticsKeysExtended
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['count', 'limit', 'queryable', 'resume']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_statistics_keys" % key
                )
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_statistics_keys`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'queryable' in params:
            query_params.append(('queryable', params['queryable']))  # noqa: E501
        if 'resume' in params:
            query_params.append(('resume', params['resume']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/statistics/keys', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatisticsKeysExtended',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_statistics_protocols(self, **kwargs):  # noqa: E501
        """get_statistics_protocols  # noqa: E501

        Retrieve protocol list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statistics_protocols(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StatisticsProtocols
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_statistics_protocols_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_statistics_protocols_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_statistics_protocols_with_http_info(self, **kwargs):  # noqa: E501
        """get_statistics_protocols  # noqa: E501

        Retrieve protocol list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statistics_protocols_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StatisticsProtocols
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_statistics_protocols" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/1/statistics/protocols', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatisticsProtocols',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
