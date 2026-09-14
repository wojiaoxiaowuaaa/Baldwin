# /usr/bin/python3
# -*- coding=utf-8 -*-
from enum import unique, Enum


@unique
class BikeLifeEnum(Enum):
    WENSHU = "000-运营--test"

    @property
    def get_value(self):
        # print(self.value)  # 使用 self.value 可以访问到当前枚举成员的值，这是因为 self 在这里代表的是枚举成员本身。
        return self.value.split("-")[0]


print(BikeLifeEnum.WENSHU.get_value)
