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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from pluggy_sdk.models.acquirer_receivable_destination_account import AcquirerReceivableDestinationAccount
from pluggy_sdk.models.acquirer_receivable_related_sale import AcquirerReceivableRelatedSale
from typing import Optional, Set
from typing_extensions import Self

class AcquirerReceivable(BaseModel):
    """
    Acquirer Receivable product
    """ # noqa: E501
    id: StrictStr = Field(description="Primary identifier of the acquirer receivable")
    item_id: StrictStr = Field(description="Primary identifier of the item associated to the acquirer receivable", alias="itemId")
    description: StrictStr = Field(description="Clean description of the acquirer receivable")
    currency_code: StrictStr = Field(description="Currency ISO code", alias="currencyCode")
    var_date: datetime = Field(description="Date when the acquirer receivable was received", alias="date")
    gross_amount: Union[StrictFloat, StrictInt] = Field(description="Acquirer sale gross amount", alias="grossAmount")
    payment_id: Optional[StrictStr] = Field(default=None, alias="paymentId")
    settlement_status: Optional[StrictStr] = Field(default=None, description="Status of the payment", alias="settlementStatus")
    card_flag: Optional[StrictStr] = Field(default=None, description="Flag of the card used", alias="cardFlag")
    net_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Acquirer receivable net amount", alias="netAmount")
    destination_account: Optional[AcquirerReceivableDestinationAccount] = Field(default=None, alias="destinationAccount")
    related_sales: Optional[List[AcquirerReceivableRelatedSale]] = Field(default=None, description="Sales related to the receivable", alias="relatedSales")
    __properties: ClassVar[List[str]] = ["id", "itemId", "description", "currencyCode", "date", "grossAmount", "paymentId", "settlementStatus", "cardFlag", "netAmount", "destinationAccount", "relatedSales"]

    @field_validator('settlement_status')
    def settlement_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PAID', 'SENT', 'REJECTED', 'EXPECTED', 'OTHER']):
            raise ValueError("must be one of enum values ('PAID', 'SENT', 'REJECTED', 'EXPECTED', 'OTHER')")
        return value

    @field_validator('card_flag')
    def card_flag_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['VISA', 'MASTERCARD', 'AMEX', 'ELO', 'CABAL', 'OTHER']):
            raise ValueError("must be one of enum values ('VISA', 'MASTERCARD', 'AMEX', 'ELO', 'CABAL', 'OTHER')")
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
        """Create an instance of AcquirerReceivable from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of destination_account
        if self.destination_account:
            _dict['destinationAccount'] = self.destination_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in related_sales (list)
        _items = []
        if self.related_sales:
            for _item in self.related_sales:
                if _item:
                    _items.append(_item.to_dict())
            _dict['relatedSales'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AcquirerReceivable from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "itemId": obj.get("itemId"),
            "description": obj.get("description"),
            "currencyCode": obj.get("currencyCode"),
            "date": obj.get("date"),
            "grossAmount": obj.get("grossAmount"),
            "paymentId": obj.get("paymentId"),
            "settlementStatus": obj.get("settlementStatus"),
            "cardFlag": obj.get("cardFlag"),
            "netAmount": obj.get("netAmount"),
            "destinationAccount": AcquirerReceivableDestinationAccount.from_dict(obj["destinationAccount"]) if obj.get("destinationAccount") is not None else None,
            "relatedSales": [AcquirerReceivableRelatedSale.from_dict(_item) for _item in obj["relatedSales"]] if obj.get("relatedSales") is not None else None
        })
        return _obj


