def count_ways(X, N, num=1, memo={}):
    key = (X, num)
    if key in memo:
        return memo[key]

    if X == 0:
        return 1
    if X < 0 or num**N > X:
        return 0

    include = count_ways(X - num**N, N, num + 1, memo)
    exclude = count_ways(X, N, num + 1, memo)

    memo[key] = include + exclude
    return memo[key]

X = int(input())
N = int(input())

print(count_ways(X, N))
