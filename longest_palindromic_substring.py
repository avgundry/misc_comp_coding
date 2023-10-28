class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Manacher's algorithm: O(n) time
        """
        # first must insert characters between each character in s to ensure
        # mirroring of palindromes. i.e. even palindromes will go from 
        # aa -> |a|a|, even # of characters.
        s_prime = '|'.join(s[i:i+1] for i in range(-1, len(s)+1))
        print(s_prime)
        # array where radius[i] = longest palindrome centered at i
        radii = len(s_prime) * [0]

        center = 0
        radius = 0

        while center < len(s_prime):
            while center - radius - 1 >= 0 and \
                center + radius + 1 < len(s_prime) and \
                s_prime[center - radius - 1] == s_prime[center + radius + 1]:
                radius += 1

            radii[center] = radius

            prev_cent = center
            prev_rad = radius
            center += 1

            radius = 0

            while center <= prev_cent + prev_rad:
                mirrored_center = prev_cent - (center - prev_cent)
                max_mirrored_rad = prev_cent + prev_rad - center

                if radii[mirrored_center] < max_mirrored_rad:
                    # palindrome contained at mirrored_center is entirely 
                    # contained in palindrome centered at prev_cent
                    # so mirrored_center and center have same size palindrome

                    radii[center] = radii[mirrored_center]
                    center += 1
                elif radii[mirrored_center] > max_mirrored_rad:
                    # palindrome at mirrored_center extends beyond
                    # the palindrome at prev_center.
                    # palindrome at center must end at the edge of the
                    # prev_cent palindrome. Otherwise, 
                    # the palindrome at old_cent would be bigger
                    radii[center] = max_mirrored_rad
                    center += 1
                else:
                    radius = max_mirrored_rad
                    break

        longest_palindrome_len = max(radii)
        center = radii.index(longest_palindrome_len)
        longest_palindrome = s_prime[center - longest_palindrome_len:center + longest_palindrome_len].replace("|", "")
        # print(f"longest_palindrome_len: {longest_palindrome_len}")
        # print(f"center: {center}")
        # print(f"longest_palindrome: {longest_palindrome}")
        return longest_palindrome





        """
        slow algorithm - O(n^2)
        """
        # # start by turning s into s', which has | inserted between each 
        # # character. O(n) time total.
        # s_prime = '|'.join(s[i:i+1] for i in range(-1, len(s)+1))
        # print(s_prime)
        # # array of radius of longest palindromic substring at center i
        # radii = [0] * len(s_prime)

        # center = 0
        # while center < len(s_prime):
        #     radius = 0
        #     while center - radius - 1 >= 0 and \
        #         center + radius + 1 < len(s_prime) and \
        #         s_prime[center-radius-1] == s_prime[center+radius+1]:
        #         radius += 1
        #     radii[center] = radius

        #     center += 1

        # center = radii.index(max(radii))
        # ret = s_prime[center-radii[center]:center+radii[center]].replace("|", "")

        # return ret




        

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))