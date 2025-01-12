class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        lefts = []
        removes = []
        for i in range(len(s)):
            if s[i] == '(':
                lefts += [i]
            elif s[i] == ')':
                if lefts:
                    lefts.pop()
                else:
                    removes.append(i)

        removes.extend(lefts)
        prev = 0
        ret = ""
        for remove in sorted(removes):
            ret += s[prev:remove]
            prev = remove + 1

        # print(removes)
        # print(lefts)
        # print(ret)

        return ret + s[prev:]
        
        

        