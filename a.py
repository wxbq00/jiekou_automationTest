# a={'a':1,'b':2}
# b={'a':1,'b':2}
# print(list(a.values()),list(b.values()))
import json
a={"status": 10001, "msg": "成功", "data": {"userInfo": {"uid": "5249191"}, "url": ["http://www.imooc.com/user/ssologin?token=a-6WQ2ZLdlLs3fwqK0M4JRMEBRpdDGTdl1jWbFm0m-cGnSiFHK95L1C3_84ESWXuTxP84OLgj1bk-2DYbI5XJ620VqF5PZPQ9ZCO5micjarNaFCbLnimMs0RdgZ-ArLzGAjwWyBXVELJZsraT9iCv8f4uxmydPbwZ5h5H5-8TeeIWyp3HnCV0mKPxuOfewWOBwUw7VbY9ehcIRyqx3LmMhulW4K5iGSGKuxLJZnN2iHEI91hQxqOWfXJZ7hP3C1q-LI1b0ym", "http://coding.imooc.com/user/ssologin?token=vgvCPO5ygAIs11Jluv9GWlvx0ajs1mhT1utILVZ3b9Qk3hplyhXzUSaNFTfDw0_nuZWZ7VrXSmUt8Cji-AgPGzBfRi-ElOCi_GwjMukxYgrYWNWfKIwEgoFUYskVWXyL49hMQ2h0eq0REzSpIzr0vtHB2AxFGFWEeFnZECfDcKT0_BSphJgIMr4YMCoFicaU-7hr-vQ6Zq9prFPtDprTzhiRpw5sahXlE3W1B7qLe48t1edlV1TSwAd9clZulyuG-Z8ISxUF9B"]}}
b={"uid": "5249191"}
print(str(b) in str(a.values()))

