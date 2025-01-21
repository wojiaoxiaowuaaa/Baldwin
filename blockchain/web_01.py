from web3 import Web3
from loguru import logger
# 连接到本地 Ganache 区块链
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# 检查是否成功连接
# if web3.isConnected():
if web3.is_connected():
    logger.info("Connected to Ganache")
else:
    logger.info("Failed to connect to Ganache")
    exit()

# 获取所有账户
accounts = web3.eth.accounts
logger.info(f"Accounts all: {accounts}")

# 获取第一个账户的余额
account_0 = accounts[0]
balance_0 = web3.eth.get_balance(account_0)
logger.info(f"Balance of account one: {account_0}: {web3.from_wei(balance_0, 'ether')} ETH")

# 获取第二个账户的余额
account_1 = accounts[1]
balance_1 = web3.eth.get_balance(account_1)
logger.info(f"Balance of account two: {account_1}: {web3.from_wei(balance_1, 'ether')} ETH")

# 转账操作：从第一个账户向第二个账户转账 1 ETH
transaction = {
    'to': account_1,
    'from': account_0,
    'value': web3.to_wei(1, 'ether'),
    'gas': 21000,
    'gasPrice': web3.to_wei('50', 'gwei'),
    'nonce': web3.eth.get_transaction_count(account_0),
}

# 使用私钥签名交易
private_key_0 = "0x122a1ebd64d6ddda65e9931b3ed3b5dccb6740adadff9609ae78cb01828925eb"
signed_txn = web3.eth.account.sign_transaction(transaction, private_key_0)

# 发送交易
txn_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
logger.info(f"Transaction hash: {web3.to_hex(txn_hash)}")

# 等待交易被挖矿
txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
logger.info(f"Transaction receipt: {txn_receipt}")

# 再次获取账户余额
balance_0 = web3.eth.get_balance(account_0)
balance_1 = web3.eth.get_balance(account_1)
logger.info(f"New balance of account {account_0}: {web3.from_wei(balance_0, 'ether')} ETH")
logger.info(f"New balance of account {account_1}: {web3.from_wei(balance_1, 'ether')} ETH")
