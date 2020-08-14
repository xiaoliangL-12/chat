"*None/没有: 有宣告person的变数所以不会卡掉, 只不过写了none上去后就会从0开始"
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding ='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = "Allen"
			continue                     #跳到下一个回圈
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:                            #理解为person存在才做下一行
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, "w") as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()                                   #程序的进入点, main()->def main()->上面