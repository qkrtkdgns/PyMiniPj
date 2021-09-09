# -*- coding: utf-8 -*-
count = 0;
nono = 99;

def ctfuntion (num):
    if num > 10:
        print("count = {0}".format(num))
    elif count < 10:
        print("nono = {0}".format(nono))
    else:
        print ("none")

ctfuntion(count)
ctfuntion(3)

for i in range(0,10):
    count += i

ctfuntion(count)