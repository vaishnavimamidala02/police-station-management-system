from datetime import datetime
class FIR:
    def _init_(self, case_id, complainant_name, complainant_phone, complainant_address, case_type, description):
        self.case_id = case_id
        self.complainant_name = complainant_name
        self.complainant_phone = complainant_phone
        self.complainant_address = complainant_address
        self.case_type = case_type
        self.description = description
        self.status = 'pending'
        self.close_date = None
    def close_case(self):
        self.status = 'solved'
        self.close_date = datetime.now().strftime('%Y-%m-%d')
class PoliceStationManagement:
    def _init_(self):
        self.fir_records = []
        self.next_case_id = 1
    def file_fir(self):
        complainant_name = input("Enter Complainant Name: ").strip()
        complainant_phone = input("Enter Complainant Phone Number: ").strip()
        complainant_address = input("Enter Complainant Address: ").strip()
        case_type = input("Enter Case Type (civil/crime): ").strip()
        description = input("Enter Case Description: ").strip()
        if not complainant_name or not complainant_phone or not complainant_address or not case_type or not description:
            print("All fields are required. FIR not filed.")
            return
        for fir in self.fir_records:
            if fir.complainant_name == complainant_name and fir.complainant_phone == complainant_phone and fir.complainant_address == complainant_address and fir.case_type == case_type and fir.description == description:
                print("A similar case already exists. FIR not filed.")
                return
        fir = FIR(self.next_case_id, complainant_name, complainant_phone, complainant_address, case_type, description)
        self.fir_records.append(fir)
        print(f"FIR filed successfully: Case ID {self.next_case_id}")
        self.next_case_id += 1
    def close_case(self):
        try:
            case_id = int(input("Enter Case ID to close: "))
        except ValueError:
            print("Invalid Case ID. Please enter a numeric value.")
            return
        for fir in self.fir_records:
            if fir.case_id == case_id:
                if fir.status == 'pending':
                    fir.close_case()
                    print(f"Case ID {case_id} closed successfully on {fir.close_date}.")
                else:
                    print(f"Case ID {case_id} is already solved.")
                return
        print(f"Case ID {case_id} not found.")
    def classify_pending_cases(self):
        pending_cases = [fir for fir in self.fir_records if fir.status == 'pending']
        return pending_cases
    def classify_solved_cases(self):
        solved_cases = [fir for fir in self.fir_records if fir.status == 'solved']
        return solved_cases
    def display_cases(self, cases):
        if not cases:
            print("No cases to display.")
            return
        for fir in cases:
            close_date = fir.close_date if fir.close_date else "N/A"
            print(f"Case ID: {fir.case_id}, Complainant Name: {fir.complainant_name}, Phone: {fir.complainant_phone}, Address: {fir.complainant_address}, Type: {fir.case_type}, Status: {fir.status}, Close Date: {close_date}, Description: {fir.description}")
station = PoliceStationManagement()
while True:
    print("\nPolice Station Management System")
    print("1. File FIR")
    print("2. Close Case")
    print("3. View Pending Cases")
    print("4. View Solved Cases")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        station.file_fir()
    elif choice == '2':
        station.close_case()
    elif choice == '3':
        print("\nView Pending Cases:")
        case_type = input("Enter Case Type to filter (civil/crime): ").strip()
        if case_type in ['civil', 'crime']:
            filtered_cases = [case for case in station.classify_pending_cases() if case.case_type == case_type]
            station.display_cases(filtered_cases)
        else:
            print("Invalid Case Type. Please choose 'civil' or 'crime'.")
    elif choice == '4':
        print("\nView Solved Cases:")
        case_type = input("Enter Case Type to filter (civil/crime): ").strip()
        if case_type in ['civil', 'crime']:
            filtered_cases = [case for case in station.classify_solved_cases() if case.case_type == case_type]
            station.display_cases(filtered_cases)
        else:
            print("Invalid Case Type. Please choose 'civil' or 'crime'.")
    elif choice == '5':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")