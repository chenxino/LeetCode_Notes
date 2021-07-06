from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula:str) -> str:
        dic = defaultdict(int)
        multiply = 1
        muls = []
        num = 0
        num_count = 0
        atom = ''
        for c in formula[::-1]:
            if c == ')':
                if num:
                    multiply *= num
                    muls.append(num)
                    num = num_count = 0
                else:
                    muls.append(1)
            elif c == '(':
                
                multiply /= muls.pop()
            elif str.isdigit(c):
                num = num + int(c)*(10**num_count)
                num_count += 1
            elif str.islower(c):
                atom += c
            else:
                atom += c
                if num:
                    dic[atom[::-1]] += int(num*multiply)
                else:
                    dic[atom[::-1]] += int(multiply)
                atom = ''
                num = num_count = 0
        print(dic)
        
        return "".join(key if dic[key] == 1 else key + str(dic[key]) for key in sorted(dic.keys()))

print(Solution().countOfAtoms("((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14"))
# print(countOfAtoms("Mg(OH)2"))
print(ord('0'))
print(ord('9'))