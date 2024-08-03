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
from pluggy_sdk.models.loan_installment_balloon_payment import LoanInstallmentBalloonPayment
from typing import Optional, Set
from typing_extensions import Self

class LoanInstallments(BaseModel):
    """
    LoanInstallments
    """ # noqa: E501
    type_number_of_installments: Optional[StrictStr] = Field(default=None, description="Type of total term of the contract referring to the type of credit informed", alias="typeNumberOfInstallments")
    total_number_of_installments: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total term according to the type referring to the type of credit informed", alias="totalNumberOfInstallments")
    type_contract_remaining: Optional[StrictStr] = Field(default=None, description="Type of remaining term of the contract referring to the type of credit informed", alias="typeContractRemaining")
    contract_remaining_number: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Remaining term according to the type referring to the credit type informed", alias="contractRemainingNumber")
    paid_installments: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Number of paid installments", alias="paidInstallments")
    due_installments: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Number of due installments", alias="dueInstallments")
    past_due_installments: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Number of overdue installments", alias="pastDueInstallments")
    balloon_payments: Optional[List[LoanInstallmentBalloonPayment]] = Field(default=None, description="List that brings the due dates and value of the non-regular installments of the contract of the type of credit consulted", alias="balloonPayments")
    __properties: ClassVar[List[str]] = ["typeNumberOfInstallments", "totalNumberOfInstallments", "typeContractRemaining", "contractRemainingNumber", "paidInstallments", "dueInstallments", "pastDueInstallments", "balloonPayments"]

    @field_validator('type_number_of_installments')
    def type_number_of_installments_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DAY', 'WEEK', 'MONTH', 'YEAR', 'WITHOUT_TOTAL_PERIOD']):
            raise ValueError("must be one of enum values ('DAY', 'WEEK', 'MONTH', 'YEAR', 'WITHOUT_TOTAL_PERIOD')")
        return value

    @field_validator('type_contract_remaining')
    def type_contract_remaining_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DAY', 'WEEK', 'MONTH', 'YEAR', 'WITHOUT_TOTAL_PERIOD', 'WITHOUT_REMAINING_PERIOD']):
            raise ValueError("must be one of enum values ('DAY', 'WEEK', 'MONTH', 'YEAR', 'WITHOUT_TOTAL_PERIOD', 'WITHOUT_REMAINING_PERIOD')")
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
        """Create an instance of LoanInstallments from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in balloon_payments (list)
        _items = []
        if self.balloon_payments:
            for _item_balloon_payments in self.balloon_payments:
                if _item_balloon_payments:
                    _items.append(_item_balloon_payments.to_dict())
            _dict['balloonPayments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LoanInstallments from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "typeNumberOfInstallments": obj.get("typeNumberOfInstallments"),
            "totalNumberOfInstallments": obj.get("totalNumberOfInstallments"),
            "typeContractRemaining": obj.get("typeContractRemaining"),
            "contractRemainingNumber": obj.get("contractRemainingNumber"),
            "paidInstallments": obj.get("paidInstallments"),
            "dueInstallments": obj.get("dueInstallments"),
            "pastDueInstallments": obj.get("pastDueInstallments"),
            "balloonPayments": [LoanInstallmentBalloonPayment.from_dict(_item) for _item in obj["balloonPayments"]] if obj.get("balloonPayments") is not None else None
        })
        return _obj


