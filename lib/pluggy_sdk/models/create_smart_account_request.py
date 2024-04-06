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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from pluggy_sdk.models.smart_account_address import SmartAccountAddress
from typing import Optional, Set
from typing_extensions import Self

class CreateSmartAccountRequest(BaseModel):
    """
    Create smart account request
    """ # noqa: E501
    name: StrictStr = Field(description="Account owner fullName")
    tax_number: StrictStr = Field(description="Account owner tax number (CPF or CNPJ)", alias="taxNumber")
    email: StrictStr = Field(description="Account owner email")
    phone_number: StrictStr = Field(description="Account owner phone", alias="phoneNumber")
    is_sandbox: Optional[StrictBool] = Field(default=None, description="Indicates if the smart account is a sandbox account", alias="isSandbox")
    address: SmartAccountAddress
    __properties: ClassVar[List[str]] = ["name", "taxNumber", "email", "phoneNumber", "isSandbox", "address"]

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
        """Create an instance of CreateSmartAccountRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateSmartAccountRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "taxNumber": obj.get("taxNumber"),
            "email": obj.get("email"),
            "phoneNumber": obj.get("phoneNumber"),
            "isSandbox": obj.get("isSandbox"),
            "address": SmartAccountAddress.from_dict(obj["address"]) if obj.get("address") is not None else None
        })
        return _obj

