import xlrd
from xlutils.copy import copy
class opertate_excel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:#不为空
            self.file_name=file_name
            self.sheet_id=sheet_id
        else:
            self.file_name='../data/case1.xls'
            self.sheet_id=0
        self.data=self.get_data()
    #获取sheets的内容
    def get_data(self):
        data=xlrd.open_workbook(self.file_name)
        tables=data.sheets()[self.sheet_id]
        print(tables)
        return tables

    #获取行数
    def get_colnum(self):
        tables=self.data
        return tables.nrows
    #获取某个单元格的内容,行和列
    def get_cellvalue(self,row,col):
        return self.data.cell_value(row,col)

    #写入数据
    def write_data(self,row,col,value):
        read_data=xlrd.open_workbook(self.file_name)
        write_data=copy(read_data)#复制一份excel
        sheet_data=write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    # 根据对应的caseid 找到对应行的行号
    def get_row_num(self,case_id):
        num=0#行号，从第二行开始
        cols_data=self.get_col_value()
        for d in cols_data:#每一列
            for caseid in d:#每一列的每一行数据
                return num
            num=num+1
    #根据case_id找到对应行的内容
    def get_rowDataByCaseid(self,case_id):
        row_num=self.get_row_num(case_id)
        row_data=self.get_row_value(row_num)
        return row_data

    #根据行号找到该行的内容
    def get_row_value(self,row_id):
        tables=self.data
        row_data=tables.row_values(row_id)
        return row_data

    #获取某一列的内容
    def get_col_value(self,col_id=None):#列号
        if col_id !='None':
            col_value=self.data.col_values(col_id)
        else:
            col_value=self.data.col_values(0)
        return col_value
if __name__ == '__main__':
    operate=opertate_excel()#实例化一个类
    first=operate.get_cellvalue(1,0)



