from solcx import compile_standard, install_solc
import json

# 安装指定版本的solc
install_solc('0.8.0')

# 读取Solidity合约
with open('./SimpleStorage.sol', 'r') as file:
    simple_storage_file = file.read()

# 编译合约
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        },
    },
    solc_version="0.8.0",
)

# 保存编译结果到文件（可选）
with open("compiled_contract.json", "w") as file:
    json.dump(compiled_sol, file, indent=4)

# 提取ABI和字节码
abi = compiled_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['abi']
bytecode = compiled_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['evm']['bytecode']['object']

print("ABI:", json.dumps(abi, indent=4))
print("Bytecode:", bytecode)
