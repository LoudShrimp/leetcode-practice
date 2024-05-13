class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        #create the hashMaps 
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        #compare the counts of each character in the hashMaps
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True