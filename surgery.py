#Import the library pandas to create dataframes which are going to be used
#as global dataframes to be accessed by multiple classes
import pandas as pd
#Dataframe prescription_list contains all the prescriptions issued by the doctor
prescription_list = pd.DataFrame(columns = ["Medicine", "Patient", "Patient address", "Doctor", "Quantity", "Dosage"])
#Dataframe appointment_list has the appointments made by the receptionist and saved in the appointment schedule
appointment_list = pd.DataFrame(columns = ["Date: ", "Time slot: ", "Urgency: ", "Patient Name", "Patient address: ", "Patient Phone", "Visited By", "Staff Number"])



class Healthcare_Professional:
    """Super class Healthcare_Professional will pass its attributes
    and methods to the classes Doctor and Nurse"""
    def __init__(self, h_name, h_employee_number):
        self.h_name = str(h_name)
        self.h_employee_number = str(h_employee_number)
    
        
    def consultation(self):
        consultation = input("Consultation: ")
        return "Patient seen by " + self.h_name + ". Findings: " + consultation


class Doctor(Healthcare_Professional):
    def __init__(self,h_name, h_employee_number):
           self.h_name = str(h_name)
           self.h_employee_number = str(h_employee_number)
           
    #The method refers to the global dataframe  prescription_list and will store 
    #any new prescriptions issued by the doctor and will return the prescription list   
    def issue_prescription(self, medicine, p_name, p_address, h_name, quantity, dosage):
        global prescription_list
        prescription_list.loc[len(prescription_list)] = [medicine, p_name, p_address, h_name, quantity, dosage]
        return prescription_list
       
    
class Nurse(Healthcare_Professional):
    def __init__(self, h_name, h_employee_number):
        self.h_name = str(h_name)
        self.h_employee_number = str(h_employee_number)


class Prescription:
    
    def __init__(self, medicine, p_name,p_address, h_name, quantity, dosage):
        self.medicine = medicine
        self.p_name = p_name
        self.p_address = p_address
        self.h_name = h_name
        self.quantity = quantity
        self.dosage = dosage

class Patient:
    
    def __init__(self, p_name, p_address, p_phone):
        self.p_name = str(p_name)
        self.p_address = str(p_address)
        self.p_phone = str(p_phone)
    
    #This method asks the patient to enter its name when is prompt a message
    #and will search the name in the global prescription dataframe allowing the
    #patient to have a previous prescription being reissued
    def request_repeat(self):
        global prescription_list
        p_name = input("Enter your name: ")
        print(prescription_list[prescription_list["Patient"] == p_name].reset_index(drop = True))
        selection = input("Select ID of prescription to be reissued:")
        return "A prescription for " + str(prescription_list[prescription_list["Patient"] == p_name].reset_index(drop = True).iloc[int(selection), 0]) + " has been reissued at your local pharmacy"
    
    #The patient is required to call the surgery to make an appointment
    def request_appointment(self):
        print("Call surgery to make an appointment")
    
class Appointment():
    
    def __init__(self, date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number):
        self.date = date
        self.time_slot = time_slot
        self.urgency = urgency
        self.p_name = p_name
        self.p_address = p_address
        self.p_phone = p_phone
        self.h_name = h_name
        self.h_employee_number = h_employee_number
       

class Receptionist:
    def __init__(self, r_name, r_employee_number):
        self.r_name = str(r_name)
        self.r_employee_number = str(r_employee_number)
        
    #This method consents the receptionist to add appointments in the global dataframe
    #and these entries will be visualized also in the appointment scheduler to check
    #when there is availability of appointments    
    def make_appointment(self, date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number):
        global appointment_list
        appointment_list.loc[len(appointment_list)] = [date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number]
        return appointment_list

    #The method performs a search in the global appointment dataframe by the name of
    #of the patient who wants to cancel an appointment. This will consent the receptionist
    #to visualize all the appointments with the patient name given and select
    #which one to cancel
    def cancel_appointment(self):
        global appointment_list
        p_name = input("Enter patient name that wants to cancel: ")
        print(appointment_list[appointment_list["Patient Name"] == p_name])
        selection = input("Select ID of appointment to cancel:")
        appointment_list = appointment_list.drop(index = int(selection))
        return "The appointment has been cancelled"


