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
from pluggy_sdk.models.smart_transfer_callback_urls import SmartTransferCallbackUrls
from pluggy_sdk.models.smart_transfer_preauthorization_parameter import SmartTransferPreauthorizationParameter
from typing import Optional, Set
from typing_extensions import Self

class CreateSmartTransferPreauthorization(BaseModel):
    """
    Create smart transfer preauthorization request data
    """ # noqa: E501
    connector_id: StrictStr = Field(description="Primary identifier of the connector", alias="connectorId")
    parameters: SmartTransferPreauthorizationParameter
    recipient_ids: List[StrictStr] = Field(alias="recipientIds")
    callback_urls: Optional[SmartTransferCallbackUrls] = Field(default=None, alias="callbackUrls")
    client_preauthorization_id: Optional[StrictStr] = Field(default=None, description="Client preauthorization identifier", alias="clientPreauthorizationId")
    __properties: ClassVar[List[str]] = ["connectorId", "parameters", "recipientIds", "callbackUrls", "clientPreauthorizationId"]

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
        """Create an instance of CreateSmartTransferPreauthorization from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of callback_urls
        if self.callback_urls:
            _dict['callbackUrls'] = self.callback_urls.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateSmartTransferPreauthorization from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "connectorId": obj.get("connectorId"),
            "parameters": SmartTransferPreauthorizationParameter.from_dict(obj["parameters"]) if obj.get("parameters") is not None else None,
            "recipientIds": obj.get("recipientIds"),
            "callbackUrls": SmartTransferCallbackUrls.from_dict(obj["callbackUrls"]) if obj.get("callbackUrls") is not None else None,
            "clientPreauthorizationId": obj.get("clientPreauthorizationId")
        })
        return _obj


