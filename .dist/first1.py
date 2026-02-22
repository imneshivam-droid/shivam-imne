# marksheet program 

print("________________STUDENT MARKSHEET__________________")

name = input ("Enter the name of the student:")
roll_no = input ("Enter the roll number of the student:")
marks = []
subjects = ["maths", "physics", "chemistry", "english", "compurter science"]
for subject in subjects:
    marks.append(float(input(f"Enter the marks for {subject}: ")))
    total = sum(marks)
    percentage = (total / 500)*100
    print("Total marks:", total)
    print("percentage:",percentage)
    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 80:
        print("Grade: B")
    elif percentage >= 70:
        print("Grade: C")
    elif percentage >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

    