from web3 import Web3
import json

# 连接到本地Ganache网络
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# 检查连接
print("连接状态:", w3.is_connected())

# 部署合约时的账户
deployer_account = w3.eth.accounts[0]

# 已部署的合约地址
contract_address = "0x4999E8909876162c5D195552962A1F8e57289D70"  # 替换为实际地址

# 读取ABI
with open("compiled_contract.json", "r") as file:
    compiled_contract = json.load(file)

abi = compiled_contract['contracts']['SimpleStorage.sol']['SimpleStorage']['abi']

# 创建合约实例
contract = w3.eth.contract(address=contract_address, abi=abi)

# 调用读取函数（不需要发送交易）
stored_data = contract.functions.storedData().call()
print("初始存储的数据:", stored_data)

# 构建交易调用set函数
tx = contract.functions.set(42).build_transaction({
    'from': deployer_account,
    'nonce': w3.eth.get_transaction_count(deployer_account),
    'gas': 200000,
    'gasPrice': w3.to_wei('21', 'gwei')
})

# 发送交易
tx_hash = w3.eth.send_transaction(tx)

# 等待交易被挖掘
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("set(42)交易已完成，块号:", tx_receipt.blockNumber)

# 再次调用读取函数
stored_data = contract.functions.storedData().call()
print("更新后的存储的数据:", stored_data)
