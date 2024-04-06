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
from pluggy_sdk.models.payment_recipient_account import PaymentRecipientAccount
from typing import Optional, Set
from typing_extensions import Self

class UpdatePaymentRecipient(BaseModel):
    """
    Request with information to update a payment recipient
    """ # noqa: E501
    tax_number: Optional[StrictStr] = Field(default=None, description="Account owner tax number. Can be CPF or CNPJ (only numbers)", alias="taxNumber")
    name: Optional[StrictStr] = Field(default=None, description="Account owner name")
    payment_institution_id: Optional[StrictStr] = Field(default=None, description="Primary identifier of the institution associated to the payment recipient", alias="paymentInstitutionId")
    account: Optional[PaymentRecipientAccount] = None
    is_default: Optional[StrictBool] = Field(default=None, description="Indicates if the recipient is the default one", alias="isDefault")
    __properties: ClassVar[List[str]] = ["taxNumber", "name", "paymentInstitutionId", "account", "isDefault"]

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
        """Create an instance of UpdatePaymentRecipient from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdatePaymentRecipient from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "taxNumber": obj.get("taxNumber"),
            "name": obj.get("name"),
            "paymentInstitutionId": obj.get("paymentInstitutionId"),
            "account": PaymentRecipientAccount.from_dict(obj["account"]) if obj.get("account") is not None else None,
            "isDefault": obj.get("isDefault")
        })
        return _obj


