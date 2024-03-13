from enum import Enum

class Company:
    '''this is the class company of the form owner company'''
    def __init__(self, company_name: str, company_address: str) -> None:
        self.__company_name = company_name
        self.__company_address = company_address

    @property
    def company_name(self):
        return self.__company_name

    @property
    def company_address(self):
        return self.__company_address

    def __str__(self) -> str:
        return f"Company Name: {self.__company_name}\nCompany Address: {self.__company_address}"
    
    def __repr__(self) -> str:
        return str(self)

class Experience:
    def __init__(self,title:str,institution:str, start_date:str, end_date:str) -> None:
        self.__title=title
        self.__institution=institution
        self.__start_date= start_date
        self.__end_date = end_date
    
    @property
    def title(self):
        return self.__title
    
    @property
    def institution(self):
        return self.__institution
    
    @property
    def start_date(self):
        return self.__start_date
    
    @property
    def end_date(self):
        return self.__end_date
    
    def __str__(self) -> str:
        return f"{self.__title}\nInstitution/Company:{self.__institution}\nStart-Date:{self.__start_date}\nEnd-Date:{self.__end_date}\n"
    

class Education(Experience):
    def __init__(self, title: str, institution: str, start_date: str, end_date: str, degree:str) -> None:
        super().__init__(title, institution, start_date, end_date) 
        self.__degree= degree

    @property
    def degree(self):
        return self.__degree
    
    def __str__(self):
        return f"Education level: {super().__str__()}Degree: {self.__degree}\n"   

class Work_Experience(Experience):
    def __init__(self, title: str, institution: str, start_date: str, end_date: str,reason_leave:str) -> None:
        super().__init__(title, institution, start_date, end_date) 
        self.__reason_to_leave= reason_leave

    @property
    def reasontoleave(self):
        return self.__reasontoleave
    
    def __str__(self):
        return f"Position: {super().__str__()}Reason to leave: {self.__reason_to_leave}\n"

class Emergency_Contact_Person:
    def __init__(self, name: str, relationship: str, contact_num: str) -> None:
        self.__name = name
        self.__relationship = relationship
        self.__contact_num = contact_num

    @property
    def name(self):
        return self.__name

    @property
    def relationship(self):
        return self.__relationship

    @property
    def contact_num(self):
        return self.__contact_num

    def __str__(self):
        return f"Emergency Contact: {self.name}\nRelationship: {self.relationship}\nContact Number: {self.contact_num}\n"

class Skills:
    def __init__(self, skill_name:str) -> None:
        self.__skills_name= skill_name
    
    @property
    def skills_name(self):
        return self.__skills_name
    
    def __str__(self) -> str:
        return f"Skill-Name: {self.__skills_name}\n"
    
class ApplicantStatus(Enum):
    ACTIVE = 'Active'
    HIRED = 'Hired'
    WITHDRAWN = 'Withdrawn'       
    
