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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from pluggy_sdk.models.boleto_payer import BoletoPayer
from pluggy_sdk.models.boleto_recipient import BoletoRecipient
from typing import Optional, Set
from typing_extensions import Self

class Boleto(BaseModel):
    """
    Boleto data
    """ # noqa: E501
    digitable_line: StrictStr = Field(description="Boleto digitable line", alias="digitableLine")
    barcode: StrictStr = Field(description="Boleto barcode")
    payer: BoletoPayer
    recipient: BoletoRecipient
    var_date: Optional[datetime] = Field(default=None, description="Boleto issue date", alias="date")
    due_date: datetime = Field(description="Boleto due date", alias="dueDate")
    expiration_date: Optional[datetime] = Field(default=None, description="After this date, the boleto cannot be paid", alias="expirationDate")
    base_amount: Union[StrictFloat, StrictInt] = Field(description="Boleto original amount, without interests, penalties and discounts", alias="baseAmount")
    penalty_amount: Union[StrictFloat, StrictInt] = Field(description="Boleto penalty amount. If there is no penalty, it will be returned as zero", alias="penaltyAmount")
    interest_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Boleto interest amount. If there is no interest, it will be returned as zero", alias="interestAmount")
    discount_amount: Union[StrictFloat, StrictInt] = Field(description="Boleto discount amount. If there is no discounts, it will be returned as zero", alias="discountAmount")
    total_amount: Union[StrictFloat, StrictInt] = Field(description="Boleto final amount. It is equal to the base amount plus penalties and interests, minus discounts", alias="totalAmount")
    updated_at: Optional[datetime] = Field(default=None, description="Date when the lastest information of this boleto has been retrieved", alias="updatedAt")
    __properties: ClassVar[List[str]] = ["digitableLine", "barcode", "payer", "recipient", "date", "dueDate", "expirationDate", "baseAmount", "penaltyAmount", "interestAmount", "discountAmount", "totalAmount", "updatedAt"]

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
        """Create an instance of Boleto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of recipient
        if self.recipient:
            _dict['recipient'] = self.recipient.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Boleto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "digitableLine": obj.get("digitableLine"),
            "barcode": obj.get("barcode"),
            "payer": BoletoPayer.from_dict(obj["payer"]) if obj.get("payer") is not None else None,
            "recipient": BoletoRecipient.from_dict(obj["recipient"]) if obj.get("recipient") is not None else None,
            "date": obj.get("date"),
            "dueDate": obj.get("dueDate"),
            "expirationDate": obj.get("expirationDate"),
            "baseAmount": obj.get("baseAmount"),
            "penaltyAmount": obj.get("penaltyAmount"),
            "interestAmount": obj.get("interestAmount"),
            "discountAmount": obj.get("discountAmount"),
            "totalAmount": obj.get("totalAmount"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


