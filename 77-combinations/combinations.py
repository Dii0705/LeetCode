class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return all possible combinations of k chosen from 1-n
        curSet, subSet = [],[]

        def helper(i, curSet, subSet):
            if len(curSet) == k:
                subSet.append(curSet.copy())
                return
            if i > n:
                return
            
            for j in range(i, n+1):
                curSet.append(j)
                helper(j+1, curSet, subSet)
                curSet.pop()

        helper(1, curSet, subSet)
        return subSet