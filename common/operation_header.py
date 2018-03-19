import json
import requests
from common.operate_json import operate_json
class operateHeader:
    def __init__(self,response):
        self.response=json.loads(response)#json字符串转化成字典
        print(type(self.response))
    def get_response_url(self):#获得登陆返回的token的url
        url=self.response['data']['url'][0]
        return url

    def get_cookie(self):
        '''
        获取cookie的jar文件
        '''
        url = self.get_response_url() + "&callback=jQuery21008240514814031887_1508666806688&_=1508666806689"
        cookie = requests.get(url).cookies
        return cookie
    def write_cookies(self):
        cookie=requests.utils.dict_from_cookiejar(self.get_cookie())
        op_json=operate_json()
        op_json.write_json(cookie)
if __name__ == '__main__':
    url = "http://m.imooc.com/passport/user/login"
    data = {
        "username": "18513199586",
        "password": "111111",
        "verify": "",
        "referer": "https://m.imooc.com"
    }
    res=json.dumps(requests.post(url,data).json())#字典转化成json字符串类型
    op_header=operateHeader(res)
    print(type(res))
    op_header.write_cookies()
