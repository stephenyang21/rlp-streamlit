from eth_typing import HexStr
from eth_utils import keccak, to_bytes
from web3 import Web3
from web3.auto import w3
from Transaction import Transaction
from DecodedTx import DecodedTx

import rlp

def hex_to_bytes(data: str) -> bytes:
    return to_bytes(hexstr=HexStr(data))

def decode_raw_tx(raw_tx: str):
    tx = rlp.decode(hex_to_bytes(raw_tx), Transaction)
    hash_tx = Web3.to_hex(keccak(hex_to_bytes(raw_tx)))
    from_ = w3.eth.account.recover_transaction(raw_tx)
    to = w3.to_checksum_address(tx.to) if tx.to else None
    data = w3.to_hex(tx.data)
    r = hex(tx.r)
    s = hex(tx.s)
    chain_id = (tx.v - 35) // 2 if tx.v % 2 else (tx.v - 36) // 2
    return DecodedTx(hash_tx, from_, to, tx.nonce, tx.gas, tx.gas_price, tx.value, data, chain_id, r, s, tx.v)