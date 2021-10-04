#1 Write a python program to read an entire text from given file.
obj = open("file.txt",'r')
print(obj.read())
obj.close()

#2 Write a python program to read first n lines from any given file.
obj = open("file.txt",'r')
lines = obj.readlines()
for x in range(int(input())):
    print(lines[x])
obj.close()

#3 Write a python program to append text to a file and print the text
obj = open("file.txt",'a')
line = input()
obj.write('\n')
obj.write(line)
obj.close()

#4 Write a python program to read a file line by line and line by line and store it into another file
read = open("file.txt",'r')
write = open("open.txt",'w')
for line in read:
    write.write(line)
read.close()
write.close()

#5 Write a python program to store the content of a file into array.
file = open('file.txt','r')
array = []
lines = file.readlines()
for line in lines:
    array.append(line)
print(array)
file.close()

#6 Write a python program to count number of line, number of words, number character from any given file.
file = open('file.txt','r')
lines = file.readlines()
count_char = 0
count_word = 0
count_line = len(lines)
for line in lines:
    for x in line:
        if x == '\n':
            continue
        count_char+=1
    words = line.split()
    count_word+=len(words)
file.close()
print(count_char)
print(count_word)
print(count_line)

#7 Program in python count the input word from given file.
file = open('file.txt','r')
lines = file.readlines()
count = 0
for line in lines:
    for x in line:
        if x == '\n':
            continue
        count+=1
file.close()
print(count)

#8 Program to prove that the file is close or not.
import os
file = open('file.txt','r')
try:
    bool(os.rename('file.txt','file.txt'))
    print('Closed')
except:
    print('Open')
file.close()

#9 Program to generate 26 text file named A.txt, -----Z.txt and write the character which file name contains
alphabet = 'A'
import os
for x in range(26):
    file = open('temp.txt','w')
    file.write(alphabet)
    file.close()
    os.rename('temp.txt',alphabet+'.txt')
    alphabet=chr(ord(alphabet)+1)