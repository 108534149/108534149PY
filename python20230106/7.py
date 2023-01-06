import math
from pickle import APPENDS

while True:
    try:
       i=int(input())
       if i >31:
        print("輸入不能超過31")
       else:
        結果=2 ** i
        print(結果)
    except(EOFError):
        break