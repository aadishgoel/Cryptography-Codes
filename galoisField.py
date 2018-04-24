# Galois Field : AAG
### https://www.doc.ic.ac.uk/~mrh/330tutor/ch04s04.html ##Refer this link for logic
from functools import reduce
ir = '1011'                     #x3+x+1 is an irreducible polynomial
n=3                             #GF(p^n):-  GF(2^3)  n is 3

def mul(a,b,ir):
    x,y = bin(a)[2:],bin(b)[2:]
    mid = [int(y+'0'*index,2) for index,item in enumerate(x[::-1]) if item!='0']
    if not len(mid): mid=[0,0]
    ans= m = bin(reduce(lambda x,y:x^y,mid))[2:]
    if len(m)>len(ir):
        ans  = int(ir+'0',2)^int(m,2)                    #Xoring With Shifted IR
        ans  = bin(int(ir,2)^int(bin(ans)[2:],2))[2:]    #Reducing One Degree more 
    elif len(m)==len(ir):
        ans  = bin(int(ir,2)^int(m,2))[2:]               #Reducing One Degree  
    return(ans)

add=[[int(bin(i)[2:])^int(bin(j)[2:]) for j in range(2**n)] for i in range(2**n)]
mult=[[mul(i,j,ir) for j in range(2**n)] for i in range(2**n)]

print('Addition Table')
for line in add:
    print(*line)
print('Multiplication Table')
for line in mult:
    print(*line)
