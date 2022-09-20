from ddt import ddt,data,unpack
import unittest
# 测试数据
list1 = [[1,2],[3,3],[3,4]]

@ddt
class TestCase(unittest.TestCase):
    # @data([1,2],[3,3],[3,4])
    # @unpack
    # def test_ddt1(self,value,value1):
    #     print(f'第一个数是{value},第二个数是{value1}')
    #     self.assertEqual(value,value1,'两个数不一致')
    @data(*list1)
    @unpack
    def test_ddt1(self,value,value1):
        print(f'第一个数是{value},第二个数是{value1}')
        self.assertEqual(value,value1,'两个数不一致')

if __name__ == '__main__':
    unittest.main(verbosity=2)