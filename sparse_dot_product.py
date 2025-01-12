class SparseVector:
    def __init__(self, nums):
        self.nums = dict()
        self.nums = {i: v for i, v in enumerate(nums) if v}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.nums[i] = nums[i]

    def dotProduct(self, vec):
        # total = 0
        # for i in range(len(vec)):
        #     total += self.nums.get(i) * vec[i]

        return sum([self.nums.get(i, 0) * vec[i] for i in range(len(vec))])

if __name__ == "__main__":
    s = SparseVector([1,0,0,2,3])
    print(s.dotProduct([0,3,0,4,0]))