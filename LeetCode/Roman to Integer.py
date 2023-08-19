from typing import List

class Solution:
    def romanToInt(s: str) -> int:
        roman_list = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        number = 0
        for i in range(0,len(s)):
            char = s[i]
            if(i+1 < len(s)):
                nextchar = s[i+1]
                if roman_list[char] < roman_list[nextchar]:
                    number -= roman_list[char]
                    continue
            number += roman_list[char]
        return number
    
print(Solution.romanToInt("MCMXCIV"))