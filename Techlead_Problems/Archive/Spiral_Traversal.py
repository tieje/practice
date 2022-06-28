#!/usr/bin/env python3
'''
https://www.techseries.dev/products/coderpro/categories/1831147/posts/6191071
Print a matrix of numbers by traversing in a spiral, outer to inner.
Honestly, I have no idea how to solve this problem in a simple way.
Mutating the matrix is one solution.
'''
class Solution:
    def __init__(self, matrix, row_len):
        self.matrix = matrix
        self.row_len = row_len
    def pop_matrix_top(self):
        if self.row_len < 1:
            print('finished')
            return
        for i in self.matrix[0:self.row_len]:
            print(i)
        self.matrix = self.matrix[self.row_len:]
        self.row_len -= 1
    def pop_matrix_right(self):
        pass
'''
The above was my solution so far. I don't think I'll complete it mostly because
it's a pretty long solution.
'''

'''
Study the solution later, like half an hour per day.
'''
