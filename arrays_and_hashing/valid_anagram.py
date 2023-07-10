# https://leetcode.com/problems/valid-anagram/

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        countS, countT = {}, {}
        
        for i in range(len(s)): 
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False 
        
        return True
    
    def isAnagramCounterSolution(self, s: str, t:str) -> bool:
        # same things in a shorter way - do not use in interviews
        return Counter(s) == Counter(t)


# Follow up question - is there a solution that uses O(1) memory? 
# if we actaully have both the strings sorted then they should become the exact same strings if they are anagrams 
# so we wouldn't need more space (assuming sorting does not take any extra space) but the time complexity would be O(nlog(n))
    
    def isAnagramSortingSolution(self, s: str, t:str) -> bool:
        # same things in a shorter way - do not use in interviews
        return sorted(s) == sorted(t)

# Time complexity: O(n)
# Space complexity: O(n)    
print(Solution().isAnagram("rat", "car"))
print(Solution().isAnagramCounterSolution("anagram", "nagaram"))

# Time complexity: O(nlog(n))
# Space complexity: O(1)   
print(Solution().isAnagramSortingSolution("anagram", "nagaram"))
