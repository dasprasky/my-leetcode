# https://leetcode.com/problems/contains-duplicate/
class Solution: 
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)


print(Solution().containsDuplicate([1,2,3,1]))


# brute force method
class BruteForceSolution: 
    def containsDuplicate(self, nums: list[int]) -> bool: 
        for i in range(0, len(nums)):
            num_appearance = 0
            for j in range(0, len(nums)):
                if(nums[i] == nums[j]):
                    num_appearance+=1
            if(num_appearance > 1): return True

        return False
#Time complexity: O(n^2)
#Space complexity: O(1)
print(BruteForceSolution().containsDuplicate([1,2,3,1]))


# sorting method - if we sort the list then any duplicates will be adjacent 
# and we only need to iterate over the list once making time complexity of this solution O(nlog(n))
# Space complexity: O(1)
class SortingSolution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums = sorted(nums) #O(nlongn)
        for i in range(len(nums)-1):
            if(nums[i] == nums[i+1]):
                return True
        return False


# hashset method - we enter the values one by one if the value does not already exist 
# time complexity: O(n)
# space complexity: O(n) - needed to create the hashset
class HashSetSolution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for num in nums: 
            if num in hashset:
                return True
            hashset.add(num)
        return False
