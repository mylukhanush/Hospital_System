from specialization import *
from utility import input_is_valid

print("AIG HOSPITALS")
class OperationsManager:
    def __init__(self):
        self.specs = []



    def print_menu(self):
        print("Program Options: ")
        messages = [
            '1) Check in patients',
            '2) Print all patients',
            '3) Get next patient',
            '4) Check out patient',
            # '5) End the program',
            '5) Doctors Avaliable'
        ]
        print('\n'.join(messages))
        msg = f"Enter your choice from 1 to {len(messages)} \n"
        return input_is_valid(msg, 1, len(messages))

    def run(self):
        choice = self.print_menu()
        while True:
            if choice == 1:
                spec_name = str(input("Enter specialization: "))
                patient_name = str(input("Enter patient name: "))
                patient_status = int(input("Enter status (0 normal / 1 Emergency`) "))
                spec_exist = False
                for spec_obj in self.specs:
                    if spec_obj.name == 'Specialization ' + spec_name:
                        spec_exist = True
                if spec_exist:
                    spec_obj.Check_in_patient(patient_name, patient_status)
                else:
                    new_spec = Specialization(spec_name)
                    new_spec.Check_in_patient(patient_name, patient_status)
                    self.specs.append(new_spec)

            elif choice == 2:
                for spec in self.specs:
                    print(f'{spec.name}: There are {len(spec.queue)} patients')
                    spec.print_patients()

            elif choice == 3:
                spec_name = str(input("Enter specialization: "))
                found = False
                for spec in self.specs:
                    if spec.name == 'Specialization ' + spec_name:
                        spec.get_next_patient()
                        found = True
                if not found:
                    print("There is no Specialization with this name")

            elif choice == 4:
                spec_name = str(input("Enter specialization: "))
                patient_name = str(input("Enter patient name: "))
                for spec in self.specs:
                    if spec.name == 'Specialization ' + spec_name:
                        try:
                            spec.remove_patient(patient_name)
                        except:
                            print("No patient with such a name in this Specialization !")
                        spec.print_patients()
            elif choice == 5 :
                Specialization.Doctors_Avaliable("B")
                    # print("Doctors_Aval")



            else:
                print("Invalid choice. Please select a valid option.")
            choice = self.print_menu()

a = OperationsManager()
a.run()