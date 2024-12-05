import re

def prob1(data:str):
    n = 0
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            if data[i][j] == 'X':
                for v in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                    for z in range(1, 4):
                        i_z = i + v[0] * z
                        j_z = j + v[1] * z
                        if (0<=i_z<len(data)) and (0<=j_z<len(data[i_z])) and (data[i_z][j_z] == "XMAS"[z]):
                            if z == 3:
                                n += 1
                        else:
                            break
    return str(n)


def prob2(data:str):
    n = 0
    for i in range(1, len(data)-1):
        for j in range(1, len(data[i])-1):
            if data[i][j] == 'A':
                if data[i-1][j-1] in 'MS' and data[i+1][j+1] in 'MS' and data[i-1][j-1] != data[i+1][j+1]:
                    if data[i-1][j+1] in 'MS' and data[i+1][j-1] in 'MS' and data[i-1][j+1] != data[i+1][j-1]:
                        n += 1
    return str(n)
