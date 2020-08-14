"*清单的分割功能: n = [2, 6, 6, 8, 4]"
"1. n[:3]/(0:3): 从0个数开始到第2个数结束, 共3个数[2, 6, 6]"
"2. n[2:4]: 从2个数开始到3个数结束, 共2个数[6, 8]"
"3. n[-2:]: 从倒数2开始到最后[8, 4]"

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding ='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	person = None
	a_w_c = 0
	a_s_c = 0
	a_i_c = 0
	v_w_c = 0
	v_s_c = 0
	v_i_c = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '贴图':
				a_s_c += 1
			elif s[2] == '图片':
				a_i_c += 1
			else:
				for m in s[2:]:
					a_w_c += len(m)
		elif name == 'Viki':
			if s[2] == '贴图':
				v_s_c += 1
			elif s[2] == '图片':
				v_i_c += 1
			else:
				for m in s[2:]:
					v_w_c += len(m)

	print('allen说了', a_w_c, '个字, 同时上传了', a_s_c, '个贴图和', a_i_c, '个图片')
	print('viki说了', v_w_c, '个字, 同时上传了', v_s_c, '个贴图和', v_i_c, '个图片')


def write_file(filename, lines):
	with open(filename, "w") as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('line.txt')            #读档
	lines = convert(lines)                   #转化
	#write_file('output.txt', lines)         #写入

main()                                      #程序的进入点, main()->def main()->上面