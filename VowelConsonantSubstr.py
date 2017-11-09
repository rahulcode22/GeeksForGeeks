'''
identify the substring which starts with a vowel and end with a consonant.ob
'''
def substring(string):
    n = len(string)
    j = n-1
    i = 0
    while i < j:
        if string[i] in 'aeiou' and string[j] not in 'aeiou':
            print string[i:j+1]
            i += 1
        elif string[i] not in 'aeiou' and string[j] in 'aeiou':
            i += 1
            j -= 1
        elif string[i] not in 'aeiou':
            i += 1
        else:
            j -= 1

substring('ab')
