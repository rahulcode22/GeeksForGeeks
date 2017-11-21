'''
Given arrival and departure times of all trains that reach a railway station, find         the minimum number of platforms required for the railway station so that no           train waits.
'''
#Complexity O(nlogn)
def findplatform(arr,dep):
    n = len(arr)
    arr.sort()
    dep.sort()
    plat_needed = 1
    res = 1
    i = 1
    j = 0
    while i < n and j < n:
        if arr[i] < dep[j]:
            plat_needed += 1
            i += 1
            if plat_needed > res:
                res = plat_needed
        else:
            plat_needed -= 1
            j += 1
    return res

arr = [900,940,950,1100,1500,1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

print findplatform(arr,dep)
