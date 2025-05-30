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
from typing_extensions import Annotated
from pluggy_sdk.models.issued_boleto_fine import IssuedBoletoFine
from pluggy_sdk.models.issued_boleto_interest import IssuedBoletoInterest
from pluggy_sdk.models.issued_boleto_payer import IssuedBoletoPayer
from typing import Optional, Set
from typing_extensions import Self

class IssuedBoleto(BaseModel):
    """
    Response with information related to an issued boleto
    """ # noqa: E501
    id: StrictStr = Field(description="Primary identifier")
    amount: Union[Annotated[float, Field(strict=True, ge=2.5)], Annotated[int, Field(strict=True, ge=3)]] = Field(description="Boleto amount")
    status: StrictStr = Field(description="Current status of the boleto")
    seu_numero: Annotated[str, Field(strict=True, max_length=10)] = Field(description="Your identifier for this boleto", alias="seuNumero")
    due_date: datetime = Field(description="Due date of the boleto", alias="dueDate")
    payer: IssuedBoletoPayer
    pix_qr: Optional[StrictStr] = Field(default=None, description="PIX QR code for payment", alias="pixQr")
    digitable_line: StrictStr = Field(description="Boleto digitable line", alias="digitableLine")
    nosso_numero: Optional[StrictStr] = Field(default=None, description="Bank's internal identifier for the boleto", alias="nossoNumero")
    barcode: StrictStr = Field(description="Boleto barcode")
    boleto_connection_id: StrictStr = Field(description="ID of the boleto connection used to create this boleto", alias="boletoConnectionId")
    created_at: datetime = Field(description="Date when the boleto was created", alias="createdAt")
    amount_paid: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Amount that was paid for this boleto", alias="amountPaid")
    payment_origin: Optional[StrictStr] = Field(default=None, description="Origin of the payment when the boleto is paid", alias="paymentOrigin")
    fine: Optional[IssuedBoletoFine] = None
    interest: Optional[IssuedBoletoInterest] = None
    paid_at: Optional[datetime] = Field(default=None, description="Date when the boleto was paid", alias="paidAt")
    __properties: ClassVar[List[str]] = ["id", "amount", "status", "seuNumero", "dueDate", "payer", "pixQr", "digitableLine", "nossoNumero", "barcode", "boletoConnectionId", "createdAt", "amountPaid", "paymentOrigin", "fine", "interest", "paidAt"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['OPEN', 'PAID', 'OVERDUE', 'CANCELLED']):
            raise ValueError("must be one of enum values ('OPEN', 'PAID', 'OVERDUE', 'CANCELLED')")
        return value

    @field_validator('payment_origin')
    def payment_origin_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PIX', 'BOLETO']):
            raise ValueError("must be one of enum values ('PIX', 'BOLETO')")
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
        """Create an instance of IssuedBoleto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of payer
        if self.payer:
            _dict['payer'] = self.payer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fine
        if self.fine:
            _dict['fine'] = self.fine.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interest
        if self.interest:
            _dict['interest'] = self.interest.to_dict()
        # set to None if amount_paid (nullable) is None
        # and model_fields_set contains the field
        if self.amount_paid is None and "amount_paid" in self.model_fields_set:
            _dict['amountPaid'] = None

        # set to None if payment_origin (nullable) is None
        # and model_fields_set contains the field
        if self.payment_origin is None and "payment_origin" in self.model_fields_set:
            _dict['paymentOrigin'] = None

        # set to None if fine (nullable) is None
        # and model_fields_set contains the field
        if self.fine is None and "fine" in self.model_fields_set:
            _dict['fine'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IssuedBoleto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "amount": obj.get("amount"),
            "status": obj.get("status"),
            "seuNumero": obj.get("seuNumero"),
            "dueDate": obj.get("dueDate"),
            "payer": IssuedBoletoPayer.from_dict(obj["payer"]) if obj.get("payer") is not None else None,
            "pixQr": obj.get("pixQr"),
            "digitableLine": obj.get("digitableLine"),
            "nossoNumero": obj.get("nossoNumero"),
            "barcode": obj.get("barcode"),
            "boletoConnectionId": obj.get("boletoConnectionId"),
            "createdAt": obj.get("createdAt"),
            "amountPaid": obj.get("amountPaid"),
            "paymentOrigin": obj.get("paymentOrigin"),
            "fine": IssuedBoletoFine.from_dict(obj["fine"]) if obj.get("fine") is not None else None,
            "interest": IssuedBoletoInterest.from_dict(obj["interest"]) if obj.get("interest") is not None else None,
            "paidAt": obj.get("paidAt")
        })
        return _obj


