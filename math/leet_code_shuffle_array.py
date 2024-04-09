"""
Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

    Solution(int[] nums) Initializes the object with the integer array nums.
    int[] reset() Resets the array to its original configuration and returns it.
    int[] shuffle() Returns a random shuffling of the array.

"""




#the solution of the random shuffle 

class Solution():

    def __init__(self,nums):
        self.array = nums
        self.original = list(nums)


    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):

        for i in range(len(self.array)):
            idx = random.randrange(i,len(self.array))

            self.array[i],self.array[idx] = self.array[idx], self.array[i]

        return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()