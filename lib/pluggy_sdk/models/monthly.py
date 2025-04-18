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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class MONTHLY(BaseModel):
    """
    Schedule atribute to generate monthly payments
    """ # noqa: E501
    type: StrictStr = Field(description="Scheduled type")
    start_date: date = Field(alias="startDate")
    day_of_month: Union[Annotated[float, Field(le=30, strict=True, ge=1)], Annotated[int, Field(le=30, strict=True, ge=1)]] = Field(description="Day of the month on which each payment will occur. For example, if '10', the first payment will occur on the next 10th day of the month after the start date, or the same day if it is already 10th, and every 10th day after that.", alias="dayOfMonth")
    occurrences: Optional[Union[Annotated[float, Field(le=23, strict=True, ge=3)], Annotated[int, Field(le=23, strict=True, ge=3)]]] = Field(default=None, description="Under the specified schedule frequency, how many payments will be scheduled to occur.")
    __properties: ClassVar[List[str]] = ["type", "startDate", "dayOfMonth", "occurrences"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['MONTHLY']):
            raise ValueError("must be one of enum values ('MONTHLY')")
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
        """Create an instance of MONTHLY from a JSON string"""
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
        """Create an instance of MONTHLY from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "startDate": obj.get("startDate"),
            "dayOfMonth": obj.get("dayOfMonth"),
            "occurrences": obj.get("occurrences")
        })
        return _obj


