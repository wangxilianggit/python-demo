print("开始操作列表===============")
# 列表
list = ['0','1','2','3','4']
print("给列表赋予初始值===============")

print("打印列表的长度list len,",len(list))
print("打印列表下标3的元素,",list[3])

print("打印列表下标2-4的元素,",list[2:4])

print("列表追加元素")
list.append('5')
list.append('6')
list.append('7')

print("打印list,",list)

print("删除index=5元素")
del list[5]
print("打印list," , list)

print("修改index=5元素")
list[2] = '8'
print("打印list," , list)

for x in list : print(x, end="\n")


print("打印当前列表中最大的元素",max(list))
print("打印当前列表中最小的元素",min(list))

list.reverse()

print("反转列表元素,",list)



print("\n\n开始操作元组===============Python 的元组与列表类似，不同之处在于元组的元素不能修改。")
print("可以理解元组就是不可变列表")

tup = (95,85,33,45)
tup1 = (925,185,433,945)

print("读取元组，第二个元素",tup[1])


print("拼接新元组,",tup+tup1)

print("删除元组tup1,",tup1)
del tup1


print("\n\n开始操作字典===============")
print("字典理解为java的MAP")