# https://leetcode.com/problems/valid-palindrome/description/

class Solution: 
    def valid_palindrome_extra_space(self, phrase: str) -> bool:
        alpha_num_phrase = ""
        for s in phrase: 
            if s.isalnum():
                alpha_num_phrase += s.lower()

        return alpha_num_phrase == alpha_num_phrase[::-1]
    
    def valid_palindrome_with_no_extra_space_using_pointers(self, phrase: str) -> bool: 
        l, r = 0, len(phrase) - 1 

        while l < r: 
            while(l < r and not self.is_alpha_num(phrase[l])):
                l += 1
            while(r > l and not self.is_alpha_num(phrase[r])):
                r -= 1

            if phrase[l].lower() != phrase[r].lower():
                return False
            l += 1
            r -= 1
        
        return True
    
    def is_alpha_num(self, s: str) -> bool:
        if ord('A') <= ord(s) <= ord('Z') or  ord('a') <= ord(s) <= ord('z') or ord('0') <= ord(s) <= ord('9'): 
            return True
        return False

print(Solution().valid_palindrome_extra_space("A man, a plan, a canal: Panama"))
print(Solution().valid_palindrome_with_no_extra_space_using_pointers("race a car"))