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
from openapi_client.models.bulk_payment import BulkPayment
from openapi_client.models.connector import Connector
from openapi_client.models.payment_request import PaymentRequest
from typing import Optional, Set
from typing_extensions import Self

class PaymentIntent(BaseModel):
    """
    Request with information related to a payment intent
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Primary identifier")
    status: Optional[StrictStr] = Field(default=None, description="Payment intent status")
    created_at: Optional[datetime] = Field(default=None, description="Date when the payment intent was created", alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, description="Date when the payment intent was updated", alias="updatedAt")
    payment_request: Optional[PaymentRequest] = Field(default=None, alias="paymentRequest")
    bulk_payment: Optional[BulkPayment] = Field(default=None, alias="bulkPayment")
    connector: Optional[Connector] = None
    consent_url: Optional[StrictStr] = Field(default=None, description="Url to authorize the payment intent", alias="consentUrl")
    reference_id: Optional[StrictStr] = Field(default=None, description="Pix id related to the payment intent", alias="referenceId")
    __properties: ClassVar[List[str]] = ["id", "status", "createdAt", "updatedAt", "paymentRequest", "bulkPayment", "connector", "consentUrl", "referenceId"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PAYMENT_REJECTED', 'ERROR', 'CANCELED', 'CONSENT_REJECTED', 'STARTED', 'ENQUEUED', 'CONSENT_AWAITING_AUTHORIZATION', 'CONSENT_AUTHORIZED', 'PAYMENT_PENDING', 'PAYMENT_PARTIALLY_ACCEPTED', 'PAYMENT_SETTLEMENT_PROCESSING', 'PAYMENT_SETTLEMENT_DEBTOR_ACCOUNT', 'PAYMENT_COMPLETED']):
            raise ValueError("must be one of enum values ('PAYMENT_REJECTED', 'ERROR', 'CANCELED', 'CONSENT_REJECTED', 'STARTED', 'ENQUEUED', 'CONSENT_AWAITING_AUTHORIZATION', 'CONSENT_AUTHORIZED', 'PAYMENT_PENDING', 'PAYMENT_PARTIALLY_ACCEPTED', 'PAYMENT_SETTLEMENT_PROCESSING', 'PAYMENT_SETTLEMENT_DEBTOR_ACCOUNT', 'PAYMENT_COMPLETED')")
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
        """Create an instance of PaymentIntent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of payment_request
        if self.payment_request:
            _dict['paymentRequest'] = self.payment_request.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_payment
        if self.bulk_payment:
            _dict['bulkPayment'] = self.bulk_payment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of connector
        if self.connector:
            _dict['connector'] = self.connector.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentIntent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "paymentRequest": PaymentRequest.from_dict(obj["paymentRequest"]) if obj.get("paymentRequest") is not None else None,
            "bulkPayment": BulkPayment.from_dict(obj["bulkPayment"]) if obj.get("bulkPayment") is not None else None,
            "connector": Connector.from_dict(obj["connector"]) if obj.get("connector") is not None else None,
            "consentUrl": obj.get("consentUrl"),
            "referenceId": obj.get("referenceId")
        })
        return _obj


