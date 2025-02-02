'''import random

class Server:
    def __init__(self,id):
        self.id=id
        if id%2==0:
            self.load=random.randint(1,5)
        else:
            self.load=random.randint(5,10)
    
    def get_status(self):
        if self.load<5:
            return 'Underloaded'
        elif self.load==5:
            return 'Balanced'
        elif self.load>5:
            return 'Overloaded'
        
    
class LoadBalancerAgent:
    def __init__(self):
        pass

    def displayLoadStatus(self,servers):
        for server in servers:
            print(f'Server : {server.id} Load : {server.get_status()}')

    def scan(self,servers):
        print("Agent Balancing Load...")
        idx=0
        while idx<len(servers):
            if servers[idx].get_status()=='Overloaded':
                i=0
                while i!=idx and i < len(servers):
                    print("a")
                    if servers[i].get_status()=='Underloaded':
                        print("b")
                        #while servers[i].load!=5 or servers[idx].load!=5:
                        servers[i].load+=1
                        servers[idx].load-=1
                    else:
                        i+=1
            else:
                idx+=1


    
servers=[Server(i) for i in range(1,6)]
agent=LoadBalancerAgent()
print("Initia; Status :")
agent.displayLoadStatus(servers)
agent.scan(servers)
agent.displayLoadStatus(servers)

'''

import random

class Server:
    def __init__(self, id):
        self.id = id
        if id % 2 == 0:
            self.load = random.randint(5, 10)
        else:
            self.load = random.randint(1, 5)
    
    def get_status(self):
        if self.load < 5:
            return 'Underloaded'
        elif self.load == 5:
            return 'Balanced'
        else:
            return 'Overloaded'

class LoadBalancerAgent:
    def __init__(self):
        pass

    def display_load_status(self, servers):
        for server in servers:
            print(f'Server {server.id}: Load = {server.load}, Status = {server.get_status()}')

    def scan(self, servers):
        print("Agent Balancing Load...")
        overloaded_servers = [s for s in servers if s.get_status() == 'Overloaded']
        underloaded_servers = [s for s in servers if s.get_status() == 'Underloaded']

        for i in overloaded_servers:
            for j in underloaded_servers:
                if i.load > 5 and j.load < 5:  
                    transfer = min(i.load - 5, 5 - j.load)  
                    i.load -= transfer
                    j.load += transfer
                    print(f"Transferred {transfer} load from Server {i.id} to Server {j.id}")

servers = [Server(i) for i in range(1, 6)]
agent = LoadBalancerAgent()

print("Initial Status:")
agent.display_load_status(servers)

agent.scan(servers)

print("\nFinal Status:")
agent.display_load_status(servers)
