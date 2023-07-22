# https://leetcode.com/problems/trapping-rain-water/

class Solution():
    def max_rain_water(self, input: list[int]) -> int: 
        if not input: return 0
        
        l, r = 0, len(input) - 1
        maxL, maxR = input[l], input[r]
        storedUnits = 0

        while l < r: 
            bottleneck = min(maxL, maxR)

            if maxL <= maxR:
                availableUnits = bottleneck - input[l]
                if availableUnits > 0: 
                    storedUnits += availableUnits
                l += 1
                maxL = max(maxL, input[l])
                
            else: 
                availableUnits = bottleneck - input[r]
                if availableUnits > 0: 
                    storedUnits += availableUnits
                r -= 1
                maxR = max(maxR, input[r])

        return storedUnits
    
print(Solution().max_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().max_rain_water([4,2,0,3,2,5]))