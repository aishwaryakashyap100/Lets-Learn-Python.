# Writelines method in python writes a sequence of strings to a file
# f = open('myfile4.txt','w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close

f = open('myfile4.txt','w')
lines2 = ['line 4', 'line 5', 'line 6']
for line in lines2:
    f.write(line +'\n')
f.close()