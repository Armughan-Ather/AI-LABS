import random

class Environment:
    def __init__(self, state='Initial', component=None):
        self.state = state
        if component is None:
            component = [random.choice(['vulnerable', 'safe']) for _ in range(10)]
        self.component = component

    def display(self):
        print(f'State: {self.state}')
        print("Components:")
        for i in range(len(self.component)):
            print(f"Component {i+1}: {self.component[i]}")

class Agent:
  def scan(self, environment):
    print("Scanning Components")
    for i in range(len(enviroment.component)):
            if environment.component[i] == 'vulnerable':
              print(f"Warning ! Component {i+1} is Vulnerable")
        
    return environment.component
        
  def __init__(self):
    pass
  def patch(self, environment):  
    print("Patching Components")
    for i in range(10):
      if environment.component[i] == 'vulnerable':
        environment.component[i] = 'safe'
        print(f"Component {i+1} has been patched")
    enviroment.state = 'Final'
    return environment.component      
            
            
    

agent = Agent()
enviroment = Environment()
enviroment.display()
agent.scan(enviroment)
agent.patch(enviroment)
enviroment.display()

