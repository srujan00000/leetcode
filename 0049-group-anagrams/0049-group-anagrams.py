class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap = {}
        # for string in strs:
        #     letterCount = [0 for i in range(26)]
        #     for char in string:
        #         letterCount[ord(char) - ord('a')] = letterCount[ord(char)-ord('a')] + 1
        #     key = tuple(letterCount)
        #     if key in hashmap:
        #         hashmap[key].append(string)
        #     else:
        #         hashmap[key] = [string]
        # return hashmap.values()
        hashmap = defaultdict(list)
        sortedStrs = []
        for string in strs:
            sortedStrs.append(str(sorted(string)))
        for i in range(len(strs)):
            key = sortedStrs[i]
            value = strs[i]
            hashmap[key].append(value)
        return hashmap.values()
