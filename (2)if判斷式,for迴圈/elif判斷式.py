
try:
    weI=float(input("請輸入你的體重："))
    if weI>=100:
        print("你也太胖了吧!!!")
    elif weI >=80:
        print("你已經有點胖了哦!")
    elif weI >=60:
        print("真是不胖不受的好身材呢~")
    else:
        print("你也太瘦了吧...")
    print("程式執行完畢")
except:
    print("請輸入數字哦!!!")