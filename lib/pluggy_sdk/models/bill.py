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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from pluggy_sdk.models.bill_finance_charge import BillFinanceCharge
from typing import Optional, Set
from typing_extensions import Self

class Bill(BaseModel):
    """
    Response with information related to a credit card bill
    """ # noqa: E501
    id: StrictStr = Field(description="Primary identifier")
    due_date: datetime = Field(description="Due date of the bill, displayed for payment by the customer", alias="dueDate")
    total_amount: Union[StrictFloat, StrictInt] = Field(description="Total bill amount", alias="totalAmount")
    total_amount_currency_code: StrictStr = Field(description="Code referencing the currency of the bill", alias="totalAmountCurrencyCode")
    minimum_payment_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Minimum payment amount of the bill", alias="minimumPaymentAmount")
    allows_installments: Optional[StrictBool] = Field(default=None, description="Indicates whether the bill allows installment payments (true) or not (false)", alias="allowsInstallments")
    finance_charges: List[BillFinanceCharge] = Field(description="List of charges associated to the bill", alias="financeCharges")
    __properties: ClassVar[List[str]] = ["id", "dueDate", "totalAmount", "totalAmountCurrencyCode", "minimumPaymentAmount", "allowsInstallments", "financeCharges"]

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
        """Create an instance of Bill from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in finance_charges (list)
        _items = []
        if self.finance_charges:
            for _item_finance_charges in self.finance_charges:
                if _item_finance_charges:
                    _items.append(_item_finance_charges.to_dict())
            _dict['financeCharges'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Bill from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "dueDate": obj.get("dueDate"),
            "totalAmount": obj.get("totalAmount"),
            "totalAmountCurrencyCode": obj.get("totalAmountCurrencyCode"),
            "minimumPaymentAmount": obj.get("minimumPaymentAmount"),
            "allowsInstallments": obj.get("allowsInstallments"),
            "financeCharges": [BillFinanceCharge.from_dict(_item) for _item in obj["financeCharges"]] if obj.get("financeCharges") is not None else None
        })
        return _obj


