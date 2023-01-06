import math

while True:
    try:
       輸入=input().split('')
       數字=[]
       for x in 輸入:
        數字.append(int(x))
        小值=min(數字[0],數字[1])
        for x in range(小值,0,-1):
            if 數字[0]%x==0 and 數字[1] %x ==0:
                最大公因數=x
            print=(最大公因數)

    except(EOFError):
        break