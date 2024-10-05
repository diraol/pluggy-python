# coding: utf-8

"""
    Pluggy API

    Pluggy's main API to review data and execute connectors

    The version of the OpenAPI document: 1.0.0
    Contact: hello@pluggy.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from pluggy_sdk.models.connector import Connector
from pluggy_sdk.models.connector_credential import ConnectorCredential
from pluggy_sdk.models.connector_user_action import ConnectorUserAction
from pluggy_sdk.models.item_error import ItemError
from pluggy_sdk.models.status_detail import StatusDetail
from typing import Optional, Set
from typing_extensions import Self

class Item(BaseModel):
    """
    Item object
    """ # noqa: E501
    id: StrictStr = Field(description="Primary identifier")
    connector: Optional[Connector] = None
    status: StrictStr = Field(description="Status of the Item")
    execution_status: StrictStr = Field(description="Status of the sync execution", alias="executionStatus")
    error: Optional[ItemError] = None
    parameter: Optional[ConnectorCredential] = None
    user_action: Optional[ConnectorUserAction] = Field(default=None, alias="userAction")
    webhook_url: Optional[StrictStr] = Field(default=None, description="Url to be notified of item changes", alias="webhookUrl")
    created_at: Optional[datetime] = Field(default=None, description="Date of creation", alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, description="Date of last modification", alias="updatedAt")
    last_updated_at: Optional[datetime] = Field(default=None, description="Date of last syncronization", alias="lastUpdatedAt")
    status_detail: Optional[StatusDetail] = Field(default=None, alias="statusDetail")
    next_auto_sync_at: Optional[datetime] = Field(default=None, description="Date of next auto-sync, or null if auto-sync is disabled for this Item", alias="nextAutoSyncAt")
    consecutive_failed_login_attempts: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Consecutives execution that ends up with a LOGIN_ERROR status", alias="consecutiveFailedLoginAttempts")
    consent_expires_at: Optional[datetime] = Field(default=None, description="Consent expiration date", alias="consentExpiresAt")
    products: Optional[List[StrictStr]] = Field(default=None, description="Products collected by the item")
    __properties: ClassVar[List[str]] = ["id", "connector", "status", "executionStatus", "error", "parameter", "userAction", "webhookUrl", "createdAt", "updatedAt", "lastUpdatedAt", "statusDetail", "nextAutoSyncAt", "consecutiveFailedLoginAttempts", "consentExpiresAt", "products"]

    @field_validator('products')
    def products_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['ACCOUNTS', 'CREDIT_CARDS', 'TRANSACTIONS', 'PAYMENT_DATA', 'INVESTMENTS', 'INVESTMENTS_TRANSACTIONS', 'IDENTITY', 'BROKERAGE_NOTE', 'MOVE_SECURITY', 'LOANS']):
                raise ValueError("each list item must be one of ('ACCOUNTS', 'CREDIT_CARDS', 'TRANSACTIONS', 'PAYMENT_DATA', 'INVESTMENTS', 'INVESTMENTS_TRANSACTIONS', 'IDENTITY', 'BROKERAGE_NOTE', 'MOVE_SECURITY', 'LOANS')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Item from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of connector
        if self.connector:
            _dict['connector'] = self.connector.to_dict()
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parameter
        if self.parameter:
            _dict['parameter'] = self.parameter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_action
        if self.user_action:
            _dict['userAction'] = self.user_action.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status_detail
        if self.status_detail:
            _dict['statusDetail'] = self.status_detail.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Item from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "connector": Connector.from_dict(obj["connector"]) if obj.get("connector") is not None else None,
            "status": obj.get("status"),
            "executionStatus": obj.get("executionStatus"),
            "error": ItemError.from_dict(obj["error"]) if obj.get("error") is not None else None,
            "parameter": ConnectorCredential.from_dict(obj["parameter"]) if obj.get("parameter") is not None else None,
            "userAction": ConnectorUserAction.from_dict(obj["userAction"]) if obj.get("userAction") is not None else None,
            "webhookUrl": obj.get("webhookUrl"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "lastUpdatedAt": obj.get("lastUpdatedAt"),
            "statusDetail": StatusDetail.from_dict(obj["statusDetail"]) if obj.get("statusDetail") is not None else None,
            "nextAutoSyncAt": obj.get("nextAutoSyncAt"),
            "consecutiveFailedLoginAttempts": obj.get("consecutiveFailedLoginAttempts"),
            "consentExpiresAt": obj.get("consentExpiresAt"),
            "products": obj.get("products")
        })
        return _obj


