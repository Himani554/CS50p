import csv

students=[]
def main():
     a=int(input("Do you want to check the data or insert the data (Choose 1 to check or 2 to insert the data): "))
     data = Data(a)
     print(data)


def Reader(s):
    with open("data.csv") as file:
        reader=csv.DictReader(file)
        for row in reader:
            students.append(row)
        for student in students:
                if student["Registration No."]==s:
                     return f"Registration No.: {student['Registration No.']}\nName: {student['Name']}\nCourse: {student['Course']}\nResults-\n1st Semester: {student['1st Semester']}\n2nd Semester: {student['2nd Semester']}\n3rd Semester: {student['3rd Semester']}\n4th Semester: {student['4th Semester']}\n5th Semester: {student['5th Semester']}\n6th Semester: {student['6th Semester']}\n7th Semester: {student['7th Semester']}\n8th Semester: {student['8th Semester']}\n"
                else:
                     return f"Student not found"


def Writer():
    RegistrationNo = int(input("Registration No.: "))
    Name=input("Name: ")
    Course=input("Course: ")
    sem1=input("1st Semester: ")
    sem2=input("2nd Semester: ")
    sem3=input("3rd Semester: ")
    sem4=input("4th Semester: ")
    sem5=input("5th Semester: ")
    sem6=input("6th Semester: ")
    sem7=input("7th Semester: ")
    sem8=input("8th Semester: ")



    with open("data.csv","a") as file:
         writer=csv.DictWriter(file,fieldnames=["Registration No.","Name","Course","1st Semester","2nd Semester","3rd Semester","4th Semester","5th Semester","6th Semester","7th Semester","8th Semester"])
         writer.writerow({"Registration No.":RegistrationNo,"Name":Name,"Course":Course,"1st Semester":sem1,"2nd Semester":sem2,"3rd Semester":sem3,"4th Semester":sem4,"5th Semester":sem5,"6th Semester":sem6,"7th Semester":sem7,"8th Semester":sem8})
    return("Your data have been stored")


def Data(a):
    if a == 1:
         number = input("Enter your Registration No.: ")
         data=Reader(number)
         return(data)
    elif a==2:
         data=Writer()
         return(data)
    else:
         return("Invalid No.")




if __name__ == "__main__":
    main()
