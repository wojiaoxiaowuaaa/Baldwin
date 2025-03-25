// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 public storedData;

    event DataStored(uint256 data);

    // 存储数据
    function set(uint256 x) public {
        storedData = x;
        emit DataStored(x);
    }

    // 读取数据：由于声明为public，自动生成getter，所以可以省略
    // function get() public view returns (uint256) {
    //     return storedData;
    // }
}
