import json
import types #调试信息

#获取目录的json文件并转化为dict格式返回
def readdrectjson():
    drectdata=open("static/drect_collection",mode='r',encoding='utf-8')
    readrul=json.load(drectdata)
    return readrul

#获取接口的json文件并转化为dict格式返回
def readapijson():
    apidata=open("static/API_collection",mode='r',encoding='utf-8')
    apiurl=json.load(apidata)
    return apiurl


def main():
   data=open("static/exportapi.txt",mode='w')    #以写的方式打开文件
   textdrect = readdrectjson()
   textapi = readapijson()
   for inter in textdrect["item"]:
       if inter is not None:
          for twoinfer in inter["item"]:
              if twoinfer is not None:
                  laststr=twoinfer.values()
                  for value in laststr:
                      if type(value) is dict:       #判断是否是dict类型
                         url=value["url"]           #取出url的值
                         url_dict=url.split('&')
                         for x in range(len(url_dict)):
                              apinamelist=url_dict[x].split('=')[1:]      #分割后获取=右侧的值
                              apinamestr=','.join(apinamelist)            #将list类型转为str
                              for item1 in textapi['item']:
                                if item1 is not None:
                                   for item2 in item1['item']:
                                      if item2 is not None:
                                        apirequest=item2.values()
                                        for urlstr in apirequest:
                                            if type(urlstr) is dict:
                                               urlapi=urlstr['url']
                                               if apinamestr in urlapi:
                                                data.write(urlapi)      #将结果输出到文件中，每次运行会将之前的结果覆盖
                                               else:
                                                   continue



#入口主函数
if __name__=='__main__':
    main()