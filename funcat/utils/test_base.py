# -*- coding: utf-8 -*-
import unittest

import numpy as np



class MyTestCase(unittest.TestCase):
    """测试单元基类
    """
    @classmethod
    def setUpClass(cls) -> None:
        from funcat import QuantaxisDataBackend as BACKEND, set_data_backend
        set_data_backend(BACKEND())
        cls.BE = BACKEND()

    def fakeMarketData(self, arr=None):
        from funcat.time_series import MarketDataSeries
        """产生模拟交易数据,便于校验数据"""
        if arr is None:
            fakeData = np.array(range(100))
        else:
            fakeData = arr
        name = "fake"
        dtype = float
        cls = type("{}Series".format(name.capitalize()), (MarketDataSeries,), {"name": name, "dtype": dtype})
        obj = cls(dynamic_update=False)
        obj._series = fakeData
        print(f"{obj}, {obj.series}")
        return obj