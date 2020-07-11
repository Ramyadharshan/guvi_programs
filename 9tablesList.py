N=int(input())
if N<=0:
    print('NULL')
elif N==1:
    print(9)
else:
    my_list=[]
    for i in range(1,N+1):
        my_list.append(9*i)
    print(*my_list)
