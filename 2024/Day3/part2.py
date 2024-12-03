import re
with open('input2') as file:
	total = 0
	pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
	isDo = True

	def mul(text):
		pattern = r"mul\((\d+),(\d+)\)"
		match = re.search(pattern, text)
		num1 = int(match.group(1))
		num2 = int(match.group(2))
		return num1 * num2
		
	for line in file.read().strip().split('\n'):
		matches = re.findall(pattern, line)
		for m in matches:
			if m == 'do()':
				isDo = True
			elif m == "don't()":
				isDo = False
			else:
				if isDo:
					total += mul(m)
	print(total)
