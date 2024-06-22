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
from pluggy_sdk.models.create_item_parameters import CreateItemParameters
from typing import Optional, Set
from typing_extensions import Self

class CreateItem(BaseModel):
    """
    Create Item Request
    """ # noqa: E501
    connector_id: Union[StrictFloat, StrictInt] = Field(description="Primary identifier of the connector", alias="connectorId")
    parameters: CreateItemParameters
    webhook_url: Optional[StrictStr] = Field(default=None, description="Url to be notified of item changes", alias="webhookUrl")
    client_user_id: Optional[StrictStr] = Field(default=None, description="Client's identifier for the user, it can be a ID, UUID or even an email.", alias="clientUserId")
    products: Optional[List[StrictStr]] = Field(default=None, description="Products to be collected in the connection")
    __properties: ClassVar[List[str]] = ["connectorId", "parameters", "webhookUrl", "clientUserId", "products"]

    @field_validator('products')
    def products_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['ACCOUNTS', 'CREDIT_CARDS', 'TRANSACTIONS', 'PAYMENT_DATA', 'INVESTMENTS', 'INVESTMENTS_TRANSACTIONS', 'IDENTITY', 'BROKERAGE_NOTE', 'OPPORTUNITIES', 'PORTFOLIO', 'INCOME_REPORTS', 'MOVE_SECURITY', 'LOANS', 'ACQUIRER_OPERATIONS']):
                raise ValueError("each list item must be one of ('ACCOUNTS', 'CREDIT_CARDS', 'TRANSACTIONS', 'PAYMENT_DATA', 'INVESTMENTS', 'INVESTMENTS_TRANSACTIONS', 'IDENTITY', 'BROKERAGE_NOTE', 'OPPORTUNITIES', 'PORTFOLIO', 'INCOME_REPORTS', 'MOVE_SECURITY', 'LOANS', 'ACQUIRER_OPERATIONS')")
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
        """Create an instance of CreateItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['parameters'] = self.parameters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "connectorId": obj.get("connectorId"),
            "parameters": CreateItemParameters.from_dict(obj["parameters"]) if obj.get("parameters") is not None else None,
            "webhookUrl": obj.get("webhookUrl"),
            "clientUserId": obj.get("clientUserId"),
            "products": obj.get("products")
        })
        return _obj


