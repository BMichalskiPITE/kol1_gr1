from task import Matrix

matrix_1 = Matrix(4,5,6,7)
matrix_2 = Matrix(2,8,1,5)

sumOfMatrices = matrix_1.sum(matrix_2)
productOfMatrices = matrix_1.product(matrix_2)

print( "Matrix 1: {}".format(matrix_1) )
print( "Matrix 2: {}".format(matrix_2) )


print( "Sum: {}".format(sumOfMatrices) )
print( "Product: {}".format(productOfMatrices) )
