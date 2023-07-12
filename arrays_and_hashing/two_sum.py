class Solution:
    def bruteForceSolution(self, nums: list[int], target: int) -> list[int]:
        result = list()
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target: 
                    result.append(i)
                    result.append(j)
                    return result;
        result.extend([0, len(nums) - 1])
        return result;
    
    
    def oneLoopSolution(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in nums and nums.index(remain) != i: 
                return [i, nums.index(remain)]
            
print(Solution().bruteForceSolution(nums= [3, 3], target= 6))
print(Solution().oneLoopSolution(nums= [3, 3], target= 6))


