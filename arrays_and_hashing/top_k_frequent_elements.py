# https://leetcode.com/problems/top-k-frequent-elements/
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

import heapq


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def top_k_freq_elements(self, nums:list[int], k:int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = list()

        for i in range(len(freq) - 1, -1, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if(len(res) == k):
                    return res
    
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    def top_k_freq_elements_heapq(self, nums: list[int], k: int) -> list[int]:
        dic = {}            
        for i, num in enumerate(nums):
            dic[num] = dic.get(num,0) + 1
        
        heap=[]
        for item in dic.items():
            key, value = item
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for value, key in heap:
            res.append(key)
        return res         
                
print(Solution().top_k_freq_elements(nums = [1,1,1,2,2,3], k = 2))
print(Solution().top_k_freq_elements_heapq(nums = [1,1,1,2,2,3], k = 2))