class Applicant:
    def __init__(self, firstname: str = "", lastname: str = "", middleinitial: str = "", date_of_birth: str = "",
                 address_number: int = 0, address_street: str = "", address_city: str = "",
                 telephone_home: str = "", telephone_mobile: str = "", email_address: str = "",
                 place_of_birth_city: str = "", place_of_birth_country: str = "", citizenship: str = "", applied_job: str = "") -> None:
        self.__firstname = firstname
        self.__lastname = lastname
        self.__middleinitial = middleinitial
        self.__date_of_birth = date_of_birth
        self.__address_number = address_number
        self.__address_street = address_street
        self.__address_city = address_city
        self.__telephone_home = telephone_home
        self.__telephone_mobile = telephone_mobile
        self.__email_address = email_address
        self.__place_of_birth_city = place_of_birth_city
        self.__place_of_birth_country = place_of_birth_country
        self.__citizenship = citizenship
        self.__education_list:list[Education]=[]
        self.__work_experience:list[Work_Experience]=[]
        self.__emergency_contact:list[Emergency_Contact_Person]=[]
        self.__skills:list[Skills]=[]
        self.__selected_job=applied_job
        self.__status = ApplicantStatus.ACTIVE
    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

    @property
    def middleinitial(self):
        return self.__middleinitial

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @property
    def address_number(self):
        return self.__address_number

    @property
    def address_street(self):
        return self.__address_street

    @property
    def address_city(self):
        return self.__address_city

    @property
    def telephone_home(self):
        return self.__telephone_home

    @property
    def telephone_mobile(self):
        return self.__telephone_mobile

    @property
    def email_address(self):
        return self.__email_address

    @property
    def place_of_birth_city(self):
        return self.__place_of_birth_city

    @property
    def place_of_birth_country(self):
        return self.__place_of_birth_country

    @property
    def citizenship(self):
        return self.__citizenship
    
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        if isinstance(new_status, ApplicantStatus):
            self.__status = new_status
        else:
            raise ValueError("Invalid status value.")
    
    def fill_form(self):
        self.__firstname = input("Enter your firstname: ")
        self.__lastname = input("Enter your last Name: ")

        self.__middleinitial = input("Enter your Middle Initial (Optional): ")
        self.__date_of_birth = input("Enter your Date of Birth (YYYY-MM-DD): ")
        self.__address_number = int(input("Enter your Address Number: "))
        self.__address_street = input("Enter your Address Street: ")
        self.__address_city = input("Enter your Address City: ")
        self.__telephone_home = input("Enter your Home Telephone: ")
        self.__telephone_mobile = input("Enter your Mobile Telephone: ")
        self.__email_address = input("Enter your Email Address: ")       
        self.__place_of_birth_city = input("Enter your Place of Birth City: ")
        self.__place_of_birth_country = input("Enter your Place of Birth Country: ")
        self.__citizenship = input("Enter your Citizenship: ")
        self.__selected_job = input("Enter the Job Position you are applying for: ")

        self.add_education()
        self.add_work_experience()
        self.add_emergency_contact()
        self.add_skills()
    
    def add_education(self)->None:
        while True:
            title = input("Enter Education Title (or 'complete' to finish): ")
            if title.lower() == 'complete':
                break

            institution = input("Enter Education Institution: ")
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            end_date = input("Enter End Date (YYYY-MM-DD): ")
            degree = input("Enter Degree: ")

            self.__education_list.append(Education(title, institution, start_date, end_date, degree))

    def add_work_experience(self)->None:
        while True:
            title = input("Enter Work Experience Title (or 'complete' to finish): ")
            if title.lower() == 'complete':
                break

            institution = input("Enter Work Experience Institution: ")
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            end_date = input("Enter End Date (YYYY-MM-DD): ")
            reason_to_leave = input("Enter Reason to Leave: ")

            self.__work_experience.append(Work_Experience(title, institution, start_date, end_date, reason_to_leave))
    
    def add_emergency_contact(self)->None:
        i = 0
        while i < 2:
            name = input("Enter 2 Emergency Contact Name (or 'complete' to finish): ")
            if name.lower() == 'complete':
                break

            relationship = input("Enter Relationship: ")
            contact_num = input("Enter Contact Number: ")

            self.__emergency_contact.append(Emergency_Contact_Person(name, relationship, contact_num))
            i += 1
    
    def add_skills(self)->None:
        skill = 0
        while skill < 7:
            skill_name = input("Enter Skill Name (max 7 skills you can put)(or 'complete' to finish): ")
            if skill_name.lower() == 'complete':
                break

            self.__skills.append(Skills(skill_name))
            skill += 1
    
    def view_form(self)->None:
        print(self.__str__())
    
    def withdraw_form(self) -> None:
        if not self.__firstname:
            print("No existing application to withdraw.")
        else:
            confirmation = input("Are you sure you want to withdraw your application? (yes/no): ").lower()
            if confirmation == 'yes':
                print("Application withdrawn successfully.")
                self.__status = ApplicantStatus.WITHDRAWN
            else:
                print("Withdrawal canceled.")
    
    def __iter__(self):
        self.__index = -1
        return self
    
    def __next__(self):
        # Iterate over education, work experience, emergency contact, and skills
        if self.__index < len(self.__education_list) - 1:
            self.__index += 1
            return self.__education_list[self.__index]
        elif self.__index < len(self.__work_experience) + len(self.__education_list) - 1:
            self.__index += 1
            return self.__work_experience[self.__index - len(self.__education_list)]
        elif self.__index < len(self.__emergency_contact) + len(self.__work_experience) + len(self.__education_list) - 1:
            self.__index += 1
            return self.__emergency_contact[self.__index - len(self.__work_experience) - len(self.__education_list)]
        elif self.__index < len(self.__skills) + len(self.__emergency_contact) + len(self.__work_experience) + len(
                self.__education_list) - 1:
            self.__index += 1
            return self.__skills[self.__index - len(self.__emergency_contact) - len(self.__work_experience) - len(
                self.__education_list)]
        else:
            raise StopIteration
        
    def update_details(self, value_update: str, new_value: str) -> None:
        valid_attributes = ['firstname', 'lastname', 'telephone_mobile']

        if value_update in valid_attributes:
            if value_update == 'firstname':
                self.__firstname = new_value
            elif value_update == 'lastname':
                self.__lastname = new_value
            elif value_update == 'telephone_mobile':
                self.__telephone_mobile = new_value

            print(f"{value_update} updated successfully.")
        else:
            print(f"Invalid attribute '{value_update}', cannot update.")

    def __str__(self) -> str:
        education_str = "\n".join([f"-{edu}" for edu in self.__education_list])
        work_experience_str = "\n".join([f"- {exp}" for exp in self.__work_experience])
        emergency_contact_str = "\n".join([f"- {ec}" for ec in self.__emergency_contact])
        skills_str = "\n".join([f"- {skill}" for skill in self.__skills])

        return f"  Applicant Full-Name: {self.__firstname} {self.__lastname} {self.__middleinitial}\n" \
               f"  Date of Birth: {self.__date_of_birth}\n" \
               f"  Address: {self.__address_number} {self.__address_street}, {self.__address_city}\n" \
               f"  Telephone: Home - {self.__telephone_home}, Mobile - {self.__telephone_mobile}\n" \
               f"  Email: {self.__email_address}\n" \
               f"  Place of Birth: {self.__place_of_birth_city}, {self.__place_of_birth_country}\n" \
               f"  Citizenship: {self.__citizenship}\n" \
               f"  Applied Job: {self.__selected_job}\n" \
               f"  Education:\n{education_str}\n" \
               f"  Work Experience:\n{work_experience_str}\n" \
               f"  Emergency Contacts:\n{emergency_contact_str}\n" \
               f"  Skills:\n{skills_str}\n"\
               f"  Application Status--{self.__status}"
    
    def __repr__(self):
        return str(self)
    
    def create_job_application(self):
        return Job_Application(self)

