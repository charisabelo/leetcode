# time: n + m
# space: n + m

import math


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_arr = []
        start1 = 0
        start2 = 0

        while start1 < len(nums1) or start2 < len(nums2):
            if start1 >= len(nums1):
                new_arr.extend(nums2[start2:])
                break
            elif start2 >= len(nums2):
                new_arr.extend(nums1[start1:])
                break

            if nums1[start1] <= nums2[start2]:
                new_arr.append(nums1[start1])
                start1 += 1
            elif nums1[start1] > nums2[start2]:
                new_arr.append(nums2[start2])
                start2 += 1

        if len(new_arr) % 2 == 1:
            num = int(math.floor(len(new_arr)) / 2)
            print(num, len(new_arr))
            return float(new_arr[num])
        else:
            num = int(math.floor(len(new_arr)) / 2)
            num1 = num - 1
            return (new_arr[num] + new_arr[num1]) / 2


# new_arr = []
# loop both arrays while both start points is not greater than the list length
# every loop should add the next highest number
# if len(new_arr) % 2 == 1,
# num = math.floor(len(new_arr)), return float(new_arr[num])
# else: num = len(new_arr) / 2, num1 = num - 1
# return (new_arr[num] + new_arr[num1]) / 2
