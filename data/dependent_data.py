import sys
sys.path.append('/Users/Tiernan/PycharmProjects/jiekou_automationTest')
from case.getAndPost_test import runmain
from config.get_data import getData
from common.operate_excel import opertate_excel
from jsonpath_rw import jsonpath,parse
import json
class dependentData:
    def __init__(self,case_id):
        self.case_id=case_id
        self.operate_excel=opertate_excel()
        self.data=getData()
        self.runmain = runmain()
    #执行依赖测试，获取结果
    def run_test(self):
        row_num=self.operate_excel.get_row_num(self.case_id)
        request_data=self.data.get_dataFromJson(row_num)
        header=self.data.get_header(row_num)
        method=self.data.get_request_method(row_num)
        url=self.data.get_url(row_num)
        res=self.runmain.run_main(url,method,header,request_data)
        print(type(res))
        return json.loads(res)#dict

        # 根据依赖的key去获取执行依赖测试case的响应,然后返回
    def get_data_forKey(self,row):
        depend_data=self.data.get_depend_key(row)#依赖的响应数据
        #print(type(depend_data))#excel里的数据是str类型
        response_data=self.run_test()
        json_exe=parse(depend_data)
        madle=json_exe.find(response_data)
        return [math.value for math in madle][0]

if __name__ == '__main__':
    order = {
        "data": {
            "_input_charset": "utf-8",
            "body": "慕课网订单-1710141907182334",
            "it_b_pay": "1d",
            "notify_url": "http://order.imooc.com/pay/notifyalipay",
            "out_trade_no": "1710141907182334",#订单号
            "partner": "2088002966755334",
            "payment_type": "1",
            "seller_id": "yangyan01@tcl.com",
            "service": "mobile.securitypay.pay",
            "sign": "kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D",
            "sign_type": "RSA",
            "string": "_input_charset=utf-8&body=慕课网订单-1710141907182334&it_b_pay=1d&notify_url=http://order.imooc.com/pay/notifyalipay&out_trade_no=1710141907182334&partner=2088002966755334&payment_type=1&seller_id=yangyan01@tcl.com&service=mobile.securitypay.pay&subject=慕课网订单-1710141907182334&total_fee=299&sign=kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D&sign_type=RSA",
            "subject": "慕课网订单-1710141907182334",
            "total_fee": 299
        },
        "errorCode": 1000,
        "errorDesc": "成功",
        "status": 1,
        "timestamp": 1507979239100
    }
    res = "data.out_trade_no"

    json_exe = parse(res)
    madle = json_exe.find(order)
    print( [math.value for math in madle][0])


