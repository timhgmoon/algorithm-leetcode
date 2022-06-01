#14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        
        if not strs:
            return ""
        
        ans = strs[0]
        for i in range(1, len(strs)):
            if len(strs[i]) > len (ans):
                strs[i] = strs[i][:len(ans)]
            else:
                ans = ans[:len(strs[i])]
            for j in range(len(strs[i])):
                if strs[i][j] != ans[j]:
                    ans = ans[:j]
                    break
        return ans
                    
            
        
