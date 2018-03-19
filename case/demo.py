import unittest
import requests
import json
import HTMLTestRunner
from mock import mock
from case.mock_test import mock_test
from case.getAndPost_test import runmain
class demo(unittest.TestCase):
    def setUp(self):
        self.run=runmain()

    def test_01(self):
        # url='https://www.imooc.com/passport/user/login'#换post地址
        # data={
        #     'username':'13166427863',
        #     'password':'2ZT33WlvgUyvZVfifBK6cv0GYh05qRKXgYQp/NN8RyvGdYZ78nNTwydiAd5GYuJPcnGPFZFSUH+WVdqOHeVRJI+FRvCaXP+y53E2sQ4Vv/xeaxCCZZdFLO6QTYuqaXXPjnF1KduLSLit/0AqcxYE98aaJRSiiDgqEeOltc6SKkw=',
        #     'remember':'1',
        #     'pwencode':'1',
        #     'browser_key':'837ae2adf8f897f8cc9d47944cb4c7622',
        #     'referer':'https://www.imooc.com'
        # }
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507034803124',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0',
            'errorCode': 1000
        }
        # mock_data=mock.Mock(return_value=data)
        # self.run.run_main=mock_data
        # res=self.run.run_main(url,'POST',data)
        res=mock_test(self.run.run_main,data,url,'POST',data)
        print(type(res))#dict,json
        self.assertEqual(res['errorCode'],1000,'success')

    def test_02(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507034803120',
            'uid': '52491910',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0',
            'errorCode': 1000
        }
        # mock_data = mock.Mock(return_value=data)
        # self.run.run_main = mock_data
        # res=self.run.run_main(url,'POST',data)
        res = mock_test(self.run.run_main, data, url, 'POST', data)
        print(res)
        self.assertEqual(res['errorCode'], 1001, 'fail')

if __name__ == '__main__':
    # filepath='../report/result.html'
    # fp=open(filepath,'wb')
    # suite=unittest.TestSuite()
    # suite.addTest(demo('test_01'))
    # suite.addTest(demo('test_02'))
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
    #                                        title=u'自动化测试报告,测试结果如下：',
    #                                        description=u'用例执行情况：')
    #
    # # 调用add_case函数返回值
    # runner.run(suite)
    unittest.main()


