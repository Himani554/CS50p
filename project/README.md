# To save and check the result of students
#### Video Demo: https://youtu.be/bJdRcQyr1WU
#### Description:
This project involves developing a Python program that handles student data using CSV files.
The user can either check the data for a specific student or insert new student data into the file.
The program uses two key functionalities: Reader, for retrieving data based on a student's registration number, and Writer, for inserting new student data.
CSV is the primary format used for storing the information, ensuring that data is easily readable and writable in a structured manner.

Key Features
1. Main Function:
The main function is the entry point of the program.
It prompts the user to choose whether they want to check or insert data.
Depending on their selection, the Data function is called with an argument representing their choice (1 for checking data, 2 for inserting data).
After the operation is completed, the result is printed to the console.

2. Reader Function:
The Reader function is responsible for reading student data from the data.csv file.
It takes a student's registration number as an argument, searches the CSV file for a match, and returns the student's details if found.
It uses Python’s csv.DictReader to parse the CSV file into a dictionary format, making it easy to search by specific field names such as "Registration No."

If a matching student is found, the function returns a formatted string with their registration number, name, course, and semester results (up to 8 semesters).
If the student is not found, it returns a "Student not found" message.

3. Writer Function:
The Writer function allows the user to insert new student data into the data.csv file.
It prompts the user to enter various details such as the registration number, name, course, and results for up to 8 semesters.
This data is then written to the CSV file using csv.DictWriter, appending it as a new row.

Once the data is stored, the function returns a message confirming that the data has been successfully saved.

CSV File Structure
The program uses a CSV file named data.csv to store student records. The CSV file includes the following fields:

Registration No.
Name
Course
1st Semester
2nd Semester
3rd Semester
4th Semester
5th Semester
6th Semester
7th Semester
8th Semester
This structure allows the program to manage and retrieve detailed information about each student’s academic performance over the course of 8 semesters.

Error Handling and Improvements
Handling Missing Students: In the Reader function, if a student is not found, a "Student not found" message is displayed.
This ensures that the user is informed when the data for a specific registration number does not exist.

Enhancements: One key improvement would be to add validation for the user input, such as checking if
the registration number is a valid integer or if the semester results follow a specific
format (e.g., ensuring the results are numeric or within a certain range).

Reading Performance: The Reader function appends all students into a list first and then checks for the required registration number.
This could be optimized by directly returning the result as soon as a matching student is found,
which would improve performance for large datasets.

Conclusion
This project is a simple and effective way to manage student data using Python and CSV files.
By offering functionality to both read and write data, the program serves as a flexible tool for managing student records.
It also introduces concepts such as file handling, user input, and CSV operations,
which are essential for building more complex data management applications.







