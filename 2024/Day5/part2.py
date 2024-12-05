from collections import defaultdict

rules = defaultdict(list)

with open('rules') as file:
    for line in file.read().strip().split('\n'):
        [k, v] = line.split('|')
        rules[int(k)].append(int(v))

with open('input') as file:
    def good(nums):
        prefix = set()
        for n in nums:
            banned = rules[n]
            for p in prefix:
                if p in banned:
                    return False
            prefix.add(n)
        return True

    def fix(nums):
        prefix = []
        
        for n in nums:
            banned = rules[n]
            pos = float('inf') 
            for i in range(len(prefix)):
                if prefix[i] in banned:
                    pos = min(pos, i)
            if pos < float('inf'):
                prefix = prefix[0: pos] + [n] + prefix[pos:]
            else:
                prefix.append(n)
        return prefix

    total = 0
    for line in file.read().strip().split('\n'):
        nums = list(map(int, line.split(',')))

        if not good(nums):
            fixNums = fix(nums)
            mid = len(fixNums) // 2
            total += fixNums[mid]

    print(total)