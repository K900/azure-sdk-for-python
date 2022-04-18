# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ChangeAttributes(msrest.serialization.Model):
    """Details about the change resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar correlation_id: The ARM correlation ID of the change resource.
    :vartype correlation_id: str
    :ivar timestamp: The time the change(s) on the target resource ocurred.
    :vartype timestamp: str
    :ivar changes_count: The number of changes this resource captures.
    :vartype changes_count: long
    :ivar previous_resource_snapshot_id: The GUID of the previous snapshot.
    :vartype previous_resource_snapshot_id: str
    :ivar new_resource_snapshot_id: The GUID of the new snapshot.
    :vartype new_resource_snapshot_id: str
    """

    _validation = {
        'correlation_id': {'readonly': True},
        'timestamp': {'readonly': True},
        'changes_count': {'readonly': True},
        'previous_resource_snapshot_id': {'readonly': True},
        'new_resource_snapshot_id': {'readonly': True},
    }

    _attribute_map = {
        'correlation_id': {'key': 'correlationId', 'type': 'str'},
        'timestamp': {'key': 'timestamp', 'type': 'str'},
        'changes_count': {'key': 'changesCount', 'type': 'long'},
        'previous_resource_snapshot_id': {'key': 'previousResourceSnapshotId', 'type': 'str'},
        'new_resource_snapshot_id': {'key': 'newResourceSnapshotId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(ChangeAttributes, self).__init__(**kwargs)
        self.correlation_id = None
        self.timestamp = None
        self.changes_count = None
        self.previous_resource_snapshot_id = None
        self.new_resource_snapshot_id = None


class ChangeBase(msrest.serialization.Model):
    """An individual change on the target resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar property_change_type: The type of change that occurred. Possible values include:
     "Update", "Insert", "Remove".
    :vartype property_change_type: str or
     ~azure.mgmt.resource.changes.v2022_03_01_preview.models.PropertyChangeType
    :ivar change_category: The entity that made the change. Possible values include: "User",
     "System", "Create".
    :vartype change_category: str or
     ~azure.mgmt.resource.changes.v2022_03_01_preview.models.ChangeCategory
    :ivar previous_value: The target resource property value before the change.
    :vartype previous_value: str
    :ivar new_value: The target resource property value after the change.
    :vartype new_value: str
    """

    _validation = {
        'property_change_type': {'readonly': True},
        'change_category': {'readonly': True},
        'previous_value': {'readonly': True},
        'new_value': {'readonly': True},
    }

    _attribute_map = {
        'property_change_type': {'key': 'propertyChangeType', 'type': 'str'},
        'change_category': {'key': 'changeCategory', 'type': 'str'},
        'previous_value': {'key': 'previousValue', 'type': 'str'},
        'new_value': {'key': 'newValue', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(ChangeBase, self).__init__(**kwargs)
        self.property_change_type = None
        self.change_category = None
        self.previous_value = None
        self.new_value = None


class ChangeProperties(msrest.serialization.Model):
    """The properties of a change.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar target_resource_id: The fully qualified ID of the target resource that was changed.
    :vartype target_resource_id: str
    :ivar target_resource_type: The namespace and type of the resource.
    :vartype target_resource_type: str
    :ivar change_type: The type of change that was captured in the resource. Possible values
     include: "Update", "Create".
    :vartype change_type: str or ~azure.mgmt.resource.changes.v2022_03_01_preview.models.ChangeType
    :ivar change_attributes: Details about the change resource.
    :vartype change_attributes:
     ~azure.mgmt.resource.changes.v2022_03_01_preview.models.ChangeAttributes
    :ivar changes: A dictionary with changed property name as a key and the change details as the
     value.
    :vartype changes: dict[str, ~azure.mgmt.resource.changes.v2022_03_01_preview.models.ChangeBase]
    """

    _validation = {
        'target_resource_id': {'readonly': True},
        'target_resource_type': {'readonly': True},
        'change_type': {'readonly': True},
    }

    _attribute_map = {
        'target_resource_id': {'key': 'targetResourceId', 'type': 'str'},
        'target_resource_type': {'key': 'targetResourceType', 'type': 'str'},
        'change_type': {'key': 'changeType', 'type': 'str'},
        'change_attributes': {'key': 'changeAttributes', 'type': 'ChangeAttributes'},
        'changes': {'key': 'changes', 'type': '{ChangeBase}'},
    }

    def __init__(
        self,
        *,
        change_attributes: Optional["ChangeAttributes"] = None,
        changes: Optional[Dict[str, "ChangeBase"]] = None,
        **kwargs
    ):
        """
        :keyword change_attributes: Details about the change resource.
        :paramtype change_attributes:
         ~azure.mgmt.resource.changes.v2022_03_01_preview.models.ChangeAttributes
        :keyword changes: A dictionary with changed property name as a key and the change details as
         the value.
        :paramtype changes: dict[str,
         ~azure.mgmt.resource.changes.v2022_03_01_preview.models.ChangeBase]
        """
        super(ChangeProperties, self).__init__(**kwargs)
        self.target_resource_id = None
        self.target_resource_type = None
        self.change_type = None
        self.change_attributes = change_attributes
        self.changes = changes


class ChangeResourceListResult(msrest.serialization.Model):
    """The list of resources.

    :ivar next_link: The link used to get the next page of Change Resources.
    :vartype next_link: str
    :ivar value: The list of resources.
    :vartype value:
     list[~azure.mgmt.resource.changes.v2022_03_01_preview.models.ChangeResourceResult]
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[ChangeResourceResult]'},
    }

    def __init__(
        self,
        *,
        next_link: Optional[str] = None,
        value: Optional[List["ChangeResourceResult"]] = None,
        **kwargs
    ):
        """
        :keyword next_link: The link used to get the next page of Change Resources.
        :paramtype next_link: str
        :keyword value: The list of resources.
        :paramtype value:
         list[~azure.mgmt.resource.changes.v2022_03_01_preview.models.ChangeResourceResult]
        """
        super(ChangeResourceListResult, self).__init__(**kwargs)
        self.next_link = next_link
        self.value = value


class Resource(msrest.serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class ChangeResourceResult(Resource):
    """Change Resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar properties: The properties of a change.
    :vartype properties: ~azure.mgmt.resource.changes.v2022_03_01_preview.models.ChangeProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ChangeProperties'},
    }

    def __init__(
        self,
        *,
        properties: Optional["ChangeProperties"] = None,
        **kwargs
    ):
        """
        :keyword properties: The properties of a change.
        :paramtype properties: ~azure.mgmt.resource.changes.v2022_03_01_preview.models.ChangeProperties
        """
        super(ChangeResourceResult, self).__init__(**kwargs)
        self.properties = properties


class ErrorAdditionalInfo(msrest.serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: any
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(msrest.serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.resource.changes.v2022_03_01_preview.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.resource.changes.v2022_03_01_preview.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(ErrorDetail, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(msrest.serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).

    :ivar error: The error object.
    :vartype error: ~azure.mgmt.resource.changes.v2022_03_01_preview.models.ErrorDetail
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetail'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorDetail"] = None,
        **kwargs
    ):
        """
        :keyword error: The error object.
        :paramtype error: ~azure.mgmt.resource.changes.v2022_03_01_preview.models.ErrorDetail
        """
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error
