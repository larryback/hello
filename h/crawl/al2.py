import numpy as np

n = 5
matrix = [[9, -9, -4, 3, 6],
          [7, -3, -8, 4, 4],
          [7, -9, 1, -2, 8],
          [5, -3, -4, -9, -8],
          [8, 5, -5, 4, 6]]

#answer = sum(matrix[i][i] for i in range(len(matrix)))
#print(answer)

print(sum(np.diag(matrix)))



#    sum_first_diagonal = sum(A[i][i] for i in range(n))
#     sum_second_diagonal = sum(A[n-i-1][n-i-1] for i in range(n))
 #    print(str(sum_first_diagonal)+" "+str(sum_first_diagonal))

 #    print("====================================================================================")

#     n = 5
#     B = [[ 2, -7,  2, -2,  0], [ 1,  8,  2,  2, -2], [ 6, -2,  5, -2,  5], [-4,  9, -5, -9, -7],[ 8,  0, -9,  2, -7]]
#     sum_first_diagonal = sum(B[i][i] for i in range(n))
#     sum_second_diagonal = sum(B[n-i-1][n-i-1] for i in range(n))
#     print(str(sum_first_diagonal)+" "+str(sum_first_diagonal))