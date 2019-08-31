# coding: utf-8


def match(a, b):
    if a == "(":
        return True if b == ")" else False
    elif a == "[":
        return True if b == "]" else False
    elif a == "{":
        return True if b == "}" else False
    else:
        return False


class Solution:
    def __init__(self):
        self.left = {"{", "(", "["}
        self.right = {"}", ")", "]"}

    def isValid(self, s: str) -> bool:
        statck = list()
        for a in s:
            if a in self.left:
                statck.append(a)
            else:
                if not statck:
                    return False
                last = statck.pop()
                if not match(last, a):
                    return False
        return False if statck else True


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("([)]"))
    print(s.isValid("{[]}"))
    print(s.isValid(""))
    print(s.isValid("]"))