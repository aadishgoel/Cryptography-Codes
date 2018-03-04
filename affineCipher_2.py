# Affine Cipher (MOD 26 Version) :AAG
MOD = 26
while True:
    b = int(input("Enter Affine Cipher Additive Key : "))
    a = int(input("Enter Affine Cipher Multiplicative Key : "))
    data = input("Enter Data: ").upper()
    ans = []
    print('''Enter a choice:
        1: For encryption
        2: For decryption''')
    choice = int(input())
    if choice==1:
        for i in data:
            ans.append(chr(((ord(i)-65)*a+b)%MOD +65))
    elif choice==2:
        for i in data:
            for j in range(MOD):
                if (a*j)%MOD==1: a_inverse=j
            ans.append(chr((a_inverse*((ord(i)-65)+MOD-b))%MOD +65))
    else:
        print("Enter a valid choice")
    print(''.join(ans))

''' Output
Enter Affine Cipher Additive Key : 20
Enter Affine Cipher Multiplicative Key : 17
Enter Data: AFFINECIPHER
Enter a choice:
        1: For encryption
        2: For decryption
1
UBBAHKCAPJKX
Enter Affine Cipher Additive Key : 20
Enter Affine Cipher Multiplicative Key : 17
Enter Data: UBBAHKCAPJKX
Enter a choice:
        1: For encryption
        2: For decryption
2
AFFINECIPHER
'''
