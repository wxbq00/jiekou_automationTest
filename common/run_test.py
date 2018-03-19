import sys
sys.path.append('/Users/Tiernan/PycharmProjects/jiekou_automationTest')
from case.getAndPost_test import runmain
from config.get_data import getData
from common.common_util import common_util
from common.operate_excel import opertate_excel
from data.dependent_data import dependentData
from common.operation_header import operateHeader
from common.operate_json import operate_json
class RunTest:
    def __init__(self):
        self.operate_excel=opertate_excel()
        self.data=getData()
        self.run_main=runmain()
        self.common_util=common_util()

    #程序执行入口
    def go_on_run(self):
        pass_count=[]
        fail_count=[]
        res=None
        rows_count=self.data.get_lines()
        for i in range(0,rows_count):#行数
            is_run=self.data.get_isRun(i)
            if is_run:
                url=self.data.get_url(i)
                method=self.data.get_request_method(i)
                header=self.data.get_header(i)
                request_data=self.data.get_dataFromJson(i)
                expect_result=self.data.get_expect_result(i)
                depend_case=self.data.is_depend(i)#case依赖的id

                if depend_case!=None:
                    self.dependent_data=dependentData(depend_case)#返回的响应结果
                    dependent_response_data=self.dependent_data.get_data_forKey(i)#根据依赖的key去获取执行依赖测试case的响应数据,然后返回
                    depend_key=self.data.get_depend_field(i)#依赖的字段
                    request_data[depend_key]=dependent_response_data
                else:
                    res=self.run_main.run_main(url,method,request_data)

                if header=='write':
                    res = self.run_main.run_main(url, method, request_data)
                    op_header=operateHeader(res)
                    op_header.write_cookies()
                elif header=='yes':
                    op_json=operate_json('../data/cookie.json')
                    cookie=op_json.get_data('apsid')
                    cookies={
                        'apsid':cookie
                    }
                    res=self.run_main.run_main(url,method,request_data,cookies)
                else:
                    res=self.run_main.run_main(url,method,request_data)

                if str(expect_result) in res:
                    self.data.write_data(i,'pass') 
                    pass_count.append(i)


                else:
                    self.data.write_data(i,res)
                    fail_count.append(i)



if __name__ == '__main__':
    run=RunTest()
    run.go_on_run()




