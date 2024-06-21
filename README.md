# Job Application System README

## Overview
The Job Application System is a simple console-based application that allows two types of users - applicants and administrators - to interact with job applications. Applicants can fill out and manage their job applications, while administrators can oversee and manage all applications submitted to the system.

## Getting Started

### Prerequisites
- Python 3.x

### Running the Program
1. Clone or download the repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using Python:
   ```sh
   python job_application_system.py
   ```

### User Roles
Upon running the program, users can select their role:
1. **Applicant**
2. **Administrator**

## Applicant Functions

### 1. Fill Form
The applicant can fill out their job application form by selecting this option. The form will prompt for various details such as name, contact information, and other relevant details.

### 2. View Form
Applicants can view their completed application form to ensure all details are correct.

### 3. Submit Application
Submitting the application will create an instance of the application in the system. The job is automatically submitted once this action is performed.

### 4. Withdraw Form
If the applicant no longer wishes to apply for the job, they can withdraw their application. They also have the option to reactivate and resubmit the application if they change their mind.

### 5. Back to Main Menu
This option allows the applicant to return to the main menu to either switch roles or exit the program.

## Administrator Functions

### 1. Add Job Application
Administrators can manually add a job application to the system. Note that if an application is added before the applicant submits it, the form will have empty values. If added after submission, a duplicate application may be created.

### 2. Search Job Applications
Administrators can search for specific job applications based on criteria found in the form. This helps in filtering and locating applications easily.

### 3. Update Job Application
Administrators have the authority to update details in an applicant's form, such as name and mobile number.

### 4. Delete Job Application
If an application is no longer needed, administrators can delete it from the system.

### 5. Display All Job Applications
This option allows administrators to view all job applications currently available in the system.

## Code Structure
The code is structured into methods corresponding to each function available to the applicant and the administrator. The main menu prompts users to select their role, and subsequent menus guide them through available actions.

## Notes
- The "Back to Main Menu" option for applicants currently redirects to the admin menu due to time constraints during development. Ideally, this should lead back to the main user selection menu.
- Care should be taken when using the "Add Job Application" function to avoid duplicates.

## Future Improvements
- Separate user navigation for better user experience.
- Enhanced validation and error handling.
- Improved UI/UX for a more intuitive interaction.
