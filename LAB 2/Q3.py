import random 
class BackupSystem:
    def __init__(self,backupTasks=None):
        if backupTasks is None:
            backupTasks=[]
        for i in range (1,7):
            backupTasks.append(random.choice(['Completed','Failed']))
        self.backupTasks=backupTasks
    def get_status(self,i):
        return self.backupTasks[i]
    
    def display(self):
        for i in range(len(self.backupTasks)):
            print(f"Task Id : {i}  BackupStatus : {self.backupTasks[i]}")

class BackupAgent:
    def __init__(self):
        pass
    def scan(self,backupSystem):
        for task in range(len(backupSystem.backupTasks)):
            if backupSystem.get_status(task)=='Failed':
                print(f"Warning! Backup of task {task} failed")
            else:
                print(f"Backup of Task {task} Completed")

    def Retry(self,backupSystem):
        for task in range(len(backupSystem.backupTasks)):
            if backupSystem.get_status(task)=='Failed':
                print(f"Retrying backup of task {task} ")
                backupSystem.backupTasks[task]='Completed'


System=BackupSystem()
System.display()
print()
Agent=BackupAgent()
Agent.scan(System)
print()
Agent.Retry(System)
print()
System.display()
                

        
