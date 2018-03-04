#Play Fair Cipher :AAG
key = input('Enter the input key:- ')
plain_text = input('Enter the plain text:- ')
special_symbol='x'                                              

def construct_box(key):
    '''Creates Play Fair Box'''
    key.replace('j', 'i')
    d={i:0 for i in 'abcdefghiklmnopqrstuvwxyz'}
    box=[]                                              
    for i in key:
        if not d[i]:
            d[i]+=1
            box.append(i)
    box.extend([i for i in d if not d[i]])
    box = [box[i:i+5] for i in range(0,25,5)]
    return box

def transform(data,ss='x'):
    '''Transforming data in sets of 2-2 and using special symbol '''
    data = [data[i:i+2] for i in range(0,len(data),2)]  #Splitting data in 2-2
    new = []
    for item in data:                                   #Inserting Special Symbol 
        if len(item)==1: new.append((item[0],ss))
        elif item[0]==item[1]: new.extend([(item[0],ss),(item[0],ss)])
        else: new.append((item[0],item[1]))
    return new

def encryption(data,ss):
    box = construct_box(key)
    data = transform(data,ss)
    #print(*box,sep='\n')                               #To See the structure Uncomment these
    #print(data)
    ans = []
    for x,y in data:
        a=b=c=d=-1
        for i in range(5):
            for j in range(5):
                if box[i][j]==x: a,b=i,j
                if box[i][j]==y: c,d=i,j
        if a==c: ans.append((box[a][(b+1)%5],box[c][(d+1)%5]))          #Same Row
        elif b==d: ans.append((box[(a+1)%5][b] ,box[(c+1)%5][d]))       #Same Column 
        else: ans.append((box[a][d] ,box[c][b]))                        #Different Row & Column
    ans = ''.join([element for group in ans for element in group])
    return ans

cipher_text = encryption(plain_text,special_symbol)
print(cipher_text)

''' Output
Enter the input key:- hello
Enter the plain text:- yahoo
zoealy
'''
        

    
