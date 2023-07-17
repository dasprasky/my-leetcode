# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict


class Solution:
    # while iterating on each word, get the count of the character appearances saved in an array 
    # use the tuple as a key to the dictionary, and save the word 
    # runtime: O(NK), since there is a limited number of alphabets
    # space: O(NK) for hashmap
    def group_anagram_character_hashmap(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)

        return res.values()
    
    # while iterating on each word, create a tuple of the sorted word 
    # use the tuple as a key to the dictionary, and save the word 
    # runtime: O(NKlogK), where N is the number of words, and K is the length of a word.
    # space: O(NK) for hashmap
    def group_anagrams_sorting(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            key = sorted(s)
            res[tuple(key)].append(s)

        return res.values()


    
print(Solution().group_anagram_character_hashmap(["eat","tea","tan","ate","nat","bat"]))
print(Solution().group_anagrams_sorting(["eat","tea","tan","ate","nat","bat"]))

