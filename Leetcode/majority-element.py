"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array."""

arr = [ 1,2,3,1,6,1,3,1,1]
def majority_element(nums):
    nums.sort()
    n = len(nums)
    mid_num = n // 2
    result = nums[mid_num]

    return result


mode_num = majority_element(arr)
print(mode_num)
