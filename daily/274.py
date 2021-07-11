from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse = True)
        print(citations)
        a = 0
        for i in range(len(citations)):
            if citations[i]>=i+1:
                a = i+1
            else:
                break
        return a

print(Solution().hIndex([3,0,6,1,5]))