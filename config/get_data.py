#coding=utf-8
from common.operate_excel import opertate_excel
from common.operate_json import operate_json
import config.data_config
from common.connectDB import OperationMysql

#从excel中获取字段的值
class getData:
    def __init__(self):
        self.operate_excel=opertate_excel()
        self.operate_json=operate_json()

    def get_lines(self):#获取excel行数
        return self.operate_excel.get_colnum()
    #获取是否执行

    def get_isRun(self,row):
        flag=None
        col=int(config.data_config.get_isRun())#直接使用这个类
        run=self.operate_excel.get_cellvalue(row,col)
        if run=='yes':
            flag=True
        else:
            flag=False
        return flag
    #是否携带header
    def get_header(self,row):
        flag = None
        col = int(config.data_config.get_header())  # 直接使用这个类
        header = self.operate_excel.get_cellvalue(row, col)
        if header!='':
            flag = True
        else:
            flag = False
        return flag
    #获取请求方式
    def get_request_method(self,row):
        col = int(config.data_config.get_request_method())  # 直接使用这个类
        request_method = self.operate_excel.get_cellvalue(row, col)
        return request_method
    def get_url(self,row):
        col = int(config.data_config.get_url())  #
        url = self.operate_excel.get_cellvalue(row, col)
        return url
    #获得请求数据
    def get_request_data(self,row):
        col = int(config.data_config.get_request_data())  #
        request_data = self.operate_excel.get_cellvalue(row, col)
        return request_data

    def get_expect_result(self,row):
        col = int(config.data_config.get_expect_result())  #
        expect_result = self.operate_excel.get_cellvalue(row, col)
        if expect_result=='':
            return None
        return expect_result

    # 通过sql获取预期结果
    def get_expcet_data_for_mysql(self, row):
            op_mysql = OperationMysql()
            sql = self.get_expect_result(row)
            res = op_mysql.search_one(sql)
            return res.decode('unicode-escape')

    def write_data(self,row,value):
        col = int(config.data_config.get_actual_result())  # 直接使用这个类
        self.operate_excel.write_data(row,col,value)

    # 获取依赖的响应数据（第7列）
    def get_depend_key(self, row):
            col = int(config.data_config.get_data_depend())#case依赖的id
            depent_key = self.operate_excel.get_cellvalue(row, col)#依赖的返回数据
            if depent_key == "":
                return None
            else:
                return depent_key
    # 判断是否有case依赖

    def is_depend(self, row):
        col = int(config.data_config.get_case_depend())#case依赖id
        depend_case_id = self.operate_excel.get_cellvalue(row, col)#case依赖id
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    # 获取数据依赖字段

    def get_depend_field(self, row):
        col = int(config.data_config.get_field_depend())
        data = self.operate_excel.get_cellvalue(row, col)#数据依赖字段
        if data == "":
            return None
        else:
            return data
    #通过key拿data数据
    def get_dataFromJson(self,row):
        request_data=self.operate_json.get_data(self.get_request_data(row))
        return request_data