class Appointment_schedule:

    def __init__(self, date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number):
        
        self.appointments = [Appointment(date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number)]
    
    #This method consents to add appointments in the global dataframe appointment_list.
    #Once add the appointment will be returned the dataframe.
    #when there is availability of appointments     
    def add_appointment(self, date, time_slot,urgency, p_name, p_address, p_phone, h_name, h_employee_number):
        global appointment_list
        appointment_list.loc[len(appointment_list)] = [date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number]
        return appointment_list
        
    #The method performs a search in the global appointment dataframe by the name of
    #of the patient who wants to cancel an appointment.
    #will be visualized all the appointments with the patient name given and select
    #which one to cancel
    def cancel_scheduled_appointment(self):
        global appointment_list
        p_name = input("Enter patient name that wants to cancel scheduled appointment: ")
        print(appointment_list[appointment_list["Patient Name"] == p_name])
        selection = input("Select ID of appointment to cancel:")
        appointment_list = appointment_list.drop(index = int(selection))
        return "The scheduled appointment has been cancelled"
    
    #This method gives a message with opening hours of the surgery and info regarding
    #the time slots for the appointments. Then will print the appointment list sorted by
    #date and time to help the receptionist to see the when there are slots available
    def show_schedule(self):
        print("Surgery opened daily from 0900 to 1700. Every appointment slot is 1 hour and last appointment is at 1600")
        print(appointment_list.sort_values(by=["Date: ", "Time slot: "],axis = 0, ascending = True))
        


        
        





"""=============================CODE END==================================="""

"""=============================TEST CASES================================="""
print("Begin of test cases")

"""TEST 1"""  
"""The doctor or the Nurse can enter his name and employee number, then will be able to 
print the findings of the consultation when visits a patient"""      


print("Test 1")

class Healthcare_Professional:
    """Super class Healthcare_Professional will pass its attributes
    and methods to the classes Doctor and Nurse"""
    def __init__(self, h_name, h_employee_number):
        self.h_name = str(h_name)
        self.h_employee_number = str(h_employee_number)
    
        
    def consultation(self):
        consultation = input("Consultation: ")
        return "Patient seen by " + self.h_name + ". Findings: " + consultation


class Doctor(Healthcare_Professional):
    def __init__(self,h_name, h_employee_number):
           self.h_name = str(h_name)
           self.h_employee_number = str(h_employee_number)
           
      
    def issue_prescription(self, medicine, p_name, p_address, h_name, quantity, dosage):
        global prescription_list
        prescription_list.loc[len(prescription_list)] = [medicine, p_name, p_address, h_name, quantity, dosage]
        return prescription_list


class Nurse(Healthcare_Professional):
    def __init__(self, h_name, h_employee_number):
        self.h_name = str(h_name)
        self.h_employee_number = str(h_employee_number)

D = Doctor("Valentino Rossi", "46")
print(D.consultation())
N = Nurse("Daniel Ricciardo", "3")
print(N.consultation())

"""TEST 2"""
"""The the doctor enters his name and employee number, then will be able to 
issue a prescription for the patient that is visiting. The prescription will
be saved into a dataframe containing all the prescriptions issued and will be
displayed all the prescriptions issued"""

print("Test 2")

import pandas as pd
prescription_list = pd.DataFrame(columns = ["Medicine", "Patient", "Patient address", "Doctor", "Quantity", "Dosage"])

class Healthcare_Professional:
    """Super class Healthcare_Professional will pass its attributes
    and methods to the classes Doctor and Nurse"""
    def __init__(self, h_name, h_employee_number):
        self.h_name = str(h_name)
        self.h_employee_number = str(h_employee_number)
    
        
    def consultation(self):
        consultation = input("Consultation: ")
        return "Patient seen by " + self.h_name + ". Findings: " + consultation


class Doctor(Healthcare_Professional):
    def __init__(self,h_name, h_employee_number):
           self.h_name = str(h_name)
           self.h_employee_number = str(h_employee_number)
             
    def issue_prescription(self, medicine, p_name, p_address, h_name, quantity, dosage):
        global prescription_list
        prescription_list.loc[len(prescription_list)] = [medicine, p_name, p_address, h_name, quantity, dosage]
        return prescription_list

