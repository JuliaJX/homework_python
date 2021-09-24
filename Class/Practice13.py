# f=open('D://homework_python//Tp.txt', 'r')
# print(f.read())
# f.close()

# f=open('D://homework_python//Tp.txt', 'w')
# print(f.write('i guess'))
# f.close()

# f=open('D://homework_python//README.md', 'a')
# print(f.write("I don't know"))
# f.close()

# f=open('D://homework_python//Class//Tp.txt', 'r')
# str_list = f.readlines()
# print(str_list)
# f.close()

# f=open('D://homework_python//Class//Tp.txt', 'w')
# f.writelines(['fghj', 'fghj'])
# f.close()

# f=open('D://homework_python//Class//Pt.txt', 'r')

# lines = f.readlines()
# {'Ip': '192.168.111.1', 'port': 22}
# lines=[line[:-1] for line in lines]
# h={lines[1]:lines[2],lines[3]:int(lines[4])}
# print(h)
# f.close()

f = open('D://homework_python//Class//Tp.txt', 'r')
lines = f.readlines()
lines = [line[:-1] for line in lines]
dict_ = {'ip': lines[2][:-1], 'port': int(lines[4][:-1])}
d = {lines[1]:lines[2], lines[3]: int(lines[4])}
print(d)
f.close()