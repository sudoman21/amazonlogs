# File: q2.py
# Author: Angel Valdez
# Date: 11/19/19
# Section: 502
# E-mail: angelval@tamu.edu
# Description: This program takes all the student IDs and the grades for their 3 exams and calculates their final grade and then arranges them into different documents based on specific criteria.

file1 = open("exam_scores.txt","r")
student_grades = {}
student_ids = []
sorted_grades = {}
'''This for loop takes each line from the text file, converts it into a list, and then it strips all the non-numerical characters in order to convert the list items from strings to integers and perform mathematical operations later in the program. The loop also sets the student ID as a key and the grades as values and adds them to the dictionary student_grades. '''
for x in range(0,900):
    line = file1.readline().split()
    key = str(line[0:1])
    key = key.replace("'",'')
    key = key.replace("[",'')
    key = key.replace("]",'')
    key = key.strip()
    key = int(key)
    value = line[1:4]
    value = list(map(int, value))
    student_grades[key] = value

file1.close()
file2 = open("grades.txt","w")
'''This for loop takes the values from each key which are the scores for the three exams of each students and divides them by their respective percentage then adds them together to determine the final average and replaces the exam grades for the final average in the dictionary student_grades'''
for key,value in student_grades.items():
    value = (0.25 * value[0])+(0.35 * value[1])+(0.40 * value[2])
    updated_grade = {key:value}
    student_grades.update(updated_grade)
'''This for loop takes each students ID, their final average and calculates their final grade based on the average and prints it line by line unordered in the text file grades.txt '''
for key,value in (student_grades.items()):
    if value >= 90:
        final_grade = "A"
    
    elif value >= 80:
        final_grade = "B"
        
    elif value >= 70:
        final_grade = "C"    
        
    elif value >= 60:
        final_grade = "D"
        
    elif value < 60:
        final_grade = "F"    
    
    file2.write(str(f"ID :{key} has a score of {round(value,1)} Letter grade : {final_grade}\n"))
    
file2.close
file3 = open("sorted_ids.txt","w") 
'''This for loop takes each students ID, their final average and calculates their final grade based on the average and prints it line by line sorted by ID from lowest to highest in the text file sorted_ids.txt '''
for key,value in sorted(student_grades.items()):
    if value >= 90:
        final_grade = "A"
    
    elif value >= 80:
        final_grade = "B"
        
    elif value >= 70:
        final_grade = "C"    
        
    elif value >= 60:
        final_grade = "D"
        
    elif value < 60:
        final_grade = "F"    
    
    file3.write(str(f"ID :{key} has a score of {round(value,1)} Letter grade : {final_grade}\n"))
            
file3.close()
file4 = open("sorted_grades.txt","w")

sorted_grades = sorted(student_grades.items(), key=lambda x: x[1])

'''This for loop takes each students ID, their final average and calculates their final grade based on the average and prints it line by line sorted by the final average grade from lowest to highest in the text file sorted_grades.txt '''
for key,value in sorted_grades:
    if value >= 90:
        final_grade = "A"
    
    elif value >= 80:
        final_grade = "B"
        
    elif value >= 70:
        final_grade = "C"    
        
    elif value >= 60:
        final_grade = "D"
        
    elif value < 60:
        final_grade = "F"    
    
    file4.write(str(f"ID :{key} has a score of {round(value,1)} Letter grade : {final_grade}\n"))
    
file4.close()
