'''print only those number which is present in fibonacci series'''
def fib(n):
    lis = [0]
    a = 0
    b = 1
    while n > 0:
        c = a+b
        a = b
        b = c
        n -= 1
        lis.append(a)
    return lis
def isFib(arr):
    lis = fib(max(arr))
    for i in arr:
        if i in lis:
            print i,

isFib([2,10,4,8])