class Nurse(Healthcare_Professional):
    def __init__(self, h_name, h_employee_number):
        self.h_name = str(h_name)
        self.h_employee_number = str(h_employee_number)

class Prescription:
    
    def __init__(self, medicine, p_name,p_address, h_name, quantity, dosage):
        self.medicine = medicine
        self.p_name = p_name
        self.p_address = p_address
        self.h_name = h_name
        self.quantity = quantity
        self.dosage = dosage

class Patient:
    
    def __init__(self, p_name, p_address, p_phone):
        self.p_name = str(p_name)
        self.p_address = str(p_address)
        self.p_phone = str(p_phone)
    

    def request_repeat(self):
        global prescription_list
        p_name = input("Enter your name: ")
        print(prescription_list[prescription_list["Patient"] == p_name].reset_index(drop = True))
        selection = input("Select ID of prescription to be reissued:")
        return "A prescription for " + str(prescription_list[prescription_list["Patient"] == p_name].reset_index(drop = True).iloc[int(selection), 0]) + " has been reissued at your local pharmacy"
    
   
    def request_appointment(self):
        print("Call surgery to make an appointment")

D = Doctor("Valentino Rossi", "46")
D.issue_prescription("Aspirin", "Lewis", "44 Mercedes Road", "Valentino Rossi", 20, 3)

"""TEST 3"""
"""The patient will enter his details and can request to have a previous
prescription being reissued. In case of multiple prescription can choose which to 
have and a message will be displayed. If the patient tries to request an appointment,
a message will be displayed advising to call the surgery"""

print("Test 3")

import pandas as pd
prescription_list = pd.DataFrame(columns = ["Medicine", "Patient", "Patient address", "Doctor", "Quantity", "Dosage"])

class Healthcare_Professional:
    """Super class Healthcare_Professional will pass its attributes
    and methods to the classes Doctor and Nurse"""
    def __init__(self, h_name, h_employee_number):
        self.h_name = str(h_name)
        self.h_employee_number = str(h_employee_number)
    
        
    def consultation(self):
        consultation = input("Consultation: ")
        return "Patient seen by " + self.h_name + ". Findings: " + consultation


class Doctor(Healthcare_Professional):
    def __init__(self,h_name, h_employee_number):
           self.h_name = str(h_name)
           self.h_employee_number = str(h_employee_number)
             
    def issue_prescription(self, medicine, p_name, p_address, h_name, quantity, dosage):
        global prescription_list
        prescription_list.loc[len(prescription_list)] = [medicine, p_name, p_address, h_name, quantity, dosage]
        return prescription_list

class Nurse(Healthcare_Professional):
    def __init__(self, h_name, h_employee_number):
        self.h_name = str(h_name)
        self.h_employee_number = str(h_employee_number)

class Prescription:
    
    def __init__(self, medicine, p_name,p_address, h_name, quantity, dosage):
        self.medicine = medicine
        self.p_name = p_name
        self.p_address = p_address
        self.h_name = h_name
        self.quantity = quantity
        self.dosage = dosage

class Patient:
    
    def __init__(self, p_name, p_address, p_phone):
        self.p_name = str(p_name)
        self.p_address = str(p_address)
        self.p_phone = str(p_phone)
    

    def request_repeat(self):
        global prescription_list
        p_name = input("Enter your name: ")
        print(prescription_list[prescription_list["Patient"] == p_name].reset_index(drop = True))
        selection = input("Select ID of prescription to be reissued:")
        return "A prescription for " + str(prescription_list[prescription_list["Patient"] == p_name].reset_index(drop = True).iloc[int(selection), 0]) + " has been reissued at your local pharmacy"
    
   
    def request_appointment(self):
        print("Call surgery to make an appointment")

