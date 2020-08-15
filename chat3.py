lines = []
with open('3together.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print('时间是:', time, '人名是:', name)