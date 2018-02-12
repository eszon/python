# Create and writing on txt files (modo 'w')

file = open('writefile.txt', 'w')
for i in range(1, 6):
    file.write('\nMy name is Igor')
file.close()

#Read create file

file = open('writefile.txt', 'r')
for line in file:
    line = line.rstrip()
    print(line)
file.close()