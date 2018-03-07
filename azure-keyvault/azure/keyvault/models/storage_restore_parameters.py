# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class StorageRestoreParameters(Model):
    """The secret restore parameters.

    :param storage_bundle_backup: The backup blob associated with a storage
     account.
    :type storage_bundle_backup: bytes
    """

    _validation = {
        'storage_bundle_backup': {'required': True},
    }

    _attribute_map = {
        'storage_bundle_backup': {'key': 'value', 'type': 'base64'},
    }

    def __init__(self, storage_bundle_backup):
        super(StorageRestoreParameters, self).__init__()
        self.storage_bundle_backup = storage_bundle_backup
