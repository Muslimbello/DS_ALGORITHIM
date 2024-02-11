"""
Given an integer array arr, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""


def replicate(arr):
    list = []
    for i in arr:
        list.append(i)
        if i in list:
            return True
        else:
            return False


nums = [1, 2, 3, 4, 2]

rep = replicate(nums)
print(rep)
