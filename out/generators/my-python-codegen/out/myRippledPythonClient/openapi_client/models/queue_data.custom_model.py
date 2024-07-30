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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.transactions import Transactions
from typing import Optional, Set
from typing_extensions import Self

class QueueData(BaseModel):
    """
    QueueData
    """ # noqa: E501
    txn_count: Optional[StrictInt] = Field(default=None, description="Number of queued transactions from this address.")
    auth_change_queued: Optional[StrictBool] = Field(default=None, description="Whether a transaction in the queue changes this address's ways of authorizing transactions.")
    lowest_sequence: Optional[StrictInt] = Field(default=None, description="The lowest Sequence Number among transactions queued by this address.")
    highest_sequence: Optional[StrictInt] = Field(default=None, description="The highest Sequence Number among transactions queued by this address.")
    max_spend_drops_total: Optional[StrictStr] = Field(default=None, description="Integer amount of drops of XRP that could be debited from this address if every transaction in the queue consumes the maximum amount of XRP possible.")
    transactions: Optional[List[Transactions]] = Field(default=None, description="Information about each queued transaction from this address.")
    __properties: ClassVar[List[str]] = ["txn_count", "auth_change_queued", "lowest_sequence", "highest_sequence", "max_spend_drops_total", "transactions"]

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
        """Create an instance of QueueData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in transactions (list)
        _items = []
        if self.transactions:
            for _item in self.transactions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transactions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QueueData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "txn_count": obj.get("txn_count"),
            "auth_change_queued": obj.get("auth_change_queued"),
            "lowest_sequence": obj.get("lowest_sequence"),
            "highest_sequence": obj.get("highest_sequence"),
            "max_spend_drops_total": obj.get("max_spend_drops_total"),
            "transactions": [Transactions.from_dict(_item) for _item in obj["transactions"]] if obj.get("transactions") is not None else None
        })
        return _obj


