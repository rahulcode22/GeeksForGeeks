#Complexity O(M+N)
def isInterleaved(a,b,c):
    i, j, k = 0, 0, 0

    while k !=len(c)-1:
        if a[i] == c[k]:
            i += 1
        elif b[j] == c[k]:
            j += 1
        else:
            return 0

        k += 1
    if a[i-1] or b[j-1]:
        return 0
    return 1

a = "AB"
b = "CD"
c = "ACBG"
if isInterleaved(a,b,c) == 1:
    print c + "is Interleaved of "+ a + " and " + b
else:
    print "Not Interleaved"
