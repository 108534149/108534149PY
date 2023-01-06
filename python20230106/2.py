from math import gcd 
while True:
    try:
        x,y=map(int,input().split())

        print(gcd(x,y))

    except(EOFError):
        break