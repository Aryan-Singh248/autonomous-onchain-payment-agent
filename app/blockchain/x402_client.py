from web3 import Web3
from app.core.config import settings
from app.blockchain.wallet import load_wallet

# Initialize Web3 with Sepolia RPC
w3 = Web3(Web3.HTTPProvider(settings.RPC_URL))


def send_payment(to_address: str, amount_wei: int) -> str:
    if not w3.is_connected():
        raise RuntimeError("Web3 RPC not connected")

    wallet = load_wallet(w3)

    nonce = w3.eth.get_transaction_count(wallet["address"])

    tx = {
        "nonce": nonce,
        "to": Web3.to_checksum_address(to_address),
        "value": amount_wei,
        "gas": 21000,
        "gasPrice": w3.eth.gas_price,
        "chainId": 11155111,  # Sepolia
    }

    signed_tx = w3.eth.account.sign_transaction(
        tx, wallet["private_key"]
    )

    tx_hash = w3.eth.send_raw_transaction(
        signed_tx.rawTransaction
    )

    return tx_hash.hex()
