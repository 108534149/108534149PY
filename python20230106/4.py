import math

while True:
    try:
        l=int(input())
        NT50= l //50
        l=l % 50
        NT10=l // 10
        l=l % 10
        NT5=l // 5
        l= l % 5
        print("NT50="+str(NT50))
        print("NT10="+str(NT10))
        print("NT5="+str(NT5))
        print("NT1="+str(l))
    except(EOFError):
        break