class Job_Application:
    def __init__(self, applicant: Applicant) -> None:
        self.__applicant = applicant

    @property
    def applicant(self) -> Applicant:
        return self.__applicant
    
    def display_application_details(self) -> str:
        return self.__str__()

    def __str__(self):
        return f"{self.__applicant}"
    
    def __repr__(self) -> str:
        return str(self)

class ApplicationAdmin:
    def __init__(self, company:Company) -> None:
        self.__applications:list[Job_Application] = []
        self.__company= company
    
    @property
    def company(self)->Company:
        return self.__company
   
    def __iter__(self):
        self.__index = -1
        return self
    
    def __next__(self):
        if self.__index >= len(self.__applications)-1:
            raise StopIteration
        self.__index += 1
        return (self.__applications[self.__index])
    
    def add_jobapplications(self, job_Application: Job_Application) -> None:
        new_applicant_name = job_Application.applicant.firstname + " " + job_Application.applicant.lastname

        for application in self.__applications:
            existing_applicant_name = application.applicant.firstname + " " + application.applicant.lastname

            if new_applicant_name.lower() == existing_applicant_name.lower():
                print("Application with the same name already exists. Cannot add duplicate application.")
                return

        self.__applications.append(job_Application)
        print("Application added successfully.")
    
    def delete_application(self) -> None:
        if self.__applications:
            self.__applications.pop()
            print("Application deleted sucessfully")
        else:
            print("No Application to delete")

    def search_applications(self, criteria: str) -> list[Job_Application]:
        matching_applications = []

        for application in self.__applications:
            applicant_name = str(application)
            if criteria.lower() in applicant_name:
                matching_applications.append(application)

        if matching_applications:
            print("Applications found with the name:")
            for matching_application in matching_applications:
                print(matching_application.display_application_details())
        else:
            print("No applications found with that name.")

    def display_applications(self) -> None:
        for application in self.__applications:
            print (application.display_application_details())
    
    def __str__(self) -> str:
        output =  f"Company name = {self.__company}\n"
        output += "The application: "
        for application in self.__applications:
            output += str(application) + '\n'
        return output
    
    def __repr__(self):
        str(self)
    

