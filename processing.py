textData = "0btw50.txt";

with open(textData) as f:
    lines = f.readlines()


char = ['?', ',', '!','amp;', '-','...','\\n', '\\','   ', '.']
for index in range(0,len(lines)):
    for i in range(0, 9):
        lines[index] = lines[index].replace(char[i],' ')

'''
for i in range(0,len(lines)):
    lines[i].append(':')
'''

file = open("new.txt", "w")
for i in range(0, len(lines)):
    file.write(lines[i])
file.close()