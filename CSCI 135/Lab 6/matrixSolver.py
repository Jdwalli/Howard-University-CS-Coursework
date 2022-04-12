from linkedList import LinkedList
from typing import Union

class MatrixSolver():
    allMatricies = {}
    
    def __init__(self):
      pass

    def _calculate_column_size(self, nodes):
      count = 0
      temp = nodes
      while temp:
        count += 1
        temp = temp.next
      return count

    def _has_valid_matrix_dimensions(self, matrix_one_length, matrix_one_column, matrix_two_length, matrix_two_column):
      if matrix_one_length != matrix_two_length or matrix_one_column != matrix_two_column:
        return False
      return True

    def addMatrixToAllMatricies(self, matrixName:str, matrix:list) -> None:
      """
        You will be given a matrix name and a matrix. 
        Use the update method to add the matrix name and matrix to the allMatricies instance variable. 
        Don't return anything.
      """
      self.allMatricies[matrixName] = matrix

    def addMatricies(self, firstMatrixName:str, secondMatrixName:str) -> Union[list,str]:
      """
        Add the first matrix (corresponds to first matrix name) with the second matrix.
        When you add you are expected to put the values into a new matrix and return that new matrix.
        More on creating a matrix below. The dimensions MUST be the same in both matrices to add them. 
        If they are not return "Both matricies must have the same dimensions to add them"
      """

      firstMatrix =  self.allMatricies[firstMatrixName]
      secondMatrix = self.allMatricies[secondMatrixName]

      matrix_one_length = len(firstMatrix)
      matrix_one_column = self._calculate_column_size(firstMatrix[0])
      matrix_two_length = len(secondMatrix)
      matrix_two_column = self._calculate_column_size(secondMatrix[0])

      if self._has_valid_matrix_dimensions(matrix_one_length, matrix_one_column, matrix_two_length, matrix_two_column):
        solution_matrix = list()
        for row in range(matrix_one_length):
          ll = LinkedList()
          first_node, second_node = firstMatrix[row], secondMatrix[row]
          for col in range(matrix_one_column):
            ll.add_tail(first_node.value + second_node.value)
            first_node, second_node = first_node.next, second_node.next
          solution_matrix.append(ll.head)
        return solution_matrix
      else:
        return "Both matricies must have the same dimensions to add them" 
      

    def subtractMatricies(self, firstMatrixName:str, secondMatrixName:str) -> Union[list,str]:
      """
        subtractMatricies should be done the exact same way as addMatricies except obviously subtracting instead of adding. 
        If the dimensions are not the same return "Both matricies must have the same dimensions to subtract them"
      """
      firstMatrix =  self.allMatricies[firstMatrixName]
      secondMatrix = self.allMatricies[secondMatrixName]

      matrix_one_length = len(firstMatrix)
      matrix_one_column = self._calculate_column_size(firstMatrix[0])
      matrix_two_length = len(secondMatrix)
      matrix_two_column = self._calculate_column_size(secondMatrix[0])

      if self._has_valid_matrix_dimensions(matrix_one_length, matrix_one_column, matrix_two_length, matrix_two_column):
        solution_matrix = list()
        for row in range(matrix_one_length):
          ll = LinkedList()
          first_node, second_node = firstMatrix[row], secondMatrix[row]
          for col in range(matrix_two_column):
            ll.add_tail(first_node.value - second_node.value)
            first_node, second_node = first_node.next, second_node.next
          solution_matrix.append(ll.head)
        return solution_matrix
      else:
        return "Both matricies must have the same dimensions to subtract them" 



