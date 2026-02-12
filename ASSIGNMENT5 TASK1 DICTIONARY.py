dict1 = {"Monika":75,"Rishabh":82,"Deepika":65,"Akhila":67,"Reuben":87}
student_name = input("Enter Student Name: ").title()

if student_name in dict1:
    value = dict1[student_name]
    print(f"{student_name}'s marks: {value}")
else:
    print("Student not found")