import re
with open('input') as file:
	total = 0
	pattern = r"mul\(\d{1,3},\d{1,3}\)"
	def mul(text):
		pattern = r"mul\((\d+),(\d+)\)"
		match = re.search(pattern, text)
		num1 = int(match.group(1))
		num2 = int(match.group(2))
		return num1 * num2
	for line in file.read().strip().split('\n'):
		matchs = re.findall(pattern, line)
		for m in matchs:
			total += mul(m)

	print(total)
