class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if s == '':
            return False
        def scanUnsigned(i):
            temp = i
            while i<len(s) and '0'<=s[i]<='9':
                i+=1
            print(i)
            print(temp)
            return i>temp, i    
        def scanSigned(i):
            if s[i] == '+' or s[i] == '-':
                i += 1
            return scanUnsigned(i)
        dd = 0
        result, dd = scanSigned(dd)
        if dd<len(s) and s[dd] == '.':
            if dd+1 <len(s):
                temp, dd = scanUnsigned(dd+1)
                print(temp)
                result = result or temp
            else:
                return result

        if dd<len(s) and (s[dd] == 'e' or s[dd] == "E"):
            if dd+1 <len(s):
                temp, dd = scanSigned(dd+1)
                result = result and temp
            else:
                return False

        return result and dd == len(s)