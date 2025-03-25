"""
This module provides functionality for managing Ethereum transactions using Web3.py.

It includes a class EthereumTransactionManager that handles connections to a local Ganache instance,
account management, balance checking, and Ether transfers between accounts.
"""
import os
import sys
from eth_typing import ChecksumAddress
from loguru import logger
from web3 import Web3 
from dotenv import load_dotenv

load_dotenv()

pri_key = os.environ.get('private_key')

class EthereumTransactionManager:
    """
    A class to manage Ethereum transactions using Web3.py.
    This class provides methods to connect to a Ganache instance, retrieve account information,
    check balances, and perform Ether transfers between accounts.
    Attributes:
        GANACHE_URL (str): The URL of the Ganache instance.
        GAS_LIMIT (int): The gas limit for transactions.
        GAS_PRICE (str): The gas price in Gwei.
        TRANSFER_AMOUNT (int): The default amount of Ether to transfer.
    """

    GANACHE_URL = "http://127.0.0.1:8545"
    GAS_LIMIT = 21000
    GAS_PRICE = '50'
    TRANSFER_AMOUNT = 1

    def __init__(self):
        """
        Initialize the EthereumTransactionManager by connecting to Ganache and retrieving accounts.
        """
        self.web3 = self.connect_to_ganache()
        self.accounts = self.get_accounts()

    def connect_to_ganache(self) -> Web3:
        web3 = Web3(Web3.HTTPProvider(self.GANACHE_URL))
        if not web3.is_connected():
            logger.error("Failed to connect to Ganache")
            sys.exit(1)
        logger.info("Connected to Ganache")
        return web3

    def get_accounts(self) -> tuple[ChecksumAddress]:
        accounts = self.web3.eth.accounts
        logger.info(f"Accounts: {accounts}")
        return accounts

    def get_balance(self, account) -> float:
        balance = self.web3.eth.get_balance(account)
        return self.web3.from_wei(balance, 'ether')

    def log_balances(self):
        """
        Log the balances of the first two accounts.
        """
        for i, account in enumerate(self.accounts[:2], 1):
            balance = self.get_balance(account)
            logger.info(f"Balance of account {i}: {account}: {balance} ETH")

    def transfer_eth(self, from_account, to_account: str, amount: int, private_key: str) -> str:
        transaction = {
            'to': to_account,
            'from': from_account,
            'value': self.web3.to_wei(amount, 'ether'),
            'gas': self.GAS_LIMIT,
            'gasPrice': self.web3.to_wei(self.GAS_PRICE, 'gwei'),
            'nonce': self.web3.eth.get_transaction_count(from_account),
        }

        signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key)
        txn_hash = self.web3.eth.send_raw_transaction(signed_txn.raw_transaction)
        return self.web3.to_hex(txn_hash)

    def execute_transaction(self):
        """
        Execute a sample transaction, transferring Ether between the first two accounts.
        """
        self.log_balances()
        private_key = pri_key
        txn_hash = self.transfer_eth(self.accounts[0], self.accounts[1], self.TRANSFER_AMOUNT, private_key)
        logger.info(f"Transaction hash: {txn_hash}")
        txn_receipt = self.web3.eth.wait_for_transaction_receipt(txn_hash)
        logger.info(f"Transaction receipt: {txn_receipt}")
        self.log_balances()

def main():
    manager = EthereumTransactionManager()
    manager.execute_transaction()

if __name__ == "__main__":
    main()
