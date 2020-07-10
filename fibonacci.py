def fib(n):
    mylist=[0,1]
    a=0
    b=1
    if n == 1:
        mylist.append(a)
        print(my_list)
    elif n<=0:
        print("invalid number")
    else:
        for i in range(2,n):
             c=a+b
             a=b
             b=c
             mylist.append(c)
    print(mylist)
fib(10)
