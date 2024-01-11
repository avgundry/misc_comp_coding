class Solution:
    def lastRemaining(self, n: int) -> int:
        # As expected, brute forcing it runs out of resources.
        # Ok - let's try to find the pattern.
        # One thing we can note is that if n is odd, we will not have
        # ANY odd numbers in the list, ever.
        # If n is even - we will not have any even numbers.
        # From there...say n = 3.
        # We'd then have [1,2,3] -> 2.
        # Say n = 4. Then [1,2,3,4] -> [2,4] -> [2].
        # Say n =...8. Then [...] -> [2, 4, 6, 8] -> [2, 6].
        # Say n = 16. Then [...] -> [2, 4, 6, ..., 14, 16] -> [2, 6, 10, 14] -> [6, 14].
        # Hmm...at first I would say it's easy to exclude powers of 2 but the last part confuses me a bit.
        # Going to write this one out.







        """Brute force approach."""
        if n <= 0:
            return 
        nums = [i for i in range(1, n + 1)]
        # The direction we're going in; 0 if going left to right.
        l2r = 0
        while len(nums) > 1:
            if l2r:
                start = 1
            elif not l2r and len(nums) % 2 == 0:
                # means we start from 0
                start = 0
            else:
                start = 1
            nums = [nums[i] for i in range(start, len(nums), 2)]
            l2r = (l2r + 1) % 2

        return nums[0]



