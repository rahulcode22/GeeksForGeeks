'''
 Given n and an array of strings, print the string that contains the digits (1, 2, 3), if there are multiple strings that satisfies the conditions, print them in ascending order.

Input  : 5
         1395
         1721298
         102030
         3215
         123

Output : 123
         3215
         102030
'''
n = int(raw_input())
arr = map(str,raw_input().split())
no = ['1','2','3']
ans = []
for i in arr:
    var = True
    for j in no:
        if j not in i:
            var = False
            break
    if var:
        ans.append(i)
for i in sorted(ans):
    print i
