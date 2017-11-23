'''
Given a positive integer N, count all possible distinct binary strings of length N such that there are no consecutive 1’s.
'''
def count(n):
    a = [0]*n
    b = [0]*n

    a[0] = 1
    b[0] = 1

    for i in range(1,n):
        a[i] = a[i-1] + b[i-1]
        b[i] = a[i-1]

    return a[n-1] + b[n-1]

def countSimple(n):
    a = 1
    b = 1
    for i in range(1,n):
        temp = a
        a = a+b
        b = temp
    return a+b

print count(3)
