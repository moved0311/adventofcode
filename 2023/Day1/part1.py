with open('input') as file:
    lines = file.read().strip().split('\n')
    result = 0
    for line in lines:
        nums = [c for c in line if c.isdigit()]
        result += int(nums[0]+nums[-1])

    print(result)
