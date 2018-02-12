x,y = map(int, input().split())
def gcd(a,b):
    return a if not b else gcd(b,a%b)
print(gcd(x, y))

'''
Output:-
12 16
4
'''
