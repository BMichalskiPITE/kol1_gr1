import numbers

class MatrixError(Exception):
	def __inti__(self, error):
		super.__init__(error)

class Matrix:

	def __init__(self, *args):
	
		self.matrix_size = int(len(args) ** 0.5)
		
		if not (len(args) ** 0.5).is_integer():
			raise MatrixError("Cannot cerate square matrix")
		
		for element in args:
			if not isinstance(element, numbers.Number):
				raise MatrixError("Only numbers allowed as matrix elements")
				
		self.matrix = []
		for i in range(self.matrix_size):
			self.matrix.append([x for x in args[i * self.matrix_size : (i+1) * self.matrix_size]])
				
	def __add__(self, to_add):

		if isinstance(to_add, numbers.Number):
			return self + Matrix(*([to_add] * self.matrix_size ** 2))
		
		if isinstance(to_add, Matrix):
			if not self.matrix_size == to_add.matrix_size:
				raise MatrixError("Matrices has different sizes")
			result_matrix = []
			for i in range(self.matrix_size):
				row = []
				for j in range(self.matrix_size):
					row.append(self.matrix[i][j] + to_add.matrix[i][j])
				result_matrix.append(row)
			return Matrix(*Matrix.flatten(result_matrix))
			
		raise MatrixError("Unexpected argument")
		
	def __radd__(self, to_add):
		return self.__add__(to_add)

	def __sub__(self, to_sub):

		if isinstance(to_sub, numbers.Number):
			return self - Matrix(*([to_sub] * self.matrix_size ** 2))
		
		if isinstance(to_sub, Matrix):
			if not self.matrix_size == to_sub.matrix_size:
				raise MatrixError("Matrices has different sizes")
			result_matrix = []
			for i in range(self.matrix_size):
				row = []
				for j in range(self.matrix_size):
					row.append(self.matrix[i][j] - to_sub.matrix[i][j])
				result_matrix.append(row)
			return Matrix(*Matrix.flatten(result_matrix))
			
		raise MatrixError("Unexpected argument")
		
	def __rsub__(self, to_sub):
		if isinstance(to_sub, numbers.Number):
			return Matrix(*([to_sub] * self.matrix_size ** 2)) - self
		
		if isinstance(to_sub, Matrix):
			to_sub - self
			
		raise MatrixError("Unexpected argument")
		
	def __mul__(self, to_mul):
		if isinstance(to_mul, numbers.Number):
			return self * Matrix(*([to_mul] * self.matrix_size ** 2))
		
		if isinstance(to_mul, Matrix):
			if not self.matrix_size == to_mul.matrix_size:
				raise MatrixError("Matrices has different sizes")
			result_matrix = [[0 for _ in range(self.matrix_size)] for _ in range(self.matrix_size)]
			for i in range(self.matrix_size):
				for j in range(self.matrix_size):
					for k in range(self.matrix_size):
						result_matrix[i][j] += self.matrix[i][k]*to_mul.matrix[k][j]
			return Matrix(*Matrix.flatten(result_matrix))
			
		raise MatrixError("Unexpected argument")
	
	def __rmul__(self,to_mul):
		return self.__mul__(to_mul)
	
	def __repr__(self):
	
		def format(elements):
			return ["{}".format(element) for element in elements]
		
		def format_with_brackets(elements, delimiter):
			return "[{}]".format(delimiter.join(elements))
			
		rows = [format_with_brackets(format(row), ", ") for row in self.matrix]
		return format_with_brackets(rows,",\n")
		
	@staticmethod
	def flatten(matrix):
		return [element for row in matrix for element in row]

if __name__ == "__main__":
	matrix_1 = Matrix(4,5,6,7)
	matrix_2 = Matrix(2,8,1,5)

	sumOfMatrices = matrix_1 + matrix_2
	productOfMatrices = matrix_1 * matrix_2

	print( "Matrix 1: \n{}\n".format(matrix_1) )
	print( "Matrix 2: \n{}\n".format(matrix_2) )


	print( "Sum: \n{}\n".format(sumOfMatrices) )
	print( "Product: \n{}\n".format(productOfMatrices) )
	print( "1 + Matrix_1: \n{}\n".format( 1 + matrix_1) )
	print( "1 * Matrix_1: \n{}\n".format( 1 * matrix_1) )
	
	print( "Sub: \n{}\n".format(matrix_1 - matrix_2) )
	print( "1 - Matrix_1: \n{}\n".format( 1 - matrix_1) )
	
