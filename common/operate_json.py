import json
class operate_json:
    def __init__(self,file_path=None):
        if file_path:
            self.file_path=file_path
        else:
            self.file_path='../data/user.json'#以抓取的json返回结果
        self.data=self.read_data()
#读取json文件
    def read_data(self):
        with open(self.file_path) as fp:
            data=json.load(fp)
            print(data)#dict
            return data
    #根据关键字获取数据
    def get_data(self,keyword):
        return self.data[keyword]

    def write_json(self,data):
        with open('../data/cookie.json','w') as fp:
            fp.write(json.dumps(data))

if __name__ == '__main__':
    operate_json=operate_json()
    print(operate_json.get_data('loginstate'))