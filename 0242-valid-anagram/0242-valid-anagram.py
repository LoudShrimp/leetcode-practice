class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #build hashmaps
        countS, countT = {}, {}
        #go through the keys of the hashmaps to see if the counts are the same
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        #compare the number of occurences of each key
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True
        