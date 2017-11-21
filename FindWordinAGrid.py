x = [-1,-1,-1,0,0,1,1,1]
y = [-1,0,1,-1,1,-1,0,1]
#Microsoft, ZOHO
def findWord(matrix,row,col, word):
    n = len(word)
    if matrix[row][col] != word[0]:
        return False
    for direction in range(0,8):
        rd = row + x[direction]
        cd = col + y[direction]

        for k in range(1,n):
            if rd >= len(matrix) or rd < 0 or cd >= len(matrix[0]) or cd < 0:
                break
            if grid[rd][cd] != word[k]:
                break
            rd += x[direction]
            cd += y[direction]
        if k == n:
            return True
    return False

def patternSearch(matrix,word):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if findWord(matrix,row,col,word):
                print row,col

matrix = [["GEEKSFORGEEKS"],["GEEKSQUIZGEEK"],["IDEAQAPRACTICE"]]
patternSearch(matrix,"EEE")
