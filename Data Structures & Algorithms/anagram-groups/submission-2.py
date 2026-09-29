class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        set_map = {}

        

        for i in strs:


            sorted_words = "".join(sorted(i))


            set_map.setdefault(sorted_words, []).append(i)

        

        return list(set_map.values())