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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class CreatePaymentIntent(BaseModel):
    """
    Request with information to create a payment intent
    """ # noqa: E501
    payment_request_id: Optional[StrictStr] = Field(default=None, description="Primary identifier of the payment request associated to the payment intent", alias="paymentRequestId")
    bulk_payment_id: Optional[StrictStr] = Field(default=None, description="Primary identifier of the bulk payment associated to the payment intent", alias="bulkPaymentId")
    parameters: Optional[Dict[str, Any]] = None
    connector_id: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Primary identifier of the connector associated to the payment intent", alias="connectorId")
    payment_method: Optional[StrictStr] = Field(default=None, description="Payment method can be PIS (Payment Initiation) or PIX (PIX QR flow), if PIX selected only `bulkPaymentId` is required, if PIS selected only `paymentRequestId` or `bulkPaymentId` are required with `connectorId`, `parameters` and `paymentMethod`", alias="paymentMethod")
    __properties: ClassVar[List[str]] = ["paymentRequestId", "bulkPaymentId", "parameters", "connectorId", "paymentMethod"]

    @field_validator('payment_method')
    def payment_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PIS', 'PIX']):
            raise ValueError("must be one of enum values ('PIS', 'PIX')")
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
        """Create an instance of CreatePaymentIntent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['parameters'] = self.parameters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreatePaymentIntent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "paymentRequestId": obj.get("paymentRequestId"),
            "bulkPaymentId": obj.get("bulkPaymentId"),
            "parameters": PaymentIntentParameter.from_dict(obj["parameters"]) if obj.get("parameters") is not None else None,
            "connectorId": obj.get("connectorId"),
            "paymentMethod": obj.get("paymentMethod")
        })
        return _obj


