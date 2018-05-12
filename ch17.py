# -*- coding: utf-8 -*-

# read files

f = open('users.txt')

users = f.readlines()   # read all the text into a list

user1 = f.readline()    # read one line in text
user2 = f.readline()
user3 = f.readline()
user4 = f.readline()

f.close()               # After using, please close the file

# write into files
f = open('users.txt','r+')
f.write('test')
f.close()
f = open('users.txt')
lines = f.readlines()
for line in lines:
    print line

f = open('users.txt','w')

lines[0]='Jacob\n'
f.writelines(lines)

# add into files
f = open('users.txt','a')
line = 'Zumba'
f.write(line)
f.close()
f = open('users.txt')
f.readlines()

# get the infromation
import os
current_dir = os.getcwd()
os.listdir(current_dir)

os.listdir('.')

os.listdir('/tmp/')

os.walk('.')

os.makedir()
os.makedirs()


stats = os.stat('README.txt')
stats.st_size
stats.st_atime
stats.st_mtime

from datetime import datetime
datetime.fromtimestamp(stats.st_atime)
