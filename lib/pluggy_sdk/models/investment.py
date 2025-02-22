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
from pluggy_sdk.models.investment_metadata import InvestmentMetadata
from typing import Optional, Set
from typing_extensions import Self

class Investment(BaseModel):
    """
    Investment representing a specific asset
    """ # noqa: E501
    id: StrictStr = Field(description="Primary identifier")
    item_id: StrictStr = Field(description="Identifier of the item linked to the investment", alias="itemId")
    type: StrictStr = Field(description="Investment Asset type")
    subtype: Optional[StrictStr] = Field(default=None, description="Investment subtype, depends on the type")
    number: Optional[StrictStr] = Field(default=None, description="Reference number for this holder's asset")
    balance: Union[StrictFloat, StrictInt] = Field(description="The current net balance amount of the investment")
    name: StrictStr = Field(description="Name on the provider")
    last_month_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The performance rate of the investment in the last month", alias="lastMonthRate")
    last_twelve_months_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The performance rate of the investment in the last 12 months", alias="lastTwelveMonthsRate")
    annual_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The performance rate of the investment in the last year", alias="annualRate")
    currency_code: StrictStr = Field(description="Currency ISO code for the amounts", alias="currencyCode")
    code: Optional[StrictStr] = Field(default=None, description="Associated Code for the investment. For example, the code for a mutual fund is the CNPJ")
    isin: Optional[StrictStr] = Field(default=None, description="12-character ISIN, a globally unique identifier")
    value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Quota's current value at \"date\"")
    quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Quantity of quota at disposal")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Gross amount of the investment")
    taxes: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Income taxes applied to the investment")
    taxes2: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Financial taxes applied to the investment")
    var_date: datetime = Field(description="Value's quota date", alias="date")
    owner: Optional[StrictStr] = Field(default=None, description="Owner/beneficiary associated with the investment")
    amount_profit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Profit/Loss to date over the investment", alias="amountProfit")
    amount_withdrawal: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount available to withdraw", alias="amountWithdrawal")
    amount_original: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Amount originally invested", alias="amountOriginal")
    metadata: Optional[InvestmentMetadata] = Field(default=None, description="Security Portability details")
    due_date: Optional[datetime] = Field(default=None, description="Expiration Date", alias="dueDate")
    issuer: Optional[StrictStr] = Field(default=None, description="The entity that issued the investment")
    issuer_cnpj: Optional[StrictStr] = Field(default=None, description="The entity CNPJ that issued the investment", alias="issuerCNPJ")
    issue_date: Optional[datetime] = Field(default=None, description="The date that the investment was issued", alias="issueDate")
    rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Fixed rate percentage applied to the investment")
    rate_type: Optional[StrictStr] = Field(default=None, description="Type of fixed-rate", alias="rateType")
    fixed_annual_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Fixed income annual rate", alias="fixedAnnualRate")
    status: Optional[StrictStr] = Field(default=None, description="Current status of the investment enum value")
    __properties: ClassVar[List[str]] = ["id", "itemId", "type", "subtype", "number", "balance", "name", "lastMonthRate", "lastTwelveMonthsRate", "annualRate", "currencyCode", "code", "isin", "value", "quantity", "amount", "taxes", "taxes2", "date", "owner", "amountProfit", "amountWithdrawal", "amountOriginal", "metadata", "dueDate", "issuer", "issuerCNPJ", "issueDate", "rate", "rateType", "fixedAnnualRate", "status"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['COE', 'EQUITY', 'ETF', 'FIXED_INCOME', 'MUTUAL_FUND', 'SECURITY', 'OTHER']):
            raise ValueError("must be one of enum values ('COE', 'EQUITY', 'ETF', 'FIXED_INCOME', 'MUTUAL_FUND', 'SECURITY', 'OTHER')")
        return value

    @field_validator('subtype')
    def subtype_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['STRUCTURED_NOTE', 'STOCK', 'ETF', 'REAL_ESTATE_FUND', 'BDR', 'DERIVATIVES', 'OPTION', 'TREASURY', 'LCI', 'LCA', 'LF', 'CDB', 'CRI', 'CRA', 'CORPORATE_DEBT', 'LC', 'DEBENTURES', 'INVESTMENT_FUND', 'MULTIMARKET_FUND', 'FIXED_INCOME_FUND', 'STOCK_FUND', 'ETF_FUND', 'OFFSHORE_FUND', 'FIP_FUND', 'EXCHANGE_FUND', 'RETIREMENT', 'OTHER']):
            raise ValueError("must be one of enum values ('STRUCTURED_NOTE', 'STOCK', 'ETF', 'REAL_ESTATE_FUND', 'BDR', 'DERIVATIVES', 'OPTION', 'TREASURY', 'LCI', 'LCA', 'LF', 'CDB', 'CRI', 'CRA', 'CORPORATE_DEBT', 'LC', 'DEBENTURES', 'INVESTMENT_FUND', 'MULTIMARKET_FUND', 'FIXED_INCOME_FUND', 'STOCK_FUND', 'ETF_FUND', 'OFFSHORE_FUND', 'FIP_FUND', 'EXCHANGE_FUND', 'RETIREMENT', 'OTHER')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ACTIVE', 'PENDING', 'TOTAL_WITHDRAWAL']):
            raise ValueError("must be one of enum values ('ACTIVE', 'PENDING', 'TOTAL_WITHDRAWAL')")
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
        """Create an instance of Investment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Investment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "itemId": obj.get("itemId"),
            "type": obj.get("type"),
            "subtype": obj.get("subtype"),
            "number": obj.get("number"),
            "balance": obj.get("balance"),
            "name": obj.get("name"),
            "lastMonthRate": obj.get("lastMonthRate"),
            "lastTwelveMonthsRate": obj.get("lastTwelveMonthsRate"),
            "annualRate": obj.get("annualRate"),
            "currencyCode": obj.get("currencyCode"),
            "code": obj.get("code"),
            "isin": obj.get("isin"),
            "value": obj.get("value"),
            "quantity": obj.get("quantity"),
            "amount": obj.get("amount"),
            "taxes": obj.get("taxes"),
            "taxes2": obj.get("taxes2"),
            "date": obj.get("date"),
            "owner": obj.get("owner"),
            "amountProfit": obj.get("amountProfit"),
            "amountWithdrawal": obj.get("amountWithdrawal"),
            "amountOriginal": obj.get("amountOriginal"),
            "metadata": InvestmentMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "dueDate": obj.get("dueDate"),
            "issuer": obj.get("issuer"),
            "issuerCNPJ": obj.get("issuerCNPJ"),
            "issueDate": obj.get("issueDate"),
            "rate": obj.get("rate"),
            "rateType": obj.get("rateType"),
            "fixedAnnualRate": obj.get("fixedAnnualRate"),
            "status": obj.get("status")
        })
        return _obj


