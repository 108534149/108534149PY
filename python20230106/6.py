import math
from pickle import APPENDS

while True:
    try:
        輸入=input().split('')
        if 輸入[0]>輸入[1]:
            print("最小值:"+輸入[1])
        else:
            if 輸入[1]>輸入[0]:
                print("最小值:"+輸入[0])
            else:
                print("兩數相同")
    except(EOFError):
        break