import math
from pickle import APPENDS

while True:
    try:
        x,y=map(int,input().split())
        if 0<=x <=100 and 0<= y<=100:
            print("inside")
        else:
            print("outside")
    except(EOFError):
        break