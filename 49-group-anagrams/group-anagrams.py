class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute Force
        hashMap = {}
        for s in strs:
            sort = ''.join(sorted(s))  
            if sort in hashMap:
                hashMap[sort].append(s)
            else:
                hashMap[sort] = [s]
        

        return list(hashMap.values())