D = Doctor("Valentino Rossi", "46")
D.issue_prescription("Aspirin", "Lewis", "44 Mercedes Road", "Valentino Rossi", 20, 3)
D.issue_prescription("Paracetamol", "Lance Stroll", "18 Aston Court", "Valentino Rossi", 16, 2)
P = Patient("Lewis", "44 Mercedes Road", "07777777")
P.request_repeat()
P.request_appointment()

"""TEST 4"""
"""The receptionist enters his name and employee number, then will be able to 
make appointments for the patients. The appointments will be saved into a 
dataframe containing all the appointments made and already scheduled.
After making an appointment will be displayed all the appointments in the dataframe."""

print("Test 4")

import pandas as pd
prescription_list = pd.DataFrame(columns = ["Medicine", "Patient", "Patient address", "Doctor", "Quantity", "Dosage"])
appointment_list = pd.DataFrame(columns = ["Date: ", "Time slot: ", "Urgency: ", "Patient Name", "Patient address: ", "Patient Phone", "Visited By", "Staff Number"])

class Healthcare_Professional:
    """Super class Healthcare_Professional will pass its attributes
    and methods to the classes Doctor and Nurse"""
    def __init__(self, h_name, h_employee_number):
        self.h_name = str(h_name)
        self.h_employee_number = str(h_employee_number)
    
        
    def consultation(self):
        consultation = input("Consultation: ")
        return "Patient seen by " + self.h_name + ". Findings: " + consultation


class Doctor(Healthcare_Professional):
    def __init__(self,h_name, h_employee_number):
           self.h_name = str(h_name)
           self.h_employee_number = str(h_employee_number)
             
    def issue_prescription(self, medicine, p_name, p_address, h_name, quantity, dosage):
        global prescription_list
        prescription_list.loc[len(prescription_list)] = [medicine, p_name, p_address, h_name, quantity, dosage]
        return prescription_list

class Nurse(Healthcare_Professional):
    def __init__(self, h_name, h_employee_number):
        self.h_name = str(h_name)
        self.h_employee_number = str(h_employee_number)

class Prescription:
    
    def __init__(self, medicine, p_name,p_address, h_name, quantity, dosage):
        self.medicine = medicine
        self.p_name = p_name
        self.p_address = p_address
        self.h_name = h_name
        self.quantity = quantity
        self.dosage = dosage

class Patient:
    
    def __init__(self, p_name, p_address, p_phone):
        self.p_name = str(p_name)
        self.p_address = str(p_address)
        self.p_phone = str(p_phone)
    

    def request_repeat(self):
        global prescription_list
        p_name = input("Enter your name: ")
        print(prescription_list[prescription_list["Patient"] == p_name].reset_index(drop = True))
        selection = input("Select ID of prescription to be reissued:")
        return "A prescription for " + str(prescription_list[prescription_list["Patient"] == p_name].reset_index(drop = True).iloc[int(selection), 0]) + " has been reissued at your local pharmacy"
    
  
    def request_appointment(self):
        print("Call surgery to make an appointment")

class Appointment():
    
    def __init__(self, date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number):
        self.date = date
        self.time_slot = time_slot
        self.urgency = urgency
        self.p_name = p_name
        self.p_address = p_address
        self.p_phone = p_phone
        self.h_name = h_name
        self.h_employee_number = h_employee_number
       

class Receptionist:
    def __init__(self, r_name, r_employee_number):
        self.r_name = str(r_name)
        self.r_employee_number = str(r_employee_number)
        
   
    def make_appointment(self, date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number):
        global appointment_list
        appointment_list.loc[len(appointment_list)] = [date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number]
        return appointment_list

    def cancel_appointment(self):
        global appointment_list
        p_name = input("Enter patient name that wants to cancel: ")
        print(appointment_list[appointment_list["Patient Name"] == p_name])
        selection = input("Select ID of appointment to cancel:")
        appointment_list = appointment_list.drop(index = int(selection))
        return "The appointment has been cancelled"


