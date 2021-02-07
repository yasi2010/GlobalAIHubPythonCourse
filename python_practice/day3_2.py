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
         print('my animal has age: ',self.age,'and color: ',self.color)



   

class dog(animals):
    pass
    def __init__(self,race,size):
        self.race=race
        self.size=size
    def info_dog(self):
      print('my dog has this attributes: ','race: ',self.race,' and size: ',
            self.size,'and age: ' , self.age)


cati=animals(1,'brown')   
cati.info_animals()

kopi=dog('german','middle')
kopi.age=5
kopi.color='white'

kopi.info_animals()
kopi.info_dog()

