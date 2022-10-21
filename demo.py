list = ['0','1','2','3','4']

print("list len,",len(list))
print("list[0],",list[3])

list.append('5')
list.append('6')
list.append('7')

strings = '';
for item in list :
    if int(item) > 3 :
        print("大于3,item is",item);
    else:
        print("不大于3,item is",item)
        strings = strings+item

print("strings=",strings)
