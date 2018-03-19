#coding:utf-8
import json
class common_util:
    def is_contain(self,str1,str2):
        flag=None

        if str1 in str2:
            flag=True
        else:
            flag=False
        return flag
    def is_equal_dict(self,dict1,dict2):#判断2个字典是否相同

            if len(dict1)==len(dict2):
                if dict1.keys()==dict2.keys():
                    if list(dict1.values())==list(dict2.values()):
                        return True
            else:
                return False



a=common_util()
print(a.is_equal_dict({'a':1,'b':2},{'a':1,'b':2}))

