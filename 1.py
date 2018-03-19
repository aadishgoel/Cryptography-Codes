import math

def a(x,y):
    return -x/(x+y)*math.log(x/(x+y),2) -y/(x+y)*math.log(y/(x+y),2)

while True:
    x,y = map(int, input().split())
    print(a(x,y))
