# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

dic={'username':['mina','meysam','yasi'],
     'password':['1123','7654','9908']}


x=input('inter your name: ') 
y=input('enter your password: ')

    
if x in dic['username'] and y in dic['password']:
    print('hello dear '+ x)
else:
    print('your username or password is incorrect! ')

