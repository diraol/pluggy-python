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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class InvestmentMetadata(BaseModel):
    """
    Investment metadata for Previdencia migrations
    """ # noqa: E501
    tax_regime: Optional[StrictStr] = Field(default=None, description="Description of the type of tax applied to previdencia", alias="taxRegime")
    proposal_number: Optional[StrictStr] = Field(default=None, description="Previdencial proposal number", alias="proposalNumber")
    process_number: Optional[StrictStr] = Field(default=None, description="Number of the process of a previdencia", alias="processNumber")
    fund_name: Optional[StrictStr] = Field(default=None, description="Name of the fund associated with the previdencia.", alias="fundName")
    insurer: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["taxRegime", "proposalNumber", "processNumber", "fundName", "insurer"]

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
        """Create an instance of InvestmentMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of insurer
        if self.insurer:
            _dict['insurer'] = self.insurer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InvestmentMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "taxRegime": obj.get("taxRegime"),
            "proposalNumber": obj.get("proposalNumber"),
            "processNumber": obj.get("processNumber"),
            "fundName": obj.get("fundName"),
            "insurer": Company.from_dict(obj["insurer"]) if obj.get("insurer") is not None else None
        })
        return _obj


