from web3 import Web3
import json

# 连接到本地Ganache网络
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# 检查连接
print("连接状态:", w3.is_connected())

# 获取第一个账户用于部署合约
deployer_account = w3.eth.accounts[0]
print("部署账户:", deployer_account)

# 读取编译后的合约
with open("compiled_contract.json", "r") as file:
    compiled_contract = json.load(file)

abi = compiled_contract['contracts']['SimpleStorage.sol']['SimpleStorage']['abi']
bytecode = compiled_contract['contracts']['SimpleStorage.sol']['SimpleStorage']['evm']['bytecode']['object']

# 创建合约实例
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# 获取交易最新的nonce
nonce = w3.eth.get_transaction_count(deployer_account)

# 建立部署交易
transaction = SimpleStorage.constructor().build_transaction({
    'from': deployer_account,
    'nonce': nonce,
    'gas': 1728712,
    'gasPrice': w3.to_wei('21', 'gwei')
})

# 发送部署交易
tx_hash = w3.eth.send_transaction(transaction)

# 等待交易被挖掘
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print("合约部署成功，地址:", tx_receipt.contractAddress)
