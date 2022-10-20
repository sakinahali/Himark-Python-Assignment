print("Input the aggregate score of students for each department")
score = int(input("> "))

if int(score) in range(0, 50):
    print("No Admission/Department")
elif int(score) in range(50, 55):
    print("Admitted to Agriculture department")
elif int(score) in range(55, 61):
    print("Admitted to Botany and Zoology departments")
elif int(score) in range(61, 71):
    print("Admitted to Computer science, Psychology and Statistics departments")
elif int(score) in range(71, 75):
    print("Admitted to Phamarcy, Physiology and Nursing departments")
elif int(score) in range(75, 80):
    print("Admitted to Banking and Finance, Accounting and Insurance departments")
elif int(score) in range(80, 101):
    print("Admitted to Medicine and Law departments")
else:
    print("Invalid Input!")