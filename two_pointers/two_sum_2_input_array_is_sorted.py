# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def find_index_of_sorted_array(self, arr: list[int], target: int) -> list[int]:
        l, r = 0, len(arr) - 1

        while r > l:
            if target < arr[l] + arr[r]: 
                r -=1 
            elif target > arr[l] + arr[r]: 
                l += 1
            else: 
                return [l+1, r+1]
            

print(Solution().find_index_of_sorted_array(arr = [5,25,75], target = 100))