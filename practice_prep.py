# 
class _2048:
    def __init__(self):
        grid = [[0 for _ in range(4)] for _ in range(4)]

    # Directions are as follows:
    # 0 is up, 1 is right, 2 is down, 3 is left.
    def slide(self, direction: int):
        # slide each block starting at the row or column of the direction
        # we're sliding in.
        # if direction == 0 or direction == 2:

        for i in range(1, len(self.grid)):
            row = self.grid[i]
            for j in range(len(row)):
                if collision(this_block, row[i - 1][j]) == 0:
                    # move the block up by copying into appropriate location
                    # delete the block in this row that was moved.
                if collision(this_block, block_above) == this_block *2:
                    # merge blocks; overwrite block above it with this_block * 2
                    # delete the block in this row that was moved.
                elif collision(this_block, block_above) == -1:
                    # can't move the block; leave it as it is.
                else:
                    # throw some error

                # Clear this row of any that moved

        # At end of each slide, we have to pop in new block at open location
        if not self.pop_new_block():
            print("you lose!")


    # Check whether block1 and block2 will merge or do nothing.
    # Block2 is the block being moved into.
    def collision(self, block1: int, block2: int):
        if block2 == 0:
            return 0
        if block1 == block2:
            # Return the next highest power of 2.
            return block1 * 2

        # If it does nothing, return -1
        return -1

    def pop_new_block(self):
        temp = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 0:
                    temp.append((i, j))

        if temp == []:
            return False
        
        choice = random.choice(temp)
        grid[choice[0]][choice[1]] = random.choice(2, 4)
        return True


