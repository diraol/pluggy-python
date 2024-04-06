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
from typing import Optional, Set
from typing_extensions import Self

class CreditData(BaseModel):
    """
    Credit account additional fields
    """ # noqa: E501
    level: Optional[StrictStr] = Field(default=None, description="Card level (Black, Signature)")
    brand: Optional[StrictStr] = Field(default=None, description="Card Brand (Visa, Mastercard, Elo)")
    balance_close_date: Optional[datetime] = Field(default=None, description="Date when the balance was closed", alias="balanceCloseDate")
    balance_due_date: Optional[datetime] = Field(default=None, description="Date when the balance is dued", alias="balanceDueDate")
    available_credit_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Credit limit available to spent", alias="availableCreditLimit")
    balance_foreign_currency: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Balance in USD", alias="balanceForeignCurrency")
    minimum_payment: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Minimum payment due", alias="minimumPayment")
    credit_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Maximum amount that can be spent", alias="creditLimit")
    status: Optional[StrictStr] = Field(default=None, description="Credit card status")
    holder_type: Optional[StrictStr] = Field(default=None, description="Credit card holder type", alias="holderType")
    __properties: ClassVar[List[str]] = ["level", "brand", "balanceCloseDate", "balanceDueDate", "availableCreditLimit", "balanceForeignCurrency", "minimumPayment", "creditLimit", "status", "holderType"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ACTIVE', 'BLOCKED', 'CANCELLED']):
            raise ValueError("must be one of enum values ('ACTIVE', 'BLOCKED', 'CANCELLED')")
        return value

    @field_validator('holder_type')
    def holder_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MAIN', 'ADDITIONAL']):
            raise ValueError("must be one of enum values ('MAIN', 'ADDITIONAL')")
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
        """Create an instance of CreditData from a JSON string"""
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
        """Create an instance of CreditData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "level": obj.get("level"),
            "brand": obj.get("brand"),
            "balanceCloseDate": obj.get("balanceCloseDate"),
            "balanceDueDate": obj.get("balanceDueDate"),
            "availableCreditLimit": obj.get("availableCreditLimit"),
            "balanceForeignCurrency": obj.get("balanceForeignCurrency"),
            "minimumPayment": obj.get("minimumPayment"),
            "creditLimit": obj.get("creditLimit"),
            "status": obj.get("status"),
            "holderType": obj.get("holderType")
        })
        return _obj

