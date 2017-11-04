'''Print pattern like this

Example:
Input: 1
Output: 0

Input: 2
Output:
0 0
0 1
1 0
1 1

Input: 3
Output:
0 0 0
0 0 1
0 1 0
0 1 1
1 0 0
1 0 1
1 1 0
1 1 1
'''
def printbinary(n):
    lis = []
    for i in range(2**n):
        lis.append(bin(i)[2:])
    return lis
n = int(raw_input())
lis = printbinary(n)
for i in lis:
    print i.rjust(n, '0')
