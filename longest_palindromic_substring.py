class Solution:
    def radiusPalindrome(self, s: str) -> str:
        """Attempt to remember Manacher's algorithm."""
        # First must insert '|' characters between each.
        # s = ''.join(['|'])

        """Brute force first."""
        # loop over each character. see if the characters around it
        # form a palindrome. O(nk) time, I think, where k = length of
        # radius palindrome.

        # insert dummy characters at each position so that we don't
        # have to account for both odd- and even-length palindrome
        # cases.
        s1 = s
        s = ''.join(['|' + s[i] for i in range(len(s))]) + '|'
        n = len(s)
        print(s)
        best_radius = 0
        best_ind = 0
        for i in range(n):
            radius = 0
            while i - radius >= 0 and i + radius < n and \
                s[i - radius] == s[i + radius]:
                radius += 1
            if radius - 1 > best_radius:
                best_ind = i
                best_radius = radius - 1
        s = ''.join(s[best_ind + i]  for i in (-radius, radius) if s[i] != '|')
        # print(s)
        return s



        

if __name__ == "__main__":
    s = Solution()
    print(s.radiusPalindrome("babad"))
    # print(s.radiusPalindrome("cbbd"))
    # print(s.radiusPalindrome)