
student_data  = {"Sajid":45,
                 "Raja":98,
                 "Muna":99,
                 "Shafi":88,
                 "Amir":66}

#Student having highest marks
hi_std_name = max(student_data,key=student_data.get)
#max_marks = max(student_data.values()) 
max_marks = student_data[hi_std_name]  #alternative way


#Student having lowest marks 
std_name = min(student_data,key=student_data.get)
#min_marks = min(student_data.value())
min_marks = student_data[std_name] #alternative way

print("Student name:",hi_std_name,"\tHighest marks:",max_marks)
print("Student name:",std_name,"\tLowest marks:",min_marks)