#Write a library that contains a class that can represent any 2𝑥2 real matrice. 
#Include two functions to calculate the sum and product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
#Examples:
#
# matrix_1 = Matrix(4,5,6,7)
# matrix_2 = Matrix(2,2,2,1)
#
# matrix_3 = matrix_2.add(matrix_1)
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#(If you want you can expand implementation to NxN matrix.)
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#The whole repository MUST be a fork from https://github.com/mwmajew/kol1_gr1.py
#
#Delete these comments before commit!
#Good luck.


class Matrix:

	def __init__(self, m11, m12, m21, m22):
		self.matrix = [[m11,m12],[m21, m22]]

	def sum(self, toAdd):

		that = self.matrix
		other = toAdd.matrix

		l = [[that[i][j] + other[i][j]  for j in range(len(that[0]))] for i in range(len(that))]
		return Matrix( * [item for sublist in l for item in sublist])

	def __repr__(self):
		return "Matrix [ {}, {}, {} ,{} ]".format(*Matrix.flatten(self.matrix))


	def product(self, other):
		A = self.matrix
		B = other.matrix
		C = [[0 for row in range(len(A))] for col in range(len(B[0]))]
		for i in range(len(A)):
			for j in range(len(B[0])):
				for k in range(len(B)):
					C[i][j] += A[i][k]*B[k][j]
		return Matrix(*Matrix.flatten(C))

	@staticmethod
	def flatten(matrix):
		return [item for sublist in matrix for item in sublist]
if __name__ == "__main__":
	matrix_1 = Matrix(4,5,6,7)
	matrix_2 = Matrix(2,8,1,5)

	sumOfMatrices = matrix_1.sum(matrix_2)
	productOfMatrices = matrix_1.product(matrix_2)

	print( "Matrix 1: {}".format(matrix_1) )
	print( "Matrix 2: {}".format(matrix_2) )


	print( "Sum: {}".format(sumOfMatrices) )
	print( "Product: {}".format(productOfMatrices) )
