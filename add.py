import json
import os

def inputurl():
    urllist=[]
    print("每行输入一个url，以0结束")
    url=input()
    while not url=="0":
        urllist.append(url)
        url=input()
    return urllist

#os.system("git pull origin master")
#os.system("git pull second master")


print("年级（如：初一）:",end=" ")
grade=input()
print("科目（如：数学）:",end=" ")
subject=input()
try:
    file=open(grade+"/"+subject+".json","r",encoding='utf-8')
    #file=file.read(encode="utf-8")
    filejs=json.load(file)
    file.close()
except IOError:
    filejs={"SUBJECT":subject,"ASSETS":[]}
print(filejs)
print("日期（如：2020/2/24）:",end=" ")
date=input()
flag=0
for ae in filejs["ASSETS"]:
    if ae["date"]==date:
        flag=1
        print("今日该科目课件已添加，url如下")
        print(ae["url"])
        print("取消 or 追加？(Y/N) :",end=" ")
        opt=input()
        if opt=="N" :
            urllist=inputurl()
            ae["url"]+=urllist
            print(filejs)
        else :
            exit(0)
            
if flag==0:
    urllist=inputurl()
    node={"date":date,"url":urllist}
    filejs["ASSETS"].append(node)
    print(filejs)
fileout=json.dumps(filejs,sort_keys=True,indent=4,ensure_ascii=False)
file=open(grade+"/"+subject+".json","w",encoding='utf-8')
file.write(fileout)
file.close()