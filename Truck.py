from Vechile import Vechile

class Truck(Vechile):

    def __init__(self):
        self.speed=200
        self.gear=8

    def print_speed(self):
        print("Speed: " + str(self.speed))

    def print_gear(self):
        print("Gear: " + str(self.gear))    