from typing import List


# class Solution:
#     def generate_dict(self, word: str) -> dict:
#         letters = {}
#         for s in word:
#             if s in letters:
#                 letters[s] += 1
#             else:
#                 letters[s] = 1
#         return letters
    
#     def group_anagrams(self, strs: List[str]) -> List[List[str]]:
#         """
#         Works but very inefficient
#         """
#         anagram_dicts = [] # array of dictionaries
#         anagrams = []
#         for s in strs:
#             s_dict = self.generate_dict(s)
#             if s_dict in anagram_dicts:
#                 index = anagram_dicts.index(s_dict)
#                 anagrams[index].append(s)
#             else:
#                 anagram_dicts.append(s_dict)
#                 anagrams.append([s])
#         return anagrams

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time Complexity: O(n * klogk)
        - assuming k is the average length of a string in the list
        """
        seen = {}
        sorted_strs = list(map((lambda s: "".join(sorted(s))), strs))
        anagrams = []
        length = len(strs)
        for i in range(length):
            if sorted_strs[i] in seen:
                index = seen[sorted_strs[i]]
                anagrams[index].append(strs[i])
            else:
                seen[sorted_strs[i]] = len(anagrams)
                anagrams.append([strs[i]])
        return anagrams


sol = Solution()
print(sol.group_anagrams(["cat", "bat", "tab"]))
