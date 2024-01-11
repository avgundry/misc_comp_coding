class Solution:
    def fractionAddition(self, expression: str) -> str:
        if not expression:
            return "0/1"

        i = 0
        curr = [0, 1]

        while i < len(expression):
            if i == 0 and expression[0] != '-':
                i -= 1
                op = '+'
            else:
                op = expression[i]
            # if numerator of curr is 0 just replace it with
            # expression instead.
            if curr[0] == 0:
                curr = [int(expression[i + 1]), int(expression[i + 3])]
                if op == '-':
                    curr[0] *= -1
            elif expression[i + 1] == '0':
                # do nothing in this case.
                pass
            else:
                for j in range(i, i + 4):
                    if expression[j] == '/':
                        num1 = int(expression[i:j])
                for k in range(i + j, i + j + 2):
                    if expression[k] == '+' or expression[k] == '-':
                        num2 = int(expression[j:k])
                        break
                self.oper(curr, op, num1, num2)
                # print(curr)
            
            i += 4

        return f"{int(curr[0])}/{int(curr[1])}"

    def simplify(self, curr):
        for prime in [2, 3, 5, 7]:
            while curr[0] % prime == 0 and curr[1] % prime == 0:
                curr[0] //= prime
                curr[1] //= prime

    def oper(self, curr, op, num2, denom2):
        num1 = curr[0]
        # num2 = int(other[0])
        denom1 = curr[1]
        # denom2 = int(other[2])

        if num1 == 0:
            curr[0] = num2
            curr[1] = denom2
            if op == '-':
                curr[0] *= -1
            return
        elif num2 == 0:
            return
        elif denom1 != denom2:
            curr[1] = denom1 * denom2
            if op == '-':
                num2 *= -1
            curr[0] = num1*denom2 + num2*denom1
        else:
            curr[0] = num1 + num2
            if op == '-':
                curr[0] *= -1

        self.simplify(curr)

if __name__ == "__main__":
    s = Solution()
    # print(s.fractionAddition("-1/2+1/2"))
    # print(s.fractionAddition("-1/2+1/2+1/3"))
    print(s.fractionAddition("1/3-1/2"))
    print(s.fractionAddition("-5/2+10/3+7/9"))
        


        