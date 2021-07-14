# Write a Python program to eliminate all empty lists from a given list of lists.
# The input will have a list of lists and the output should have the resulting list after eliminating empty lists from it.

# Sample Input:
# [[1,2,3],[],[4,5],[],[],[6,7,8]]

# Sample Output:
# [[1, 2, 3], [4, 5], [6, 7, 8]]

# A similar question was asked in a Data Scientist interview coding round.


import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
list=[l for l in input_list if l] 
print(list)
