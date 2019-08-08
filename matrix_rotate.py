def rotate(matrix):

    len_matrix = len(matrix)
    layer = 0

    for i in range(layer, len_matrix // 2):
        for j in range(i, len_matrix - 1 - i):
            # store the first val
            p1 = matrix[i][j]
            
            # store the second val
            p2 = matrix[j][len_matrix-1-i]

            # store the third val
            p3 = matrix[len_matrix-1-i][len_matrix-1-j]

            # storte the fourth val
            p4 = matrix[len_matrix-1-j][i]

            #exchange the val to make the rotation result
            matrix[i][j] = p4
            matrix[j][len_matrix-1-i] = p1
            matrix[len_matrix-1-i][len_matrix-1-j] = p2
            matrix[len_matrix-1-j][i] = p3

    return matrix

def main():

    s = [[7,4,1],
         [8,5,2],
         [9,6,3]]

    result = rotate(s)

    print(result)

if __name__ == '__main__':
    main()