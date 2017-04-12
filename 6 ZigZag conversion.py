# Author: Steven Wang    Date: 20170410
# 6 ZigZag conversion
# did not do abstraction well, slow algorithm

        # if numRows == 1 or numRows >= len(s):
        #     return s

        # L = [''] * numRows
        # index, step = 0, 1

        # for x in s:
        #     L[index] += x
        #     if index == 0:
        #         step = 1
        #     elif index == numRows -1:
        #         step = -1
        #     index += step

        # return ''.join(L)

a = "abcdefghijklmnopqrstuvwxyz"

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s
    result = []
    numBlocks = len(s) // (2*numRows - 2) + 1
    numColumns = (numRows - 1)*numBlocks
    matrix = [[0 for x in range(numColumns)] for y in range(numRows)]

    s = list(s)
    i = 0
    while s:
        quotient = i // numRows
        quotient_2 = quotient % (numRows - 1)
        remainder = i % numRows

        if quotient_2 == 0:
            matrix[remainder][quotient] = s[0]
            del s[0]
        elif remainder + quotient_2 == numRows - 1:
            matrix[remainder][quotient] = s[0]
            del s[0]

        i += 1

    for  i in range(len(matrix)):
        for _ in range(len(matrix[i])):
            if matrix[i][_] != 0:
                result.append(matrix[i][_])

    result = ''.join(result)
    return result


convert(a, 5)
