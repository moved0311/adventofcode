from collections import defaultdict

rules = defaultdict(list)

with open('rules') as file:
    for line in file.read().strip().split('\n'):
        [k, v] = line.split('|')
        rules[int(k)].append(int(v))

with open('input') as file:
    def check(nums):
        prefix = set()
        for n in nums:
            banned = rules[n]
            for p in prefix:
                if p in banned:
                    return False
            prefix.add(n)
        return True

    total = 0
    for line in file.read().strip().split('\n'):
        nums = list(map(int, line.split(',')))

        if check(nums):
            mid = len(nums) // 2
            total += nums[mid]

    print(total)