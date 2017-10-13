'''Given two numbers ‘a’ and b’. Write a program to count number of bits needed to be flipped to convert ‘a’ to ‘b’.
'''
def Countsetbits(num):
    count = 0
    while num:
        num = num & num-1
        count += 1
    return count

a = int(raw_input())
b = int(raw_input())
num = a^b
print Countsetbits(num)
