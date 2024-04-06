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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Webhook(BaseModel):
    """
    
    """ # noqa: E501
    id: StrictStr = Field(description="UUID identifier for the entity")
    url: StrictStr = Field(description="Url to be notified of item changes")
    event: StrictStr
    disabled_at: Optional[datetime] = Field(default=None, description="Date when the webhook was disabled", alias="disabledAt")
    created_at: Optional[datetime] = Field(default=None, description="Date when it was created", alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, description="Date of the last update", alias="updatedAt")
    __properties: ClassVar[List[str]] = ["id", "url", "event", "disabledAt", "createdAt", "updatedAt"]

    @field_validator('event')
    def event_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['all', 'item/created', 'item/updated', 'item/error', 'item/deleted', 'item/waiting_user_input', 'item/waiting_user_action', 'item/login_succeeded', 'connector/status_updated']):
            raise ValueError("must be one of enum values ('all', 'item/created', 'item/updated', 'item/error', 'item/deleted', 'item/waiting_user_input', 'item/waiting_user_action', 'item/login_succeeded', 'connector/status_updated')")
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
        """Create an instance of Webhook from a JSON string"""
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
        """Create an instance of Webhook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "url": obj.get("url"),
            "event": obj.get("event"),
            "disabledAt": obj.get("disabledAt"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj

