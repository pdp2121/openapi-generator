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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.account_flags import AccountFlags
from openapi_client.models.account_root_with_signer_lists import AccountRootWithSignerLists
from openapi_client.models.queue_data import QueueData
from openapi_client.models.response_warning import ResponseWarning
from typing import Optional, Set
from typing_extensions import Self

class AccountInfoSuccessResponseV1(BaseModel):
    """
    AccountInfoSuccessResponseV1
    """ # noqa: E501
    forwarded: Optional[StrictBool] = Field(default=None, description="Indicates whether the request was forwarded.")
    status: StrictStr = Field(description="The status of the response (e.g., 'success').")
    warning: Optional[StrictStr] = Field(default=None, description="A specific warning type (e.g., 'load').")
    warnings: Optional[List[ResponseWarning]] = Field(default=None, description="An array of response warnings.")
    account_flags: Optional[AccountFlags] = Field(default=None, description="The account's flag statuses.")
    ledger_current_index: Optional[StrictInt] = Field(default=None, description="The ledger index of the current in-progress ledger.")
    ledger_index: Optional[StrictInt] = Field(default=None, description="The ledger index of the ledger version used when retrieving this information.")
    queue_data: Optional[QueueData] = Field(default=None, description="Information about queued transactions sent by this account.")
    validated: Optional[StrictBool] = Field(default=None, description="True if this data is from a validated ledger version; if omitted or set to false, this data is not final.")
    account_data: Optional[AccountRootWithSignerLists] = Field(default=None, description="The AccountRoot ledger object with this account's information, including signer lists, as stored in the ledger.")
    __properties: ClassVar[List[str]] = ["forwarded", "status", "warning", "warnings", "account_flags", "ledger_current_index", "ledger_index", "queue_data", "validated", "account_data"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['success']):
            raise ValueError("must be one of enum values ('success')")
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
        """Create an instance of AccountInfoSuccessResponseV1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in warnings (list)
        _items = []
        if self.warnings:
            for _item in self.warnings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['warnings'] = _items
        # override the default output from pydantic by calling `to_dict()` of account_flags
        if self.account_flags:
            _dict['account_flags'] = self.account_flags.to_dict()
        # override the default output from pydantic by calling `to_dict()` of queue_data
        if self.queue_data:
            _dict['queue_data'] = self.queue_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account_data
        if self.account_data:
            _dict['account_data'] = self.account_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccountInfoSuccessResponseV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "forwarded": obj.get("forwarded"),
            "status": obj.get("status"),
            "warning": obj.get("warning"),
            "warnings": [ResponseWarning.from_dict(_item) for _item in obj["warnings"]] if obj.get("warnings") is not None else None,
            "account_flags": AccountFlags.from_dict(obj["account_flags"]) if obj.get("account_flags") is not None else None,
            "ledger_current_index": obj.get("ledger_current_index"),
            "ledger_index": obj.get("ledger_index"),
            "queue_data": QueueData.from_dict(obj["queue_data"]) if obj.get("queue_data") is not None else None,
            "validated": obj.get("validated"),
            "account_data": AccountRootWithSignerLists.from_dict(obj["account_data"]) if obj.get("account_data") is not None else None
        })
        return _obj


