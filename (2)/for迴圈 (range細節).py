'''
range(1,10,2)  #完整形態為此
#1為初始值(預設為0),10為終止值,2為間隔值(預設為1)
range(10)   >>> range(0,10,1) 
range(1,10) >>> range(1,10,1)

#終止值不會有(上限為終止值"上一個")
print(list(range(10)))   #list[0~9]
print(list(range(2,9)))  #list[2~8]
print(list(range(1,10,2)))  #list[1,3,5,7,9]
#正常情況初始值不能大於終止值,但間隔值為負就可以
print(list(range(10,1,-1))) #list[10~2]
'''
# for i in range(10):
#     print(i)
# print("程式執行完畢")

for i in range (10):
    if i % 2 == 0:
        print(i,"我是偶數")