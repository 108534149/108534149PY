import math
from pickle import APPENDS

while True:
    try:
        輸入=input().split('')
        座標=[]
        for x in 輸入 :
         座標.append(int(x))
        if 座標[0] <=100 and 座標[1]<=100:
            print("inside")
        else:
            print("outside")
    except(EOFError):
        break