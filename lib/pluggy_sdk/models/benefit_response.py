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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from pluggy_sdk.models.benefit_loan import BenefitLoan
from pluggy_sdk.models.benefit_response_paying_institution import BenefitResponsePayingInstitution
from typing import Optional, Set
from typing_extensions import Self

class BenefitResponse(BaseModel):
    """
    Response with information related to a benefit
    """ # noqa: E501
    id: StrictStr = Field(description="Primary identifier")
    item_id: StrictStr = Field(description="Identifier of the item linked to the loan", alias="itemId")
    beneficiary_name: StrictStr = Field(description="Beneficiary name", alias="beneficiaryName")
    available_margin_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Available margin value", alias="availableMarginValue")
    margin_base_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Base margin value", alias="marginBaseValue")
    deductible_available_margin_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Deductible available margin value", alias="deductibleAvailableMarginValue")
    used_margin_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Used margin value", alias="usedMarginValue")
    reserved_margin_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Reserved margin value", alias="reservedMarginValue")
    paying_institution: Optional[BenefitResponsePayingInstitution] = Field(default=None, alias="payingInstitution")
    loans: Optional[List[BenefitLoan]] = Field(default=None, description="List of benefit loans")
    __properties: ClassVar[List[str]] = ["id", "itemId", "beneficiaryName", "availableMarginValue", "marginBaseValue", "deductibleAvailableMarginValue", "usedMarginValue", "reservedMarginValue", "payingInstitution", "loans"]

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
        """Create an instance of BenefitResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of paying_institution
        if self.paying_institution:
            _dict['payingInstitution'] = self.paying_institution.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in loans (list)
        _items = []
        if self.loans:
            for _item_loans in self.loans:
                if _item_loans:
                    _items.append(_item_loans.to_dict())
            _dict['loans'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BenefitResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "itemId": obj.get("itemId"),
            "beneficiaryName": obj.get("beneficiaryName"),
            "availableMarginValue": obj.get("availableMarginValue"),
            "marginBaseValue": obj.get("marginBaseValue"),
            "deductibleAvailableMarginValue": obj.get("deductibleAvailableMarginValue"),
            "usedMarginValue": obj.get("usedMarginValue"),
            "reservedMarginValue": obj.get("reservedMarginValue"),
            "payingInstitution": BenefitResponsePayingInstitution.from_dict(obj["payingInstitution"]) if obj.get("payingInstitution") is not None else None,
            "loans": [BenefitLoan.from_dict(_item) for _item in obj["loans"]] if obj.get("loans") is not None else None
        })
        return _obj


