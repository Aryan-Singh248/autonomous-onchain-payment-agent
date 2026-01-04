from web3 import Web3
from app.core.config import settings

w3 = Web3(Web3.HTTPProvider(settings.RPC_URL))


def verify_transaction(tx_hash: str) -> bool:
    try:
        receipt = w3.eth.get_transaction_receipt(tx_hash)
        if receipt is None:
            return False

        current_block = w3.eth.block_number
        confirmations = current_block - receipt.blockNumber

        return (
            receipt.status == 1
            and confirmations >= settings.REQUIRED_CONFIRMATIONS
        )
    except Exception:
        return False
