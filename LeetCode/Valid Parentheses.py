class Solution:
    def isValid(s: str) -> bool:
        credit = []
        for i in s:
            if i in '({[':
                credit.append(i)
            else:
                if len(credit) != 0:
                    if i == ')' and credit[-1] == '(':
                        credit.pop(-1)
                    elif i == '}' and credit[-1] == '{':
                        credit.pop(-1)
                    elif i == ']' and credit[-1] == '[':
                        credit.pop(-1)
                    else:
                        return False
                else:
                        return False
        if len(credit) == 0:
            return True
        else:
            return False


Solution.isValid("(){[}{]}")

