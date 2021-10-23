class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        l = []
        i = 0
        j = 0
        while j<len(popped):
            if l == []:
                l.append(pushed[i])
                i += 1
            if l[-1] == popped[j]:
                l.pop()
                j += 1
            elif i < len(pushed):
                l.append(pushed[i])
                i += 1
            else:
                return False
        return True