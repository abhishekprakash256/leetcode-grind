"""
find the max sliding windown in the array 
"""


def find_max_sliding_window(nums, w):

    # Replace this placeholder return statement with your code
    res = []
    for i in range(len(nums)-w + 1):
        cur_max = max(nums[i:i+w])
        res.append(cur_max)

    return res