class Appointment_schedule:

    def __init__(self, date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number):
        
        self.appointments = [Appointment(date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number)]
      
    def add_appointment(self, date, time_slot,urgency, p_name, p_address, p_phone, h_name, h_employee_number):
        global appointment_list
        appointment_list.loc[len(appointment_list)] = [date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number]
        return appointment_list
        
   
    def cancel_scheduled_appointment(self):
        global appointment_list
        p_name = input("Enter patient name that wants to cancel scheduled appointment: ")
        print(appointment_list[appointment_list["Patient Name"] == p_name])
        selection = input("Select ID of appointment to cancel:")
        appointment_list = appointment_list.drop(index = int(selection))
        return "The scheduled appointment has been cancelled"
    
   
    def show_schedule(self):
        print("Surgery opened daily from 0900 to 1700. Every appointment slot is 1 hour and last appointment is at 1600")
        print(appointment_list.sort_values(by=["Date: ", "Time slot: "],axis = 0, ascending = True))


R = Receptionist("Toto Wolff", "8")
R.make_appointment("01-01-2022", "1200", "Standard", "Lando", "4 Mclaren road", "9837", "Valentino Rossi", "46")
R.make_appointment("01-01-2022", "1100", "Urgent", "Guenther", "10 Haas Avenue", "23453", "Valentino Rossi", "46")
R.make_appointment("04-01-2022", "1500", "Urgent", "Charles", "16 Ferrari road", "374097", "Valentino Rossi", "46")
R.make_appointment("04-01-2022", "1500", "Standard", "Max", "1 Red Bull road", "55735", "Valentino Rossi", "46")


"""TEST 5"""
"""The receptionist enters his name and employee number, then will be able to 
cancel appointments for the patients. The receptionist needs to enter the name
of the patient that wants to cancel the appointment. The global dataframe will
display all the appointments with that patient name and then the receptionist 
can select which appointment to cancel."""

print("Test 5")

import pandas as pd
prescription_list = pd.DataFrame(columns = ["Medicine", "Patient", "Patient address", "Doctor", "Quantity", "Dosage"])
appointment_list = pd.DataFrame(columns = ["Date: ", "Time slot: ", "Urgency: ", "Patient Name", "Patient address: ", "Patient Phone", "Visited By", "Staff Number"])

class Healthcare_Professional:
    """Super class Healthcare_Professional will pass its attributes
    and methods to the classes Doctor and Nurse"""
    def __init__(self, h_name, h_employee_number):
        self.h_name = str(h_name)
        self.h_employee_number = str(h_employee_number)
    
        
    def consultation(self):
        consultation = input("Consultation: ")
        return "Patient seen by " + self.h_name + ". Findings: " + consultation


class Doctor(Healthcare_Professional):
    def __init__(self,h_name, h_employee_number):
           self.h_name = str(h_name)
           self.h_employee_number = str(h_employee_number)
             
    def issue_prescription(self, medicine, p_name, p_address, h_name, quantity, dosage):
        global prescription_list
        prescription_list.loc[len(prescription_list)] = [medicine, p_name, p_address, h_name, quantity, dosage]
        return prescription_list

class Nurse(Healthcare_Professional):
    def __init__(self, h_name, h_employee_number):
        self.h_name = str(h_name)
        self.h_employee_number = str(h_employee_number)

class Prescription:
    
    def __init__(self, medicine, p_name,p_address, h_name, quantity, dosage):
        self.medicine = medicine
        self.p_name = p_name
        self.p_address = p_address
        self.h_name = h_name
        self.quantity = quantity
        self.dosage = dosage

class Patient:
    
    def __init__(self, p_name, p_address, p_phone):
        self.p_name = str(p_name)
        self.p_address = str(p_address)
        self.p_phone = str(p_phone)
    

    def request_repeat(self):
        global prescription_list
        p_name = input("Enter your name: ")
        print(prescription_list[prescription_list["Patient"] == p_name].reset_index(drop = True))
        selection = input("Select ID of prescription to be reissued:")
        return "A prescription for " + str(prescription_list[prescription_list["Patient"] == p_name].reset_index(drop = True).iloc[int(selection), 0]) + " has been reissued at your local pharmacy"
    
  
    def request_appointment(self):
        print("Call surgery to make an appointment")

class Appointment():
    
    def __init__(self, date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number):
        self.date = date
        self.time_slot = time_slot
        self.urgency = urgency
        self.p_name = p_name
        self.p_address = p_address
        self.p_phone = p_phone
        self.h_name = h_name
        self.h_employee_number = h_employee_number
       

