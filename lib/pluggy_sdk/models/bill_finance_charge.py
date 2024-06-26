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

class BillFinanceCharge(BaseModel):
    """
    Response with information related to a credit card bill finance charge
    """ # noqa: E501
    id: StrictStr = Field(description="Primary identifier")
    type: StrictStr = Field(description="Denomination of the charges that apply to the postpaid payment account bill")
    amount: Union[StrictFloat, StrictInt] = Field(description="Amount charged for the charge/fee")
    currency_code: StrictStr = Field(description="Code referencing the currency of the charge", alias="currencyCode")
    additional_info: Optional[StrictStr] = Field(default=None, description="Free field, mandatory to fill if 'OTHER' type of charge is selected", alias="additionalInfo")
    __properties: ClassVar[List[str]] = ["id", "type", "amount", "currencyCode", "additionalInfo"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['LATE_PAYMENT_REMUNERATIVE_INTEREST', 'LATE_PAYMENT_FEE', 'LATE_PAYMENT_INTEREST', 'IOF', 'OTHER']):
            raise ValueError("must be one of enum values ('LATE_PAYMENT_REMUNERATIVE_INTEREST', 'LATE_PAYMENT_FEE', 'LATE_PAYMENT_INTEREST', 'IOF', 'OTHER')")
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
        """Create an instance of BillFinanceCharge from a JSON string"""
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
        """Create an instance of BillFinanceCharge from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "amount": obj.get("amount"),
            "currencyCode": obj.get("currencyCode"),
            "additionalInfo": obj.get("additionalInfo")
        })
        return _obj


