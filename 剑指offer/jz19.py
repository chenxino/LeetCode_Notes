class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def my_match(s, p):
            if s == p:
                return True
            b = len(p)
            if s == '' and b%2 == 0:
                bb = 1
                while bb<b:
                    if p[bb] != '*':
                        return False
                    bb += 2
                return True

                
            if s == '' or p =='':
                return False
            
            i, j = 0, 0
            if j+1 < len(p):
                if p[j+1] != '*':
                    if p[i] == '.' or p[i] == s[i]:
                        return my_match(s[1:], p[1:])
                    else:
                        return False
                else:
                    if s[i] == p[i] or p[i] == '.':
                        return my_match(s[1:], p) or my_match(s, p[2:])
                    else:
                        return my_match(s, p[2:])
            if p[i] == '.' or p[i] == s[i]:
                return my_match(s[1:], p[1:])
            else:
                return False
        return my_match(s, p)