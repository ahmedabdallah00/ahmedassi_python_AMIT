from Vechile import Vechile

class Car(Vechile):
    name=""
    speed=0

    #construct
    def __init__(self):
        self.name='bmw'
        self.speed=50
        self.gear=6
    '''
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
    '''
    '''
    def __init__(self):
        print("entre name: ")
        self.name=input()
        print("entre speed: ")
        self.speed=int(input())
'''
    def set_speed(self,speed):
        
        self.speed=speed

    def set_name(self,name):
        
        self.name=name

    def get_speed(self):
        print("ma speed: "+str(self.speed))
        return self.speed  

    def get_name(self):
        print("name: "+self.name)
        return self.name   

    def print_data(self):
        print("data: "+self.name+" speed: "+str(self.speed))
    
    def print_speed(self):
        print("max speed: 250 ")
    
    def print_gear(self):
        print("gear: 6")
