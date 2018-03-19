import requests
import json

class runmain:
    # def __init__(self,url,method,data=None):
    #     self.res=self.run_main(url,method,data)#构造方法，要加self表示当前参数

    def send_get(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header)
        # return json.dumps(res,indent=2,sort_keys=True)#格式化json数据
        else:
            res = requests.get(url=url, data=data)
        return res.json()

#print(send_request(url,data))
    def send_post(self,url,data,header=None):
        res=None
        if header!=None:
            res=requests.post(url=url,data=data,headers=header)
        #return json.dumps(res,indent=2,sort_keys=True)#格式化json数据
        else:
            res=requests.post(url=url,data=data)
        return res.json()

    def run_main(self,url,method,data=None,header=None):#空值不能放在不为空的前面
        res=None
        if method=='GET':
            res=self.send_get(url,data,header)
        else:
            res=self.send_post(url,data,header)
        return json.dumps(res,ensure_ascii=False)
#
# if __name__ == '__main__':
#     url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
#     data = {
#         'cart': '11'
#     }
#     #run=runmain(url,'GET',data)
#     run=runmain()
#     print(run.run_main(url,'GET',data))