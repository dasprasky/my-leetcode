# https://www.lintcode.com/problem/659/
# Design an algorithm to encode a list of strings to a string. 
# The encoded string is then sent over the network and is decoded back to the original list of strings.

class Solution:
    def encode(self, strs: list[str]) -> str: 
        single_str = ""
        for s in strs:
            single_str += str(len(s)) + "#" + s
        return single_str
    
    def decode(self, single_str: str) -> list[str]: 
        strs, i = list(), 0
        while i < len(single_str):
            j = i
            while(single_str[j] != '#'):
                j += 1
            length = int(single_str[i:j])
            
            strs.append(single_str[j+1: j+1+length])
            i = j + 1 + length
        
        return strs
    
print(Solution().encode(["lint","code","love","you"]))
print(Solution().decode("4#lint4#code6#lo4#ve4#you"))