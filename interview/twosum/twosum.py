from typing import List

"""
Problem: Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up
to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def two_sum_v1(self, nums: List[int], target: int) -> List[int]:
        """
        Approach 1: Brute Force

        Algorithm

        The brute force approach is simple. Loop through each element xxx and find if there is another value that
        equals to target−xtarget - xtarget−x.

        Complexity Analysis

        Time complexity: O(n^2)
        For each element, we try to find its complement by looping through the rest of the array which takes O(n) time.
        Therefore, the time complexity is O(n^2).

        Space complexity: O(1).
        The space required does not depend on the size of the input array, so only constant space is used.
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

        return []

    def two_sum_v2(self, nums: List[int], target: int) -> List[int]:
        """
        Approach 2: Two-pass Hash Table


        """
        num_dict = {}
        for i, num in enumerate(nums):
            if (target - num) in num_dict:
                return [num_dict[target - num], i]
            num_dict[num] = i

        return []

    def two_sum_v3(self, nums: List[int], target: int) -> List[int]:
        """
        Approach 3: Two-pass Hash Table
        Intuition

        To improve our runtime complexity, we need a more efficient way to check if the complement exists in the array. If the complement exists, we need to get its index. What is the best way to maintain a mapping of each element in the array to its index? A hash table.

        We can reduce the lookup time from O(n)O(n)O(n) to O(1)O(1)O(1) by trading space for speed. A hash table is well suited for this purpose because it supports fast lookup in near constant time. I say "near" because if a collision occurred, a lookup could degenerate to O(n)O(n)O(n) time. However, lookup in a hash table should be amortized O(1)O(1)O(1) time as long as the hash function was chosen carefully.

        Algorithm

        A simple implementation uses two iterations. In the first iteration, we add each element's value as a key and its index as a value to the hash table. Then, in the second iteration, we check if each element's complement (target−nums[i]target - nums[i]target−nums[i]) exists in the hash table. If it does exist, we return current element's index and its complement's index. Beware that the complement must not be nums[i]nums[i]nums[i] itself!
        """
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]


if __name__ == "__main__":
    print(Solution().two_sum_v1([3, 5, 1, 4, -8], 5))
    print(Solution().two_sum_v1([3, 4, 9, 6, 4], 8))