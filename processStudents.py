''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.) 

*   Create a dictionary of each student where the student ID is the key
    and the GPA is the value.

*  print out the dictionary

*  print out the corresponding GPA for student - 567890123

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv


# create a file object to open the file in read mode

def main():
    student_gpa_infile = open('student.csv', 'r') 


# create a csv object from the file object

    csv.reader = csv.reader(student_gpa_infile'\n')

#skip the header row


#create an outfile object for the pocessed record

    student_gpa_outfile = open('student.csv', )
    #csv.writer = csv.writer(student_gpa_outfile)

#create a new dictionary named 'student_dict'

    student_dict = {}

#use a loop to iterate through each row of the file
    for student in student_gpa_infile:


    #check if the GPA is below 3.0. If so, write the record to the outfile

        if student[9] in student_gpa_infile > 3.0:
            csv.writer(student_gpa_outfile, 'w' )
            # print('GPA: ', student[9])
            
        else: 
            csv.writer(student_gpa_infile'\n')



    # append the record to the dictionary with the student id as the Key
    # and the value as the GPA
    
    csv.writer(student_dict, 'a')




#print the entire dictionary

print(student_dict)

#Print the student id 


#print out the corresponding GPA from the dictionary



#close the outfile








