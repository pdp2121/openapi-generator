# coding: utf-8

"""
    XRP Ledger Public API

    A JSON RPC API used to query rippled.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.lookup_by_ledger_request_ledger_index import LookupByLedgerRequestLedgerIndex
from typing import Optional, Set
from typing_extensions import Self

class LookupByLedgerRequest(BaseModel):
    """
    Additional information shared in requests which search for specific ledger data.
    """ # noqa: E501
    ledger_hash: Optional[StrictStr] = Field(default=None, description="A 20-byte hex string for the ledger version to use.")
    ledger_index: Optional[LookupByLedgerRequestLedgerIndex] = None
    __properties: ClassVar[List[str]] = ["ledger_hash", "ledger_index"]

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
        """Create an instance of LookupByLedgerRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ledger_index
        if self.ledger_index:
            _dict['ledger_index'] = self.ledger_index.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LookupByLedgerRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ledger_hash": obj.get("ledger_hash"),
            "ledger_index": LookupByLedgerRequestLedgerIndex.from_dict(obj["ledger_index"]) if obj.get("ledger_index") is not None else None
        })
        return _obj


