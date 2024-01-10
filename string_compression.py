from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) > 1:
            numrep = 1
            # index of current character we're at
            curr = chars[0]
            # index of where we're placing characters
            ind = 0
            for i in range(1, len(chars)):
                if chars[i] == curr:
                    numrep += 1
                elif numrep > 1:
                    chars[ind] = curr
                    # loop over each index one at a time
                    numrep = str(numrep)
                    ind += 1
                    for j in range(len(numrep)):
                        chars[ind] = numrep[j]
                        ind += 1
                    # chars[ind + 1] = str(numrep)
                    numrep = 1
                    curr = chars[i]
                    # ind += 2
                else:
                    chars[ind] = curr
                    curr = chars[i]
                    ind += 1
            # then check once more at the very end
            if numrep > 1:
                chars[ind] = curr
                ind += 1
                numrep = str(numrep)
                for j in range(len(numrep)):
                        chars[ind] = numrep[j]
                        ind += 1
                # chars[ind + 1] = str(numrep)
                # ind += 2
            else:
                chars[ind] = curr
                ind += 1
        else:
            ind = len(chars) + 1


        return ind 
        

if __name__ == "__main__":
    s = Solution()
    arr = ["a","a","b","b","c","c","c"]
    arr = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(arr[:s.compress(arr)])

        