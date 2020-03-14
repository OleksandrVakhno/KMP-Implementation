class Solution:
    def buildPat(self, needle):
        pattern = [-1 for i in needle]
        
        i =0 
        j =1
        
        while j<len(needle):
            if needle[i]==needle[j]:
                pattern[j] = i
                i+=1
                j+=1
            elif i>0:
                i = pattern[i-1] + 1
            else:
                j+=1
        
        return pattern
    
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)<1:
            return 0
        
        pattern = self.buildPat(needle)
        
        i = 0
        j = 0
        while i+len(needle)-j<=len(haystack):
            if haystack[i]==needle[j]:
                if j==len(needle)-1:
                    return i-j
                i+=1
                j+=1
            elif j>0:
                j = pattern[j-1]+1
            else:
                i+=1
                
        return -1
        