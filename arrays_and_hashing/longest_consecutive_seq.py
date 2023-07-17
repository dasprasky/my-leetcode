# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longest_consecutive_sequence(self, nums: list[int]) -> int: 
        numSet = set(nums)
        longest_seq = 0
        for n in numSet:
            length = 0
            # checking if n is the start of the sequence 
            if (n-1) in numSet:
                continue
            while(n+length in numSet):
                length += 1 
            if length > longest_seq:
                longest_seq = length
        return longest_seq

print(Solution().longest_consecutive_sequence([0,3,7,2,5,8,4,6,0,1]))