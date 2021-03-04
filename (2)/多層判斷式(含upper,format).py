price=0
#item.upper() 轉大寫  ,item.lower()轉小寫

item=input("請點餐(A,B,C)：")
if item.upper() =="A":
    price = 130
    drink=input("是否需要加購可樂(Y/N)?")
    if drink.upper() =="Y":
        price += 30
elif item.upper() =="B":
    price = 115
elif item.upper() =="C":
    price = 80
    food = input("是否要升級大薯(Y/N)?")
    if food.upper()=="Y":
        price += 15
    q=input("需要捐款嗎(Y/N)?")
    if q.upper() == "Y":
        money=input("要捐多少呢?")
        price += money
else:
    print("沒有這個選項哦~")
    
print("那這樣總共是：{0}元哦".format(price))


'''
score = float(input("請輸入分數："))

if score >= 90 :
    print("成績為 A ")
    if score >= 96 :
        print("很棒哦,請你喝一罐可樂")
else:
    print("成績為 B ")
'''