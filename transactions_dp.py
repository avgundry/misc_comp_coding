# was given this one as part of Geneva's quant trading internship thing.
# definitely didn't pass. :') 

# You are given an array of ints, called transaction.
# You must accept/deny the transactions in order.
# Positive transactions add to your bank account balance.
# Negative remove from your bank account balance.
# Your bank account balance may not ever go below 0.
# How do you maximize the number of transactions received?

# e.g. for [-1, -1, 3, -2, -3, -1, 0, 6]:
# you would have to skip the first two, pick 3, subtract 2 and then 1, then add 0 and 6.
# This is 5 transactions and the most you can do.
def transactions(transaction):
    return recurseTrans(0, transaction, 0)

def recurseTrans(capacity, weights, n):
    dp = dict()
    for i in range(len(weights)) + 1:
        dp[i] = []
    # dp = [[-1 for i in range(capacity+1)] for j in range(len(weights) + 1)]

    return recurseDP(capacity, weights, n, dp)

def recurseDP(capacity, weights, n, dp):
    if n == len(weights):
        return 0
    print(f"n: {n} capacity: {capacity} dp: {dp}")
    if dp[n][capacity] != -1:
        return dp[n][capacity]

    if capacity + weights[n] >= 0:
        dp[n][capacity] = max(
            1 + recurseDP(capacity + weights[n], weights, n + 1, dp),
            recurseDP(capacity, weights, n + 1, dp)
        )
    else:
        dp[n][capacity] = recurseDP(capacity, weights, n + 1, dp)
    return dp[n][capacity]
        
if __name__ == "__main__":
    print(transactions([-1, -1, 3, -2, -3, -1, 0, 6]))
    print(transactions([1, -2, -1, 0, 1]))