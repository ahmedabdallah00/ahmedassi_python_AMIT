from turtle import speed


class Vechile:
    speed=0
    gear=0

    def __init__(self):
        self.speed=150
        self.gear=4
    
    
    def  set_speed(self, speed):
        self.speed=speed

    def set_gear(self, gear):
        self.gear=gear

    def print_vel(self):
        print("max speed: "+ str(self.speed) +"number of gear: "+ str(self.gear)) 

    def print_speed(self):
        print("max speed: "+ str(self.speed))

    def print_gear(self):
        print("number of gear: "+ str(self.gear))


