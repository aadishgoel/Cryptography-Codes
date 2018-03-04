# Affine Cipher :AAG
MOD = 128
while True:
    b = int(input("Enter Affine Cipher Additive Key : "))
    a = int(input("Enter Affine Cipher Multiplicative Key : "))
    data = input("Enter Data: ")
    ans = []
    print('''Enter a choice:
        1: For encryption
        2: For decryption''')
    choice = int(input())
    if choice==1:
        for i in data:
            ans.append(chr((ord(i)*a+b)%MOD))
    elif choice==2:
        for i in data:
            for j in range(MOD):
                if (a*j)%MOD==1: a_inverse=j
            ans.append(chr((a_inverse*(ord(i)+MOD-b))%MOD))
    else:
        print("Enter a valid choice")
    print(''.join(ans))

''' Output
Enter Affine Cipher Additive Key : 20
Enter Affine Cipher Multiplicative Key : 17
Enter Data: aadish
Enter a choice:
        1: For encryption
        2: For decryption
1
87|
Enter Affine Cipher Additive Key : 20
Enter Affine Cipher Multiplicative Key : 17
Enter Data: 87|
Enter a choice:
        1: For encryption
        2: For decryption
2
aadish
'''
