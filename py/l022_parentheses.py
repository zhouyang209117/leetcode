# coding: utf-8


class Solution:
    def generateParenthesis(self, n: int) -> 'List[str]':
        def generate(A=list()):
            if len(A) == 2 * n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append("(")
                generate(A)
                A.pop()
                A.append(")")
                generate(A)
                A.pop()


        def valid(result):
            bias = 0
            for r in result:
                if r == "(":
                    bias += 1
                else:
                    bias -= 1
                if bias < 0:
                    return False
            return bias == 0
        ans = list()
        generate()
        return ans


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))