class Receptionist:
    def __init__(self, r_name, r_employee_number):
        self.r_name = str(r_name)
        self.r_employee_number = str(r_employee_number)
        
   
    def make_appointment(self, date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number):
        global appointment_list
        appointment_list.loc[len(appointment_list)] = [date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number]
        return appointment_list

    def cancel_appointment(self):
        global appointment_list
        p_name = input("Enter patient name that wants to cancel: ")
        print(appointment_list[appointment_list["Patient Name"] == p_name])
        selection = input("Select ID of appointment to cancel:")
        appointment_list = appointment_list.drop(index = int(selection))
        return "The appointment has been cancelled"


class Appointment_schedule:

    def __init__(self, date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number):
        
        self.appointments = [Appointment(date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number)]
      
    def add_appointment(self, date, time_slot,urgency, p_name, p_address, p_phone, h_name, h_employee_number):
        global appointment_list
        appointment_list.loc[len(appointment_list)] = [date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number]
        return appointment_list
        
   
    def cancel_scheduled_appointment(self):
        global appointment_list
        p_name = input("Enter patient name that wants to cancel scheduled appointment: ")
        print(appointment_list[appointment_list["Patient Name"] == p_name])
        selection = input("Select ID of appointment to cancel:")
        appointment_list = appointment_list.drop(index = int(selection))
        return "The scheduled appointment has been cancelled"
    
   
    def show_schedule(self):
        print("Surgery opened daily from 0900 to 1700. Every appointment slot is 1 hour and last appointment is at 1600")
        print(appointment_list.sort_values(by=["Date: ", "Time slot: "],axis = 0, ascending = True))


R = Receptionist("Toto Wolff", "8")
R.make_appointment("01-01-2022", "1200", "Standard", "Lando", "4 Mclaren road", "9837", "Valentino Rossi", "46")
R.make_appointment("01-01-2022", "1100", "Urgent", "Guenther", "10 Haas Avenue", "23453", "Valentino Rossi", "46")
R.make_appointment("04-01-2022", "1500", "Urgent", "Charles", "16 Ferrari road", "374097", "Valentino Rossi", "46")
R.make_appointment("04-01-2022", "1500", "Standard", "Max", "1 Red Bull road", "55735", "Valentino Rossi", "46")
R.cancel_appointment()

"""TEST 6"""
"""The Appointment schedule allows to check the appointments already scheduled.
By inserting the details of an appointment to be saved, it will be possible to 
access the scheduler and check when there is availability. The scheduler will
print the info regarding the surgery opening times and slot time for the 
appointments to help the receptionist to check when there is an appointment available.
The list of all appointments saved will be showed and sorted by date and time slot
in ascending order.
It is possible to add or cancel appointment from the scheduler by using one of the
related functions.
When cancelling an appointment a prompt message will confirm the cancellation """

print("Test 6")

import pandas as pd
prescription_list = pd.DataFrame(columns = ["Medicine", "Patient", "Patient address", "Doctor", "Quantity", "Dosage"])
appointment_list = pd.DataFrame(columns = ["Date: ", "Time slot: ", "Urgency: ", "Patient Name", "Patient address: ", "Patient Phone", "Visited By", "Staff Number"])

class Healthcare_Professional:
    """Super class Healthcare_Professional will pass its attributes
    and methods to the classes Doctor and Nurse"""
    def __init__(self, h_name, h_employee_number):
        self.h_name = str(h_name)
        self.h_employee_number = str(h_employee_number)
    
        
    def consultation(self):
        consultation = input("Consultation: ")
        return "Patient seen by " + self.h_name + ". Findings: " + consultation


class Doctor(Healthcare_Professional):
    def __init__(self,h_name, h_employee_number):
           self.h_name = str(h_name)
           self.h_employee_number = str(h_employee_number)
             
    def issue_prescription(self, medicine, p_name, p_address, h_name, quantity, dosage):
        global prescription_list
        prescription_list.loc[len(prescription_list)] = [medicine, p_name, p_address, h_name, quantity, dosage]
        return prescription_list

