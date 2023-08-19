from typing import List
class Solution:
    #Input: strs = ["flower","flow","flight"]
    #Output: "fl"
    def longestCommonPrefix(strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        firststr = strs[0]
        length = len(strs[0])
        prifix =""
        for j in range(0,length):
            count = 0
            for s in strs[1:]:
                if firststr[j] == s[j]:
                    count += 1
                else:
                    return prifix
            if count == len(strs)-1:
                prifix += firststr[j]
        return prifix           
                

print(Solution.longestCommonPrefix(["abb", "ab"]))