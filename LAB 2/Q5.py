import random
class Enviroment:
    def __init__(self,corridors,nurse_stations,patient_rooms,medicine_storage_areas,patients):
        self.corridors=corridors
        self.nurse_stations=nurse_stations
        self.patient_rooms=patient_rooms
        self.medicine_storage_areas=medicine_storage_areas
        self.patients=patients


class goalBasedAgent:
    def __init__(self,enviroment):
        self.enviroment=enviroment
    
    def move_to(self,location):
        if location in self.enviroment.patient_rooms or location in self.enviroment.corridors or location in self.enviroment.nurse_stations or location in self.enviroment.medicine_storage_areas:
            print("Moving to : ",location)
            return True
        else:
            print("Location : {location} Not Found")
            return False
        
    def pickup_medicine(self,medicine,storage):
        if storage in self.enviroment.medicine_storage_areas:
            if self.move_to(storage):

                print("Picking up ",medicine," from ",storage)
            return True
        else:
            print("Incorrect storage location")
            return False
    
    def scan_patientID(self,id):
        print("Scanning Patient Identity...")
        if id in self.enviroment.patients:
            print(f"Patient with ID : {id} verified Successfully")
            return True
        else:
            print(f"Verification of Patient with ID : {id} Failed")
            return False
    def alert_staff(self,message):
        print(f"Alert for staff : {message}")

    def deliver_medicine(self,patient_id,medicine,storage,room):
        if self.scan_patientID(patient_id):
            if self.pickup_medicine(medicine,storage):
                if room in self.enviroment.patient_rooms:
                    
                    if self.move_to(room):


                        print(f"Successfully delivered {medicine} To patient : {patient_id} in Room No : {room}")


corridors=["Corridor1","Corridor2"]
nurse_stations=["NS1","NS2"]
patient_rooms=["PR1","PR2","PR3"]
medicine_storage_areas=["MSA1","MSA2"]
patients=["P1","P2","P3"]
env=Enviroment(corridors,nurse_stations,
patient_rooms,medicine_storage_areas,patients)
Agent=goalBasedAgent(env)
Agent.deliver_medicine("P1","Panadol","MSA1","PR1")            