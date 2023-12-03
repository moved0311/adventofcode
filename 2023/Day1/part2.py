spelled = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('test') as file:
    lines = file.read().strip().split('\n')
    result = 0
    print(spelled)
    for line in lines:
        print(line)

    print(result)
