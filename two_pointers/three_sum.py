# https://leetcode.com/problems/3sum/

class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        res = list(list())
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue

            l, r = i+1, len(nums) - 1

            while(l < r):
                if n + nums[l] + nums[r] < 0:
                    l += 1
                elif n + nums[l] + nums[r] > 0:
                    r -=1
                else: 
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while(l < r and nums[l] == nums[l-1]):
                        l += 1            

        return res
                    
    
print(Solution().three_sum([-1,0,1,2,-1,-4]))