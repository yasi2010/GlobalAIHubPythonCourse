# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

employees={'employee1':{'name':'mina','age':31,'language':'persian'},
           'employee2':{'name':'meysam','age':36,'language':'itily'},
           'employee3':{'name':'mohamad','age':29,'language':'germany'}}

company_managers={'manager1':{'name':'fatemeh','age':30,'language':'british'},
                  'manager2':{'name':'ghamar','age':60,'language':'persian'}}
     

for k in employees:
    print(k , 'speak in', employees[k].get('language'))
    
for k in company_managers:
    print(k , 'speak in', company_managers[k].get('language'))  
    

class employees():
    def __init__(self,name,age,language):
        self.name=name
        self.age=age
        self.language=language
        
    
    def info_employe (self):
      print('new employee is',self.name,'and has',self.age,'years old and speak in',
            self.language)
      
      
class managers():
    def __init__(self,name,age,language):
        self.name=name
        self.age=age
        self.language=language
        
    
    def info_manager (self):
      print('your new manager is',self.name,'and has',self.age,'years old and speak in',
            self.language)
      
new_employee=employees('miki', 23, 'persian')   
new_employee.info_employe()   

new_manager=managers('esi', 65, 'itily')   
new_manager.info_manager() 