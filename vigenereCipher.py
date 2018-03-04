#Vigenere Cipher :AAG
MOD=128
while True:
    key = input("Enter Vigenere Cipher Key: ")
    data = input("Enter Data: ")
    ans = []
    print('''Enter a choice:-
        1: For encryption
        2: For decryption''')
    choice = int(input())
    if choice==1:
        j=0
        for i in data:
            ans.append(chr((ord(i)+ord(key[j]))%MOD))
            j+=1
            j%=len(key)
    elif choice==2:
        j=0
        for i in data:
            ans.append(chr((ord(i)+MOD-ord(key[j]))%MOD))
            j+=1
            j%=len(key)
    else:
        print("Enter a valid choice")
    print(''.join(ans))

''' Output
Enter Vigenere Cipher Key: hello
Enter Data: aadishgoel
Enter a choice:-
        1: For encryption
        2: For decryption
1
IFPUbPL[Q[
Enter Vigenere Cipher Key: hello
Enter Data: IFPUbPL[Q[
Enter a choice:-
        1: For encryption
        2: For decryption
2
aadishgoel
'''
