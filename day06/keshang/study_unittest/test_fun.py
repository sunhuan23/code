# 导包
from myfun import *
import unittest
# print(add(1, 2))
class MyTest(unittest.TestCase):
    def setUp(self):
        print('每条用例执行前')
    def tearDown(self):
        print('每条用例执行后')
    @classmethod
    def setUpClass(cls):
        print('所有用例执行前')
    @classmethod
    def tearDownClass(cls):
        print('所有用例执行后')


    # @unittest.skip('跳过该方法')
    # @unittest.skipIf(True,'条件满足就跳过')
    # @unittest.skipUnless(True,'条件满足就不跳过')
    def test_add(self):
        # 跳过
        # self.skipTest('跳过这条测试用例')
        print('执行test_add')
        res = add(2,3)
        self.assertEqual(res,5,"与预期不符")
    def test_mul(self):
        print('执行test_mul')
        res1 = multi(2,4)
        self.assertEqual(res1, 8, "与预期不符")
if __name__ == '__main__':
    # unittest.main(verbosity=2)

    suite = unittest.TestSuite()
    suite.addTest(MyTest('test_add'))
    suite.addTest(MyTest('test_mul'))
    suite.addTests([MyTest('test_mul'),MyTest('test_add')])

    runner = unittest.TextTestRunner()
    runner.run(suite)