def main():
    print("Welcome to the Job Application System!")

    user_type = input("Are you an Admin or an Applicant? Enter 'admin' or 'applicant': ").lower()
    company_instance = Company("ABC Corp", "123 Main Street, Cityville")
    admin_instance = ApplicationAdmin(company_instance)
    applicant_instance = Applicant()

    if user_type == 'admin':
        admin_menu(admin_instance, applicant_instance)
    elif user_type == 'applicant':
        submitted_application = applicant_menu(admin_instance, applicant_instance)
        # admin_instance.add_jobapplications(submitted_application)
        admin_menu(admin_instance, applicant_instance)


def admin_menu(admin_instance, applicant_instance):
    while True:
        print("\nAdmin Menu:")
        print("1. Add Job Application")
        print("2. Search Job Applications")
        print("3. Update Job Application")
        print("4. Delete Job Application")
        print("5. Display All Job Applications")
        print("0. Exit")

        choice = input("Enter your choice (0-5): ")

        if choice == '1':
            job_application = applicant_instance.create_job_application()
            admin_instance.add_jobapplications(job_application)
        elif choice == '2':
            name = input("Enter the any criteria to search: ")
            admin_instance.search_applications(name)
        elif choice == '3':
            value_update = input("Enter the attribute to update (e.g., firstname,lastname, telephone_mobile): ")
            new_value = input(f"Enter the new value for {value_update}: ")
            applicant_instance.update_details(value_update,new_value)
        elif choice == '4':
            admin_instance.delete_application()
    
        elif choice == '5':
            admin_instance.display_applications()
        elif choice == '0':
            print("Thank You :), Exiting.")
            exit()
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

def applicant_menu(admin_instance, applicant_instance):
    submitted_applications = []

    while True:
        print("\nApplicant Menu:")
        print("1. Fill Form")
        print("2. View Form")
        print("3. Submit Application")
        print("4. Withdraw Form")
        print("5. Back to Main Menu")
        print("0. Exit")

        choice = input("Enter your choice (0-5): ")

        if choice == '1':
            applicant_instance.fill_form()
        elif choice == '2':
            applicant_instance.view_form()
        elif choice == '3':
            job_application = applicant_instance.create_job_application()
            submitted_applications.append(job_application)
            print("Application submitted successfully.")
        elif choice == '4':
            applicant_instance.withdraw_form()
        elif choice == '5':
            print("Going back to the main menu.")
            return submitted_applications
        elif choice == '0':
            print("Thank You :), Exiting.")
            exit()
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

if __name__ == "__main__":
    main()
