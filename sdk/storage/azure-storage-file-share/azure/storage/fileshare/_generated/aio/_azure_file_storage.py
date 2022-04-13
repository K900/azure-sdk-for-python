# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable

from msrest import Deserializer, Serializer

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .. import models
from ._configuration import AzureFileStorageConfiguration
from .operations import DirectoryOperations, FileOperations, ServiceOperations, ShareOperations

class AzureFileStorage:
    """AzureFileStorage.

    :ivar service: ServiceOperations operations
    :vartype service: azure.storage.fileshare.aio.operations.ServiceOperations
    :ivar share: ShareOperations operations
    :vartype share: azure.storage.fileshare.aio.operations.ShareOperations
    :ivar directory: DirectoryOperations operations
    :vartype directory: azure.storage.fileshare.aio.operations.DirectoryOperations
    :ivar file: FileOperations operations
    :vartype file: azure.storage.fileshare.aio.operations.FileOperations
    :param url: The URL of the service account, share, directory or file that is the target of the
     desired operation.
    :type url: str
    :param base_url: Service URL. Default value is "".
    :type base_url: str
    :keyword version: Specifies the version of the operation to use for this request. Default value
     is "2021-06-08". Note that overriding this default value may result in unsupported behavior.
    :paramtype version: str
    :keyword file_range_write_from_url: Only update is supported: - Update: Writes the bytes
     downloaded from the source url into the specified range. Default value is "update". Note that
     overriding this default value may result in unsupported behavior.
    :paramtype file_range_write_from_url: str
    """

    def __init__(
        self,
        url: str,
        base_url: str = "",
        **kwargs: Any
    ) -> None:
        self._config = AzureFileStorageConfiguration(url=url, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.service = ServiceOperations(self._client, self._config, self._serialize, self._deserialize)
        self.share = ShareOperations(self._client, self._config, self._serialize, self._deserialize)
        self.directory = DirectoryOperations(self._client, self._config, self._serialize, self._deserialize)
        self.file = FileOperations(self._client, self._config, self._serialize, self._deserialize)


    def _send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AzureFileStorage":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
