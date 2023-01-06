import math
from pickle import APPENDS

while True:
    try:
      輸入=int(input("請輸入"))
      for x in range(1,輸入+1):
        for j in range(1,x+1):
            print(j,end=(""))
        print()

    except(EOFError):
        break