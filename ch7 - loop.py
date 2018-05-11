# -*- coding: utf-8 -*-
'''
for {var} in {List}:
    code block
    code block
    code block
'''
for i in range(15):
    print i

for i in range(-3,9):
    print i

for i in range(10,2,-1):
    print i

print range(1,31,2)

for year in range(1980,2020):
    print "In the {}, there...".format(year)


catstype = ['manx','tabby','calico']
for cat in catstype:
    print "That's a nice {} you have there!".format(cat)


numbers = [12,56,0,5,3]
for number in numbers:
    if number == 0 :
        print "Ugh, you give me a 0!"
        continue                            #continue 用来跳过某些项
    new_number = 100.0/number
    print "100/{}={}".format(number,new_number)


cart = [1,89,154,9749,197,13,65]
for item in cart:
    print item
    if item>100:
        print "you are going to require insurance on this order."
        break
    

cart = [1,89,154,9749,197,13,65]
for item in cart:
    print item
    if item>10000:
        print "you are going to require insurance on this order."
        break
else:
       print "There are no item over 10000"


# 只有为真时重复while

age = raw_input("Please give me your age in years(eg.30):")
while not age.isdigit():
    print "I'm sorry, but {} isn't valid.".format(age)
    age = age = raw_input("Please give me your age in years(eg.30):")
print "Thanks!your age is set to {}.".format(age)

# 无限循环
while True:
    text = raw_input("Give me some text, and I'll count the e's. Enter 'q' to quit:")
    if text == 'q':
        break
    print text.count('e')
