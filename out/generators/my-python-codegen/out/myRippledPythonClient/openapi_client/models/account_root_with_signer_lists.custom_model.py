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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.signer_list import SignerList
from typing import Optional, Set
from typing_extensions import Self

class AccountRootWithSignerLists(BaseModel):
    """
    AccountRootWithSignerLists
    """ # noqa: E501
    account: StrictStr = Field(description="The identifying (classic) address of this account.", alias="Account")
    account_txn_id: Optional[StrictStr] = Field(default=None, description="The identifying hash of the transaction most recently sent by this account. (Optional)", alias="AccountTxnID")
    ammid: Optional[StrictStr] = Field(default=None, description="The ledger entry ID of the corresponding AMM ledger entry. (Optional)", alias="AMMID")
    balance: Optional[StrictStr] = Field(default=None, description="The account's current XRP balance in drops, represented as a string. (Optional)", alias="Balance")
    burned_nf_tokens: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="How many total of this account's issued non-fungible tokens have been burned. (Optional)", alias="BurnedNFTokens")
    domain: Optional[StrictStr] = Field(default=None, description="A domain associated with this account. Cannot be more than 256 bytes in length. (Optional)", alias="Domain")
    email_hash: Optional[StrictStr] = Field(default=None, description="The md5 hash of an email address. Clients can use this to look up an avatar. (Optional)", alias="EmailHash")
    first_nf_token_sequence: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The account's Sequence Number at the time it minted its first non-fungible-token. (Optional)", alias="FirstNFTokenSequence")
    ledger_entry_type: StrictStr = Field(description="The value 0x0061, mapped to the string AccountRoot, indicates that this is an AccountRoot object.", alias="LedgerEntryType")
    message_key: Optional[StrictStr] = Field(default=None, description="A public key that may be used to send encrypted messages to this account. Must be exactly 33 bytes. (Optional)", alias="MessageKey")
    minted_nf_tokens: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="How many total non-fungible tokens have been minted by and on behalf of this account. (Optional)", alias="MintedNFTokens")
    nf_token_minter: Optional[StrictStr] = Field(default=None, description="Another account that can mint non-fungible tokens on behalf of this account. (Optional)", alias="NFTokenMinter")
    owner_count: Union[StrictFloat, StrictInt] = Field(description="The number of objects this account owns in the ledger, which contributes to its owner reserve.", alias="OwnerCount")
    previous_txn_id: StrictStr = Field(description="The identifying hash of the transaction that most recently modified this object.", alias="PreviousTxnID")
    previous_txn_lgr_seq: Union[StrictFloat, StrictInt] = Field(description="The index of the ledger that contains the transaction that most recently modified this object.", alias="PreviousTxnLgrSeq")
    regular_key: Optional[StrictStr] = Field(default=None, description="The address of a key pair that can be used to sign transactions for this account instead of the master key. (Optional)", alias="RegularKey")
    sequence: Union[StrictFloat, StrictInt] = Field(description="The sequence number of the next valid transaction for this account.", alias="Sequence")
    ticket_count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="How many Tickets this account owns in the ledger. (Optional)", alias="TicketCount")
    tick_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="How many significant digits to use for exchange rates of Offers involving currencies issued by this address. (Optional)", alias="TickSize")
    transfer_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="A transfer fee to charge other users for sending currency issued by this account to each other. (Optional)", alias="TransferRate")
    wallet_locator: Optional[StrictStr] = Field(default=None, description="An arbitrary 256-bit value that users can set. (Optional)", alias="WalletLocator")
    wallet_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Unused. (The code supports this field but there is no way to set it.) (Optional)", alias="WalletSize")
    signer_lists: Optional[List[SignerList]] = Field(default=None, description="Array of SignerList ledger objects associated with this account for Multi-Signing.")
    __properties: ClassVar[List[str]] = ["Account", "AccountTxnID", "AMMID", "Balance", "BurnedNFTokens", "Domain", "EmailHash", "FirstNFTokenSequence", "LedgerEntryType", "MessageKey", "MintedNFTokens", "NFTokenMinter", "OwnerCount", "PreviousTxnID", "PreviousTxnLgrSeq", "RegularKey", "Sequence", "TicketCount", "TickSize", "TransferRate", "WalletLocator", "WalletSize", "signer_lists"]

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
        """Create an instance of AccountRootWithSignerLists from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in signer_lists (list)
        _items = []
        if self.signer_lists:
            for _item in self.signer_lists:
                if _item:
                    _items.append(_item.to_dict())
            _dict['signer_lists'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccountRootWithSignerLists from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Account": obj.get("Account"),
            "AccountTxnID": obj.get("AccountTxnID"),
            "AMMID": obj.get("AMMID"),
            "Balance": obj.get("Balance"),
            "BurnedNFTokens": obj.get("BurnedNFTokens"),
            "Domain": obj.get("Domain"),
            "EmailHash": obj.get("EmailHash"),
            "FirstNFTokenSequence": obj.get("FirstNFTokenSequence"),
            "LedgerEntryType": obj.get("LedgerEntryType"),
            "MessageKey": obj.get("MessageKey"),
            "MintedNFTokens": obj.get("MintedNFTokens"),
            "NFTokenMinter": obj.get("NFTokenMinter"),
            "OwnerCount": obj.get("OwnerCount"),
            "PreviousTxnID": obj.get("PreviousTxnID"),
            "PreviousTxnLgrSeq": obj.get("PreviousTxnLgrSeq"),
            "RegularKey": obj.get("RegularKey"),
            "Sequence": obj.get("Sequence"),
            "TicketCount": obj.get("TicketCount"),
            "TickSize": obj.get("TickSize"),
            "TransferRate": obj.get("TransferRate"),
            "WalletLocator": obj.get("WalletLocator"),
            "WalletSize": obj.get("WalletSize"),
            "signer_lists": [SignerList.from_dict(_item) for _item in obj["signer_lists"]] if obj.get("signer_lists") is not None else None
        })
        return _obj


