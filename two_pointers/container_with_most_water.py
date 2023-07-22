# https://leetcode.com/problems/container-with-most-water/

class Solution(): 
    def maxArea(slef, height: list[int]) -> int: 
        l, r, maxArea = 0, len(height) - 1, 0

        while l < r:
            min_height = min(height[l], height[r])
            width = r - l

            area = min_height * width
            if area > maxArea:
                maxArea = area

            if height[l] > height[r]:
                r -= 1
            else: 
                l += 1

        return maxArea
    
print(Solution().maxArea([2,3,4,5,18,17,6]))