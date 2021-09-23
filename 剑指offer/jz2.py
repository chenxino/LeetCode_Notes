class Solution:
    def replaceSpace(self , s ):
        if s is None:
            return ""
        ss = ""
        for i in s:
            if i == ' ':
                ss += '%20'
            else:
                ss += i
        return ss