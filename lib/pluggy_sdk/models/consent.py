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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Consent(BaseModel):
    """
    Item consent information
    """ # noqa: E501
    id: StrictStr = Field(description="Consent primary identifier")
    item_id: StrictStr = Field(description="Primary identifier of the item associated to the consent", alias="itemId")
    products: List[StrictStr] = Field(description="Products to be collected in the connection")
    open_finance_permissions_granted: Optional[List[StrictStr]] = Field(default=None, description="Products consented by the user to be collected", alias="openFinancePermissionsGranted")
    created_at: datetime = Field(description="Date when the consent was given", alias="createdAt")
    expires_at: Optional[datetime] = Field(default=None, description="Date when the consent expires. Null if the consent doesn't expire", alias="expiresAt")
    revoked_at: Optional[datetime] = Field(default=None, description="Date when the consent was revoked", alias="revokedAt")
    __properties: ClassVar[List[str]] = ["id", "itemId", "products", "openFinancePermissionsGranted", "createdAt", "expiresAt", "revokedAt"]

    @field_validator('products')
    def products_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['ACCOUNTS', 'CREDIT_CARDS', 'TRANSACTIONS', 'PAYMENT_DATA', 'INVESTMENTS', 'INVESTMENTS_TRANSACTIONS', 'IDENTITY', 'BROKERAGE_NOTE', 'OPPORTUNITIES', 'PORTFOLIO', 'INCOME_REPORTS', 'MOVE_SECURITY', 'LOANS', 'ACQUIRER_OPERATIONS']):
                raise ValueError("each list item must be one of ('ACCOUNTS', 'CREDIT_CARDS', 'TRANSACTIONS', 'PAYMENT_DATA', 'INVESTMENTS', 'INVESTMENTS_TRANSACTIONS', 'IDENTITY', 'BROKERAGE_NOTE', 'OPPORTUNITIES', 'PORTFOLIO', 'INCOME_REPORTS', 'MOVE_SECURITY', 'LOANS', 'ACQUIRER_OPERATIONS')")
        return value

    @field_validator('open_finance_permissions_granted')
    def open_finance_permissions_granted_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['REGISTRATION_ALL', 'REGISTRATION_IDENTIFICATIONS', 'REGISTRATION_QUALIFICATIONS', 'REGISTRATION_FINANCIAL_RELATIONS', 'ACCOUNTS_ALL', 'ACCOUNTS_LIST', 'ACCOUNTS_BALANCES', 'ACCOUNTS_LIMITS', 'ACCOUNTS_TRANSACTIONS', 'CREDIT_CARDS_ALL', 'CREDIT_CARDS_LIST', 'CREDIT_CARDS_LIMITS', 'CREDIT_CARDS_TRANSACTIONS', 'CREDIT_CARDS_BILLS', 'CREDIT_OPERATIONS_ALL', 'INVESTMENTS_ALL', 'EXCHANGES_ALL']):
                raise ValueError("each list item must be one of ('REGISTRATION_ALL', 'REGISTRATION_IDENTIFICATIONS', 'REGISTRATION_QUALIFICATIONS', 'REGISTRATION_FINANCIAL_RELATIONS', 'ACCOUNTS_ALL', 'ACCOUNTS_LIST', 'ACCOUNTS_BALANCES', 'ACCOUNTS_LIMITS', 'ACCOUNTS_TRANSACTIONS', 'CREDIT_CARDS_ALL', 'CREDIT_CARDS_LIST', 'CREDIT_CARDS_LIMITS', 'CREDIT_CARDS_TRANSACTIONS', 'CREDIT_CARDS_BILLS', 'CREDIT_OPERATIONS_ALL', 'INVESTMENTS_ALL', 'EXCHANGES_ALL')")
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
        """Create an instance of Consent from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Consent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "itemId": obj.get("itemId"),
            "products": obj.get("products"),
            "openFinancePermissionsGranted": obj.get("openFinancePermissionsGranted"),
            "createdAt": obj.get("createdAt"),
            "expiresAt": obj.get("expiresAt"),
            "revokedAt": obj.get("revokedAt")
        })
        return _obj


