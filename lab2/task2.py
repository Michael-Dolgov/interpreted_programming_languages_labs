n = int(input())

results = {}

for _ in range(n):
    name, votes = input().split()
    votes = int(votes)
    results[name] = results.get(name, 0) + votes

for name in sorted(results):
    print(name, results[name])
    