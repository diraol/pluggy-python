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
from pluggy_sdk.models.payment_receipt import PaymentReceipt
from typing import Optional, Set
from typing_extensions import Self

class SmartTransferPayment(BaseModel):
    """
    Smart transfer payment
    """ # noqa: E501
    id: StrictStr = Field(description="Payment primary identifier")
    preauthorization_id: StrictStr = Field(description="Payment primary identifier", alias="preauthorizationId")
    status: StrictStr = Field(description="Payment status")
    amount: Union[StrictFloat, StrictInt] = Field(description="Payment amount")
    description: Optional[StrictStr] = Field(default=None, description="Payment description")
    recipient: PaymentReceipt
    client_payment_id: Optional[StrictStr] = Field(default=None, description="Client payment identifier", alias="clientPaymentId")
    created_at: datetime = Field(description="Date when the payemnt was created", alias="createdAt")
    updated_at: datetime = Field(description="Date when the payment was updated", alias="updatedAt")
    __properties: ClassVar[List[str]] = ["id", "preauthorizationId", "status", "amount", "description", "recipient", "clientPaymentId", "createdAt", "updatedAt"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PAYMENT_REJECTED', 'ERROR', 'CANCELED', 'CONSENT_REJECTED', 'CONSENT_AUTHORIZED', 'PAYMENT_PENDING', 'PAYMENT_PARTIALLY_ACCEPTED', 'PAYMENT_SETTLEMENT_PROCESSING', 'PAYMENT_SETTLEMENT_DEBTOR_ACCOUNT', 'PAYMENT_COMPLETED']):
            raise ValueError("must be one of enum values ('PAYMENT_REJECTED', 'ERROR', 'CANCELED', 'CONSENT_REJECTED', 'CONSENT_AUTHORIZED', 'PAYMENT_PENDING', 'PAYMENT_PARTIALLY_ACCEPTED', 'PAYMENT_SETTLEMENT_PROCESSING', 'PAYMENT_SETTLEMENT_DEBTOR_ACCOUNT', 'PAYMENT_COMPLETED')")
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
        """Create an instance of SmartTransferPayment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of recipient
        if self.recipient:
            _dict['recipient'] = self.recipient.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SmartTransferPayment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "preauthorizationId": obj.get("preauthorizationId"),
            "status": obj.get("status"),
            "amount": obj.get("amount"),
            "description": obj.get("description"),
            "recipient": PaymentReceipt.from_dict(obj["recipient"]) if obj.get("recipient") is not None else None,
            "clientPaymentId": obj.get("clientPaymentId"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


