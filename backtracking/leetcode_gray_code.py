"""
An n-bit gray code sequence is a sequence of 2n integers where:

Every integer is in the inclusive range [0, 2n - 1],
The first integer is 0,
An integer appears no more than once in the sequence,
The binary representation of every pair of adjacent integers differs by exactly one bit, and
The binary representation of the first and last integers differs by exactly one bit.

Given an integer n, return any valid n-bit gray code sequence.
"""

"""

Example 1:

Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of [0,1,3,2] is [00,01,11,10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 00 and 10 differ by one bit
- 10 and 11 differ by one bit
- 11 and 01 differ by one bit
- 01 and 00 differ by one bit

Example 2:

Input: n = 1
Output: [0,1]

 

Constraints:

1 <= n <= 16

"""


"""
approach ---

the valid sequence where bit differes by one integer 
and represenattion 

n = 2

2*2-1 
[0,1,2,3]

differs exactlky by one bit ? 

number = 0
binary = format(number, '02b')
print(binary)  # Output: 01

number2 = 1 
binary2 = format(number2, '02b')
print(binary2)


print(abs(int(binary) - int(binary2)))

bit conversion 

and then do the backtracking 

also check the new number differ by one bit from prev 

make the code 

def __init__
self.results

def _helper_dfs(idx,sequence):

base case

if idx > 0 :

    if abs(format(self.nums[idx]) - (format(sequence[idx-1])) == 1 :

        self.results.append(self.nums[idx])

    else :

        return 


def grayCode(self,n)


"""


class Solution_wrong:

    def _helper_dfs(self,idx, sequence):
        """
        The helper function to make the recursive calls 
        """

        #base case 

        if idx == 0 :

            sequence.append(self.list[idx])
            
        if idx > 0 :

            if abs(int(format(self.list[idx -1 ]))) - int((format(sequence[idx]))) == 1 :

                sequence.append(self.list[idx])

            else:

                return

        if len(sequence) ==  pow(2,self.n) - 1 :

            return sequence

        #make the recursive calls
        for i in range(idx,len(self.list)) :

            self._helper_dfs(i+1,sequence)


        sequence.pop()
        



    def grayCode(self, n: int) -> List[int]:
        """
        The function to make the sequence to follow the gray code
        """

        self.n = n 
        self.list = [i for i in range(0,pow(2,self.n))]

        #constraint case 
        if self.n == 1 :

            return [0,1]

        #vars
        sequence = [] 
        idx = 0

        #make the helper function calls 
        self._helper_dfs(idx,sequence)

        return sequence






from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        for i in range(1 << n):  # same as 2**n
            result.append(i ^ (i >> 1))
        return result

