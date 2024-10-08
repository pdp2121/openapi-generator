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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.currency_amount import CurrencyAmount
from openapi_client.models.path import Path
from typing import Optional, Set
from typing_extensions import Self

class PaymentTransactionV2(BaseModel):
    """
    PaymentTransactionV2
    """ # noqa: E501
    deliver_max: CurrencyAmount = Field(description="Only available in API v2. The maximum amount of currency to deliver. For non-XRP amounts, the nested field names MUST be lower-case. If the tfPartialPayment flag is set, deliver up to this amount instead. New in: rippled 2.0.0", alias="DeliverMax")
    transaction_type: StrictStr = Field(description="The type of transaction. Valid transaction types include: Payment, OfferCreate, TrustSet, and many others. ", alias="TransactionType")
    deliver_min: Optional[CurrencyAmount] = Field(default=None, description="(Optional) Minimum amount of destination currency this transaction should deliver. Only valid if this is a partial payment. For non-XRP amounts, the nested field names are lower-case.", alias="DeliverMin")
    destination: StrictStr = Field(description="The unique address of the account receiving the payment.", alias="Destination")
    destination_tag: Optional[StrictInt] = Field(default=None, description="(Optional) Arbitrary tag that identifies the reason for the payment to the destination, or a hosted recipient to pay.", alias="DestinationTag")
    invoice_id: Optional[StrictStr] = Field(default=None, description="(Optional) Arbitrary 256-bit hash representing a specific reason or identifier for this payment.", alias="InvoiceID")
    paths: Optional[List[List[Path]]] = Field(default=None, description="(Optional, auto-fillable) Array of payment paths to be used for this transaction. Must be omitted for XRP-to-XRP transactions.", alias="Paths")
    send_max: Optional[CurrencyAmount] = Field(default=None, description="(Optional) Highest amount of source currency this transaction is allowed to cost, including transfer fees, exchange rates, and slippage. Does not include the XRP destroyed as a cost for submitting the transaction. For non-XRP amounts, the nested field names MUST be lower-case. Must be supplied for cross-currency/cross-issue payments. Must be omitted for XRP-to-XRP payments.", alias="SendMax")
    account: StrictStr = Field(description="The unique address of the account that initiated the transaction.", alias="Account")
    fee: Optional[StrictStr] = Field(default=None, description="Integer amount of XRP, in drops, to be destroyed as a cost for distributing this transaction to the network. Some transaction types have different minimum requirements. See Transaction Cost for details.", alias="Fee")
    sequence: Optional[StrictInt] = Field(default=None, description="The sequence number of the account sending the transaction. A transaction is only valid if the Sequence number is exactly 1 greater than the previous transaction from the same account. The special case 0 means the transaction is using a Ticket instead.", alias="Sequence")
    account_txn_id: Optional[StrictStr] = Field(default=None, description="Hash value identifying another transaction. If provided, this transaction is only valid if the sending account's previously-sent transaction matches the provided hash.", alias="AccountTxnID")
    flags: Optional[StrictInt] = Field(default=None, description="Set of bit-flags for this transaction.", alias="Flags")
    last_ledger_sequence: Optional[StrictInt] = Field(default=None, description="Highest ledger index this transaction can appear in. Specifying this field places a strict upper limit on how long the transaction can wait to be validated or rejected.", alias="LastLedgerSequence")
    memos: Optional[List[Dict[str, Any]]] = Field(default=None, description="Additional arbitrary information used to identify this transaction.", alias="Memos")
    network_id: Optional[StrictInt] = Field(default=None, description="The network ID of the chain this transaction is intended for. MUST BE OMITTED for Mainnet and some test networks. REQUIRED on chains whose network ID is 1025 or higher.", alias="NetworkID")
    signers: Optional[List[Dict[str, Any]]] = Field(default=None, description="Array of objects that represent a multi-signature which authorizes this transaction.", alias="Signers")
    source_tag: Optional[StrictInt] = Field(default=None, description="Arbitrary integer used to identify the reason for this payment, or a sender on whose behalf this transaction is made.", alias="SourceTag")
    signing_pub_key: Optional[StrictStr] = Field(default=None, description="Hex representation of the public key that corresponds to the private key used to sign this transaction. If an empty string, indicates a multi-signature is present in the Signers field instead.", alias="SigningPubKey")
    ticket_sequence: Optional[StrictInt] = Field(default=None, description="The sequence number of the ticket to use in place of a Sequence number. If this is provided, Sequence must be 0. Cannot be used with AccountTxnID.", alias="TicketSequence")
    txn_signature: Optional[StrictStr] = Field(default=None, description="The signature that verifies this transaction as originating from the account it says it is from.", alias="TxnSignature")
    __properties: ClassVar[List[str]] = ["TransactionType", "DeliverMin", "Destination", "DestinationTag", "InvoiceID", "Paths", "SendMax", "Account", "Fee", "Sequence", "AccountTxnID", "Flags", "LastLedgerSequence", "Memos", "NetworkID", "Signers", "SourceTag", "SigningPubKey", "TicketSequence", "TxnSignature"]

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
        """Create an instance of PaymentTransactionV2 from a JSON string"""
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

        def camel_to_snake(name):
            return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # Convert keys to snake case
        _dict_snake_case = {camel_to_snake(key): value for key, value in _dict.items()}
        
        # override the default output from pydantic by calling `to_dict()` of deliver_min
        if self.deliver_min:
            _dict_snake_case['deliver_min'] = self.deliver_min.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in paths (list of list)
        _items = []
        if self.paths:
            for _item in self.paths:
                if _item:
                    _items.append(
                         [_inner_item.to_dict() for _inner_item in _item if _inner_item is not None]
                    )
            _dict_snake_case['paths'] = _items
        # override the default output from pydantic by calling `to_dict()` of send_max
        if self.send_max:
            _dict_snake_case['send_max'] = self.send_max.to_dict()
        
        return _dict_snake_case

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentTransactionV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "TransactionType": obj.get("TransactionType"),
            "DeliverMin": CurrencyAmount.from_dict(obj["DeliverMin"]) if obj.get("DeliverMin") is not None else None,
            "Destination": obj.get("Destination"),
            "DestinationTag": obj.get("DestinationTag"),
            "InvoiceID": obj.get("InvoiceID"),
            "Paths": [
                    [Path.from_dict(_inner_item) for _inner_item in _item]
                    for _item in obj["Paths"]
                ] if obj.get("Paths") is not None else None,
            "SendMax": CurrencyAmount.from_dict(obj["SendMax"]) if obj.get("SendMax") is not None else None,
            "Account": obj.get("Account"),
            "Fee": obj.get("Fee"),
            "Sequence": obj.get("Sequence"),
            "AccountTxnID": obj.get("AccountTxnID"),
            "Flags": obj.get("Flags"),
            "LastLedgerSequence": obj.get("LastLedgerSequence"),
            "Memos": obj.get("Memos"),
            "NetworkID": obj.get("NetworkID"),
            "Signers": obj.get("Signers"),
            "SourceTag": obj.get("SourceTag"),
            "SigningPubKey": obj.get("SigningPubKey"),
            "TicketSequence": obj.get("TicketSequence"),
            "TxnSignature": obj.get("TxnSignature")
        })
        return _obj


