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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class SmartAccount(BaseModel):
    """
    Smart account product
    """ # noqa: E501
    id: StrictStr = Field(description="Primary identifier of the Smart account")
    ispb: StrictStr = Field(description="Smart account ISP number")
    agency: StrictStr = Field(description="Smart account agency number")
    number: StrictStr = Field(description="Smart account number")
    verifying_digit: StrictStr = Field(description="Smart account verifying digit", alias="verifyingDigit")
    type: StrictStr = Field(description="Smart account type")
    is_sandbox: StrictBool = Field(description="Indicates if the smart account is a sandbox account", alias="isSandbox")
    pix_key: StrictStr = Field(description="Smart account PIX key", alias="pixKey")
    __properties: ClassVar[List[str]] = ["id", "ispb", "agency", "number", "verifyingDigit", "type", "isSandbox", "pixKey"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['CHECKING_ACCOUNT']):
            raise ValueError("must be one of enum values ('CHECKING_ACCOUNT')")
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
        """Create an instance of SmartAccount from a JSON string"""
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
        """Create an instance of SmartAccount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "ispb": obj.get("ispb"),
            "agency": obj.get("agency"),
            "number": obj.get("number"),
            "verifyingDigit": obj.get("verifyingDigit"),
            "type": obj.get("type"),
            "isSandbox": obj.get("isSandbox"),
            "pixKey": obj.get("pixKey")
        })
        return _obj


