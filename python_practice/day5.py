# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class animals():
    def __init__(self,age,color):
     self.age=age
     self.color=color
    def info_animals(self):
         print('my animal has age',self.age,'and color',self.color)



   

class dogs(animals):
    pass
    def __init__(self,race,size):
        self.race=race
        self.size=size
    def info_dogs(self):
      print('my dog has this attributes:','race:',self.race,'and size:',
            self.size,'and age:' , self.age, 'years old')


class cats(animals):
    pass
    def __init__(self,eye_color):
        self.eye_color=eye_color
    
    def info_cats(self):
     print('my cat has age',self.age,"and eye color is" ,self.eye_color)    


cati=animals(1,'brown')   
cati.info_animals()

kopi=dogs('german','middle')
kopi.age=5
kopi.color='white'

kopi.info_animals()
kopi.info_dogs()

cat1=cats('gray')
cat1.age=2
cat1.info_cats()