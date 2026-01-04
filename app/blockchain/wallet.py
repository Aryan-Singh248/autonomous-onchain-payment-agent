from web3 import Web3
import os


def load_wallet(w3: Web3):
    private_key = os.getenv("PRIVATE_KEY")
    address = os.getenv("SENDER_ADDRESS")

    if not private_key or not address:
        raise RuntimeError("Wallet credentials not set")

    return {
        "private_key": private_key,
        "address": Web3.to_checksum_address(address),
    }