class Nurse(Healthcare_Professional):
    def __init__(self, h_name, h_employee_number):
        self.h_name = str(h_name)
        self.h_employee_number = str(h_employee_number)

class Prescription:
    
    def __init__(self, medicine, p_name,p_address, h_name, quantity, dosage):
        self.medicine = medicine
        self.p_name = p_name
        self.p_address = p_address
        self.h_name = h_name
        self.quantity = quantity
        self.dosage = dosage

class Patient:
    
    def __init__(self, p_name, p_address, p_phone):
        self.p_name = str(p_name)
        self.p_address = str(p_address)
        self.p_phone = str(p_phone)
    

    def request_repeat(self):
        global prescription_list
        p_name = input("Enter your name: ")
        print(prescription_list[prescription_list["Patient"] == p_name].reset_index(drop = True))
        selection = input("Select ID of prescription to be reissued:")
        return "A prescription for " + str(prescription_list[prescription_list["Patient"] == p_name].reset_index(drop = True).iloc[int(selection), 0]) + " has been reissued at your local pharmacy"
    
  
    def request_appointment(self):
        print("Call surgery to make an appointment")

class Appointment():
    
    def __init__(self, date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number):
        self.date = date
        self.time_slot = time_slot
        self.urgency = urgency
        self.p_name = p_name
        self.p_address = p_address
        self.p_phone = p_phone
        self.h_name = h_name
        self.h_employee_number = h_employee_number
       

class Receptionist:
    def __init__(self, r_name, r_employee_number):
        self.r_name = str(r_name)
        self.r_employee_number = str(r_employee_number)
        
   
    def make_appointment(self, date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number):
        global appointment_list
        appointment_list.loc[len(appointment_list)] = [date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number]
        return appointment_list

    def cancel_appointment(self):
        global appointment_list
        p_name = input("Enter patient name that wants to cancel: ")
        print(appointment_list[appointment_list["Patient Name"] == p_name])
        selection = input("Select ID of appointment to cancel:")
        appointment_list = appointment_list.drop(index = int(selection))
        return "The appointment has been cancelled"


class Appointment_schedule:

    def __init__(self, date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number):
        
        self.appointments = [Appointment(date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number)]
      
    def add_appointment(self, date, time_slot,urgency, p_name, p_address, p_phone, h_name, h_employee_number):
        global appointment_list
        appointment_list.loc[len(appointment_list)] = [date, time_slot, urgency, p_name, p_address, p_phone, h_name, h_employee_number]
        return appointment_list
        
   
    def cancel_scheduled_appointment(self):
        global appointment_list
        p_name = input("Enter patient name that wants to cancel scheduled appointment: ")
        print(appointment_list[appointment_list["Patient Name"] == p_name])
        selection = input("Select ID of appointment to cancel:")
        appointment_list = appointment_list.drop(index = int(selection))
        return "The scheduled appointment has been cancelled"
    
   
    def show_schedule(self):
        print("Surgery opened daily from 0900 to 1700. Every appointment slot is 1 hour and last appointment is at 1600")
        print(appointment_list.sort_values(by=["Date: ", "Time slot: "],axis = 0, ascending = True))


R = Receptionist("Toto Wolff", "8")
R.make_appointment("01-01-2022", "1200", "Standard", "Lando", "4 Mclaren road", "9837", "Valentino Rossi", "46")
R.make_appointment("01-01-2022", "1100", "Urgent", "Guenther", "10 Haas Avenue", "23453", "Valentino Rossi", "46")
R.make_appointment("04-01-2022", "1500", "Urgent", "Charles", "16 Ferrari road", "374097", "Valentino Rossi", "46")
R.make_appointment("04-01-2022", "1500", "Standard", "Max", "1 Red Bull road", "55735", "Valentino Rossi", "46")


App = Appointment_schedule("02-01-2022", "0900", "Urgent", "Valtteri", "77 Alfa street", "556777655", "Valentino Rossi", "46")
App.show_schedule()
App.add_appointment("02-01-2022", "0900", "Urgent", "Valtteri", "77 Alfa street", "556777655", "Valentino Rossi", "46")
App.cancel_scheduled_appointment()