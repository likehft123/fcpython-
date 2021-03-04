name=input("請輸入名稱：")
account="lcc"
password="123456"

# if account =="lcc" and password =="123456":
#     print("登入成功")
#     print(name,"歡迎回來")
# else:
#     print("帳密錯誤")

if account =="lcc":
    if password =="123456":
        print("登入成功",name,"歡迎回來")
    else:
        print("密碼錯誤")
else:
    print("查無此帳號")
