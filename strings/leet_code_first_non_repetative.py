"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

"""


#test case 

s = "leetcode"
out = 0 

s2 = "loveleetcode"
out2 = 2 

s3 = "aabb"
out3 = -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}

        print("in")

        # Count occurrences of each character
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        print(char_count)

        # Find the first non-repeating character
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i

        return -1

    def firstUniqChar2(self,s):

        mapper = {}
        count = 1

        for char in s:

            if char not in mapper:
                mapper[char] = count

            else:
                mapper[char] = mapper[char] + 1

        for i, char in enumerate(s):
            if mapper[char] == 1:
                return i

        return -1



if __name__ == "__main__":
    sol = Solution()


    sol.firstUniqChar(s)
    sol.firstUniqChar2(s)

    #print(res)
    #print(res2)
        
        