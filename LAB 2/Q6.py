import random
def fire_checker(var):
    if var=="fire":
        return ' 🔥 '
    else:
        return '   '
class Enviroment:
    def __init__(self):
        self.grid={
            "a":"safe",
            "b":"safe",
            "c":"fire",
            "d":"safe",
            "e":"fire",
            "f":"safe",
            "g":"safe",
            "h":"safe",
            "j":"fire"
        }
        self.positions=["a",'b','c','d','e','f','g','h','j']

    def display_grid(self):
        print(fire_checker(self.grid["a"]) + '|'+ fire_checker(self.grid["b"]) +'|'+fire_checker(self.grid["c"]))
        print(fire_checker(self.grid["d"]) + '|'+ fire_checker(self.grid["e"]) +'|'+fire_checker(self.grid["f"]))
        print(fire_checker(self.grid["g"]) + '|'+ fire_checker(self.grid["h"]) +'|'+fire_checker(self.grid["j"]))

class Agent:
    def __init__(self,enviroment):
        self.enviroment=enviroment
        self.position='a'
    def scan(self):
        for position in self.enviroment.positions:
            self.position=position
            print(f"Analyzing Position : {position}")
            if self.enviroment.grid[position]=="fire":
                print(f"Extenguishing Fire At Position : {position}")
                self.enviroment.grid[position]="safe"
            else:
                print(f"Position : {position} is safe")
            self.enviroment.display_grid()
            



env=Enviroment()
agent=Agent(env)
env.display_grid()
agent.scan()