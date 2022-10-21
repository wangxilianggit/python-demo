import json
from unittest import result
import httplib2

# 打开文件
fo = open(file=r'D:\test.json',mode='r',encoding='utf-8')

# 打印文件名
print(fo.name)

# 读取文件
str = fo.read()

# 打印文件内容
print(str)
# 解析JSON
data = json.loads(str)

# 打印JSON的某个特殊的
print('pathList=',(data['pathList']))
pathList = data['pathList'][0];

# 发起http,OBS照片
http = httplib2.Http()
resp,content0 = http.request(pathList)

print("resp",resp)

filename = r'D:\test1.png'
print("resp",resp['status'])
if resp['status'] == '200':
    # 下载返回HTTP内容到文件
    with open (filename,'wb') as f:
        f.write(content0);
else:
    print('error');