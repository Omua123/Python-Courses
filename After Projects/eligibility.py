attended = int (input("Enter the number of days you attended: "))
absent = int (input("Enter the number of days you ere absent: "))

if attended / absent+attended >= 0.75:
    print ("You are eligible to take the exam")

else:
    print ("You are not eligible to take the exam")