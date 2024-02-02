"""
the problem is to set the matrix to zero in rows and columns that has zero
"""

#test cases 
matrix = [[1,1,1],[1,0,1],[1,1,1]]
out = [[1,0,1],[0,0,0],[1,0,1]]

#test casees 
matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
out2 =  [[0,0,0,0],[0,4,5,0],[0,3,1,0]]



"""
find the algo 

two hash map 
row_map 
column_map
col , row will be stored for zeroing 

for the first pass loop 
store values in both hash_map 

next pass start zeroing the values as per hashmap 
"""

class Solution():

    def setZeroes(self,matrix):
        """
        The function to set the matrix rows and columns as zeros per rule 
        """

        #initilaize the varibales 
        row_set = set()
        col_set = set()
        rows = len(matrix)
        cols = len(matrix[0])

        #first pass to get values
        for row in range(rows):
            for col in range(cols):

                if matrix[row][col] == 0 :
                    row_set.add(row)
                    col_set.add(col)
        

        #second pass for modification
        for row in range(rows):
            for col in range(cols):
                if row in row_set or col in col_set:
                    matrix[row][col] = 0


        return matrix 

        

sol = Solution()
res = sol.setZeroes(matrix)

print(res)