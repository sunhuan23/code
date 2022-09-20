# 导包
from ddt import ddt,data
import unittest

#测试数据
list1 = [1,2,3,4,5,2,3,2]


class TestCase(unittest.TestCase):
    # @data(1,2,4,5,6)
    # def test_dd1(self,value):
    #     print("dd1---->",value)
    #     self.assertEqual(value,2,'这个数不是2')
    @data(*list1)
    def test_dd2(self,value):
        print("dd1---->",value)
        self.assertEqual(value,2,'这个数不是2')

if __name__ == '__main__':
    unittest.main(verbosity=2)