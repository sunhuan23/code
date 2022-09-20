from ddt import ddt,data,unpack
import unittest
# 测试数据
list1 = [{'value':1,"value1":2},{'value':1,"value1":1},{'value':2,"value1":2}]

@ddt
class TestCase(unittest.TestCase):
    # @data({'value':1,"value1":2})
    # @unpack
    # def test_ddt1(self,value,value1):
    #     print(f'第一个数是{value},第二个数是{value1}')
    #     self.assertEqual(value,value1,'两个数不想等')

    @data(*list1)
    @unpack
    def test_ddt1(self,value,value1):
        print(f'第一个数是{value},第二个数是{value1}')
        self.assertEqual(value,value1,'两个数不想等')
if __name__ == '__main__':
    unittest.main(verbosity=2)