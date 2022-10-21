print("开始操作列表===============")
# 列表
list = ['0','1','2','3','4']
print("给列表赋予初始值===============")

print("打印列表的长度list len,",len(list))
print("打印列表下表0的元素list[0],",list[3])

list.append('5')
list.append('6')
list.append('7')

print("打印list,",list)
print("删除index=5元素")
del list[5]
print("打印list,",list)

print("打印当前列表中最大的元素",max(list))
print("打印当前列表中最小的元素",min(list))

print('开始进行for循环==============')
strings = '';
for item in list :
    if int(item) > 3 :
        print("item大于3,item is",item);
    else:
        print("item不大于3, is",item)
        strings = strings+item

print("打印拼接的字符串strings=",strings)
