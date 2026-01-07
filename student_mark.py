def total(marks):
    return sum(marks)
def average(marks):
    return sum(marks)/len(marks)
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"
name=input("Enter your name: ")
num=int(input("Enter the number of subjects:"))
marks=[]
for i in range(num):
    mark=int(input("Enter marks:"))
    marks.append(mark)
total=total(marks)
average=average(marks)
grade=grade(total)
print("STUDENT DETAILS")
print("Name:",name)
print("Total:",total)
print("Average:",average)
print("Grade:",grade)


