class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            #left decision tree to append value
            subset.append(nums[i])
            dfs(i + 1)

            #right decision tree to not append value
            subset.pop()
            dfs(i + 1)

        dfs(0)
        
        return result