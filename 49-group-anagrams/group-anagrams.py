class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute Force
        hashMap = {}
        for stringValue in strs:
            sortedString = ''.join(sorted(stringValue))  
            if sortedString in hashMap:
                hashMap[sortedString].append(stringValue)
            else:
                hashMap[sortedString] = [stringValue]
        

        return list(hashMap.values())