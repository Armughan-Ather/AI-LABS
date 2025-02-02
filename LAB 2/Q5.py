import random
class Enviroment:
    def __init__(self,rooms,patients,medicine_storage, nurse_stations,corridors, schedules):
        self.rooms = rooms
        self.patients = patients
        self.medicine_storage = medicine_storage
        self.nurse_stations = nurse_stations
        self.corridors = corridors
        self.locations = rooms+medicine_storage+nurse_stations+corridors
        self.staff = bool(random.choice([True,False]))
        self.schedules=schedules


class GoalBasedAgent:
   def move_to(self, location):
        if location in self.environment.locations:
            print(f"Moving from {self.current_location} to {location}.")
            self.current_location = location
            return True
        else:
            print("Invalid destination, Not in my environment")
            return False
   def pick_up_medicine(self, medicine):
    if self.current_location != self.environment.medicine_storage[0]:
        if(not self.move_to(self.environment.medicine_storage[0])):
            return False
    self.carrying_medicine = medicine
    print(f"Picked up medicine: {medicine}.")
    return True
   def scan_patient_id(self, patient_id):
       print(f"Scanning patient ID: {patient_id}")

       if patient_id in self.environment.patients:
          print("Patient Identified")
          return True
       else:
                    
            self.alert_staff("UnIdentified Patient, Take action accordingly")
            return False  
   
   def deliver_medicine(self, room, patient_id, medicine):

      if not self.check_med_time(patient_id):
        return False

      if self.current_location == room and self.carrying_medicine:
        print("Comming to deliver medicine")

      else:
        if not self.pick_up_medicine(medicine):
           return False
        if not self.move_to(room):
           return False

      if self.scan_patient_id(patient_id):
         print(f"Delivered {self.carrying_medicine} to patient {patient_id} in {room}.")
         self.carrying_medicine = None
      else:
         print("Patient ID mismatch. Cannot deliver medicine.")
   
   def alert_staff(self, message):
    print(f"Alerting staff: {message}")
   def check_staff(self):    
        if not self.environment.staff:
            self.alert_staff("Lack of Staff")

   def check_med_time(self, patient_id):
      current_time=random.choice(['morning', 'evening', 'night'])

      if current_time not in self.environment.schedules[patient_id]:
         self.alert_staff("It is "+current_time+". Giving medicine to patient "+patient_id)
         return True
      else:
         return False

          
   def __init__(self, environment):
        self.environment = environment
        self.current_location = environment.corridors[0]
        self.carrying_medicine = None
    

def run_agent(agent, environment):
 agent.deliver_medicine("101", "1001", "Painkiller")
schedules = {
 "1001": ["morning, night"],
 "1002": ["evening"]
}
environment = Enviroment(rooms=["101", "102"],
 patients=["1001", "1002"],
 medicine_storage=["storage_room"],
 nurse_stations=["nurse_station"], corridors=["Corridor1",
"Corridor2"],
 schedules=schedules
)
agent = GoalBasedAgent(environment)
run_agent(agent, environment)    