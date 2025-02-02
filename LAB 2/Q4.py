import random

class Environment:
    def __init__(self, state='Initial', component=None):
        self.state = state
        if component is None:
            component = [random.choice(['Low Risk Vulnerable', 'Safe','High Risk Vulnerable']) for _ in range(10)]
        self.component = component

    def display(self):
        print(f'State: {self.state}')
        print("Components:")
        for i in range(len(self.component)):
            print(f"Component {i+1}: {self.component[i]}")

class Agent:
  def scan(self, environment):
    print("Scanning Components..")
    for i in range(len(enviroment.component)):
            if environment.component[i] == 'Low Risk Vulnerable':
              print(f"Warning ! Component {i+1} is Low Risk Vulnerable")
            elif environment.component[i] == 'High Risk Vulnerable':
               print(f"Warning ! Component {i+1} is High Risk Vulnerable")
        
    return environment.component
        
  def __init__(self):
    pass
  def patch(self, environment):  
    print("Patching Components..")
    for i in range(10):
      if environment.component[i] == 'Low Risk Vulnerable':
         print(f"High Risk Component {i+1} needs premium service get patched")
      if environment.component[i] == 'Low Risk Vulnerable':
        environment.component[i] = 'Safe'
        print(f"Low Risk Component {i+1} has been patched")
    
    enviroment.state = 'Final'
    return environment.component      
            
            
    
    
    
      
agent = Agent()
enviroment = Environment()
enviroment.display()
print()
agent.scan(enviroment)
print()
agent.patch(enviroment)
print()
enviroment.display()
