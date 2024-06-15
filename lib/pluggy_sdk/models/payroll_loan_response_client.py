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

class PayrollLoanResponseClient(BaseModel):
    """
    Client information
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Client name")
    document: Optional[StrictStr] = Field(default=None, description="Client CPF")
    phone: Optional[StrictStr] = Field(default=None, description="Client phone")
    addres_street: Optional[StrictStr] = Field(default=None, description="Client email", alias="addresStreet")
    address_number: Optional[StrictStr] = Field(default=None, description="Client address number", alias="addressNumber")
    address_city: Optional[StrictStr] = Field(default=None, description="Client address city", alias="addressCity")
    address_zip_code: Optional[StrictStr] = Field(default=None, description="Client address zip code", alias="addressZipCode")
    address_state: Optional[StrictStr] = Field(default=None, description="Client address state", alias="addressState")
    __properties: ClassVar[List[str]] = ["name", "document", "phone", "addresStreet", "addressNumber", "addressCity", "addressZipCode", "addressState"]

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
        """Create an instance of PayrollLoanResponseClient from a JSON string"""
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
        """Create an instance of PayrollLoanResponseClient from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "document": obj.get("document"),
            "phone": obj.get("phone"),
            "addresStreet": obj.get("addresStreet"),
            "addressNumber": obj.get("addressNumber"),
            "addressCity": obj.get("addressCity"),
            "addressZipCode": obj.get("addressZipCode"),
            "addressState": obj.get("addressState")
        })
        return _obj


