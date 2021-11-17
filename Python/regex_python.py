import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

#raw strings tell python not to handle \
print(r'\ttab this is a raw string') #this is a raw string

exp_8 = 'Manoj got 75 marks, Ishan got 55 marks, whereas Digvijay got 98 marks'
pattern = re.compile(r'\w+\sgot\s\d+')

# with open('data.txt') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)
matches = pattern.finditer(exp_8)
for match in matches:
    str = match.group(0)
    str = str.replace('got', ':')
    print(str)

with open('file1.txt','r') as file1, open('file2.txt','w') as file2:
    contents = file1.read()
    pattern = re.compile(r'[Nn]ame\sis\s\w+\sand\scgpa\sis\s\d+\.*\d*')
    matches = pattern.finditer(contents)
    for match in matches:
        x = match.group(0)
        x = x.replace('is',':')
        x = x.replace(' and',',')
        file2.write(x)
        file2.write('\n')