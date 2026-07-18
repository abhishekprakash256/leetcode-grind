"""
basic template for the combinations
"""


res = []
path = []

nums = [1,2]

def dfs(i):

    if i == len(nums):
        res.append(path[:])
        return

    # take
    path.append(nums[i])
    dfs(i + 1)

    # undo
    path.pop()

    # skip
    dfs(i + 1)


dfs(0)

print(res)