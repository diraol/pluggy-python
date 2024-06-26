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
from pluggy_sdk.models.bank_data import BankData
from pluggy_sdk.models.credit_data import CreditData
from typing import Optional, Set
from typing_extensions import Self

class Account(BaseModel):
    """
    Account of type bank
    """ # noqa: E501
    id: StrictStr = Field(description="Primary account identifier")
    type: StrictStr = Field(description="Type of account, may be BANK or CREDIT")
    subtype: StrictStr = Field(description="Subtype of corresponding type of account")
    number: StrictStr = Field(description="External identifier of the account")
    name: StrictStr = Field(description="Name of the account in a descriptive format")
    marketing_name: Optional[StrictStr] = Field(default=None, description="Name of the account as defined externally", alias="marketingName")
    balance: Union[StrictFloat, StrictInt] = Field(description="Funds of the account")
    item_id: StrictStr = Field(description="Attached item's primary identifier", alias="itemId")
    tax_number: Optional[StrictStr] = Field(default=None, description="Tax ID of the corresponding owner", alias="taxNumber")
    owner: Optional[StrictStr] = Field(default=None, description="Name of the owner of the account")
    currency_code: StrictStr = Field(description="Code referencing the currency of the balance", alias="currencyCode")
    bank_data: Optional[BankData] = Field(default=None, alias="bankData")
    credit_data: Optional[CreditData] = Field(default=None, alias="creditData")
    __properties: ClassVar[List[str]] = ["id", "type", "subtype", "number", "name", "marketingName", "balance", "itemId", "taxNumber", "owner", "currencyCode", "bankData", "creditData"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['BANK', 'CREDIT']):
            raise ValueError("must be one of enum values ('BANK', 'CREDIT')")
        return value

    @field_validator('subtype')
    def subtype_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['SAVINGS_ACCOUNT', 'CHECKING_ACCOUNT', 'CREDIT_CARD']):
            raise ValueError("must be one of enum values ('SAVINGS_ACCOUNT', 'CHECKING_ACCOUNT', 'CREDIT_CARD')")
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
        """Create an instance of Account from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bank_data
        if self.bank_data:
            _dict['bankData'] = self.bank_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credit_data
        if self.credit_data:
            _dict['creditData'] = self.credit_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Account from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "subtype": obj.get("subtype"),
            "number": obj.get("number"),
            "name": obj.get("name"),
            "marketingName": obj.get("marketingName"),
            "balance": obj.get("balance"),
            "itemId": obj.get("itemId"),
            "taxNumber": obj.get("taxNumber"),
            "owner": obj.get("owner"),
            "currencyCode": obj.get("currencyCode"),
            "bankData": BankData.from_dict(obj["bankData"]) if obj.get("bankData") is not None else None,
            "creditData": CreditData.from_dict(obj["creditData"]) if obj.get("creditData") is not None else None
        })
        return _obj


