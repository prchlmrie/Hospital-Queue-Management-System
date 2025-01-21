from datetime import datetime
import heapq

class Patient:
    def __init__(self, name, id, symptoms, severity):
        self.name = name
        self.id = id
        self.symptoms = symptoms
        self.severity = severity
        self.timestamp = datetime.now()
 
    def __lt__(self, other):
        if self.severity != other.severity:
            return self.severity > other.severity
        return self.timestamp < other.timestamp
 
class HospitalQueue:
    def __init__(self):
        self.priority_queue = []  # Priority Queue for patients
        self.patient_dict = {}    # Hash Table for quick lookups
        self.admitted_patients = []  # List to store admitted patients
        self.last_id = 0  # Track the last used ID
        self.load_data()
        
        # Find the highest ID from existing data
        all_patients = self.priority_queue + self.admitted_patients
        if all_patients:
            max_id = max(int(patient.id) for patient in all_patients)
            self.last_id = max_id

    def generate_id(self):
        self.last_id += 1
        return f"{self.last_id:02d}"  

    def add_patient(self, name, symptoms, severity):
        new_id = self.generate_id()
        patient = Patient(name, new_id, symptoms, severity)
        heapq.heappush(self.priority_queue, patient)
        self.patient_dict[new_id] = patient
        self.save_data()
        return f"Patient added successfully with ID: {new_id}"

    def admit_patient(self):
        if not self.priority_queue:
            return "No patients in queue"
        patient = heapq.heappop(self.priority_queue)
        del self.patient_dict[patient.id]
        self.admitted_patients.append(patient)
        self.save_data()
        return f"Admitted patient: {patient.name} (Severity: {patient.severity})"
 
    def delete_patient(self, id):
        if id in self.patient_dict:
            patient = self.patient_dict[id]
            self.priority_queue = [p for p in self.priority_queue if p.id != id]
            heapq.heapify(self.priority_queue)
            del self.patient_dict[id]
            self.save_data()
            return f"Deleted patient: {patient.name}"
        return "Patient not found"
 
    def delete_admitted_patient(self, id):
        for patient in self.admitted_patients:
            if patient.id == id:
                self.admitted_patients.remove(patient)
                self.save_data()
                return f"Deleted admitted patient: {patient.name}"
        return "Patient not found in admitted list"
 
    def search_patient(self, id):
        return self.patient_dict.get(id)
 
    def update_patient(self, id, symptoms, severity):
        if id not in self.patient_dict:
            return "Patient not found"
        patient = self.patient_dict[id]
        patient.symptoms = symptoms
        patient.severity = severity
        heapq.heapify(self.priority_queue)
        self.save_data()
        return f"Updated patient: {patient.name}"
 
    def get_queue(self):
        return sorted(self.priority_queue, key=lambda x: (-x.severity, x.timestamp))
 
    def save_data(self):
        # Save patients in queue
        with open('src/hospital_queue.txt', 'w') as f:
            for patient in self.priority_queue:
                f.write(f"{patient.name},{patient.id},{patient.symptoms},{patient.severity},{patient.timestamp.isoformat()}\n")
        # Save admitted patients
        with open('src/admitted_patients.txt', 'w') as f:
            for patient in self.admitted_patients:
                f.write(f"{patient.name},{patient.id},{patient.symptoms},{patient.severity},{patient.timestamp.isoformat()}\n")
 
    def load_data(self):
        # Load patients in queue
        try:
            with open('src/hospital_queue.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    name, id, symptoms, severity, timestamp = line.strip().split(',')
                    patient = Patient(name, id, symptoms, int(severity))
                    patient.timestamp = datetime.fromisoformat(timestamp)
                    heapq.heappush(self.priority_queue, patient)
                    self.patient_dict[id] = patient
        except FileNotFoundError:
            pass
        # Load admitted patients
        try:
            with open('src/admitted_patients.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    name, id, symptoms, severity, timestamp = line.strip().split(',')
                    patient = Patient(name, id, symptoms, int(severity))
                    patient.timestamp = datetime.fromisoformat(timestamp)
                    self.admitted_patients.append(patient)
        except FileNotFoundError:
            pass