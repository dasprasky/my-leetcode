# https://leetcode.com/problems/product-of-array-except-self/ 

class Solution:
    def product_of_array_excluding_self(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)): 
            res[i] = prefix
            prefix = prefix * nums[i]
        
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        return res
    
print(Solution().product_of_array_excluding_self(nums = [-1,1,0,-3,3]))