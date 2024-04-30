class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        #go through nums
        for n in nums:

            #if duplicate return true
            if n in hashset:
                return True
            #otherwise add number to hashset
            hashset.add(n)
        return False