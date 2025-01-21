# Hospital Queue Management System

This project implements a hospital queue management system with a graphical user interface using Python and Tkinter.

## Files

1. `main.py`: Contains the GUI implementation using Tkinter.
2. `queue_functions.py`: Implements the core functionality of the queue management system.

## Usage

To run the application, execute the `main.py` file:

```
python main.py
```

The application will open a login window. Use the staff ID "12345" to log in.

## queue_functions.py

This file contains two main classes:

### Patient

Represents a patient in the hospital queue.

Attributes:
- `name`: Patient's name
- `id`: Unique identifier for the patient
- `symptoms`: Patient's symptoms
- `severity`: Severity level of the patient's condition (1-10)
- `timestamp`: Time when the patient was added to the queue

### HospitalQueue

Manages the priority queue of patients.

Methods:
- `__init__()`: Initializes the queue and loads existing data.
- `generate_id()`: Generates a unique ID for new patients.
- `add_patient(name, symptoms, severity)`: Adds a new patient to the queue.
- `admit_patient()`: Admits the patient with the highest priority.
- `delete_patient(id)`: Removes a patient from the queue.
- `delete_admitted_patient(id)`: Removes a patient from the admitted list.
- `search_patient(id)`: Searches for a patient by ID.
- `update_patient(id, symptoms, severity)`: Updates a patient's information.
- `get_queue()`: Returns the current queue of patients.
- `save_data()`: Saves the current queue and admitted patients to files.
- `load_data()`: Loads queue and admitted patients data from files.

## main.py

This file implements the GUI for the hospital queue management system. It provides the following functionalities:

1. Staff Login
2. Add New Patient
3. View Patient Queue
4. Admit Patient
5. Search Patient
6. Update Patient Information
7. Delete Patient Record

The GUI is designed with a modern, color-coded interface for ease of use.

## Note

This system uses file-based storage (`hospital_queue.txt` and `admitted_patients.txt`) to persist data between sessions. Ensure that the application has write permissions in its directory.

## Screenshots
- Login Frame
  
![image](https://github.com/user-attachments/assets/451376be-448b-4aaa-aff5-05f1cc136953)

- New Student Frame
  
![image](https://github.com/user-attachments/assets/1043333d-8142-4a8f-9ab6-4077efa61c9d)

- View Queue Frame
  
![image](https://github.com/user-attachments/assets/355717f5-ebdb-4b58-9a79-a1611065a76e)

- Admit Patient Frame
  
![image](https://github.com/user-attachments/assets/979cc4cb-517e-4c1a-b496-bfba86ff12e7)

- Search Patient Frame
  
![image](https://github.com/user-attachments/assets/a75aac02-3341-411b-87fd-5cb8120969aa)
![image](https://github.com/user-attachments/assets/e9ef5109-8353-4da2-8ba4-5ab41d9378b8)

- Update Patient Frame
  
![image](https://github.com/user-attachments/assets/f8cd9e72-28be-4461-91f0-f4ec257db55c)

- Delete Patient Frame
  
![image](https://github.com/user-attachments/assets/063370ff-302e-4352-a7bb-6de7fa0e64c7)


