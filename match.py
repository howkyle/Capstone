from app import db
from app.models import *
import json



gradeDict = {"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"U":7}
stud_list = []
subject_list =[]

capeSubjects= Cape.query.all()
students = Student.query.all()


class Student():
        def __init__(self, student_id, subjects, choices):
                self.id = student_id
                self.choices =[]
                self.subjects =[]

                for subject in subjects:
                	s = {}
                	s["subname"]= subject.subjectName
                	s["grade"] = subject.grade
                	self.subjects.append(s)

                for choice in choices:
                	c = {}
                	c["subname"]= choice.subjectName
                	c["priority"] = choice.subjectPriority
                	
                	# finds the prerequisite subject and gets grade
                	result = Cape.query.filter_by(subjectName = choice.subjectName)
                	if result:
                		preReq = result[0].prerequisiteSubject
                		if preReq == "None":
                			c["preReqGrade"] = 1
                		else:
                                        for sub in self.subjects:
	                			if sub["subname"] == preReq:
	                				grade =sub["grade"]
	                				c["preReqGrade"] = gradeDict[grade]

	                c["subScore"] = c["preReqGrade"]*c["priority"]+(0.5*c["preReqGrade"])
                	self.choices.append(c)

                def choseSubject(subname):
                        for choice in self.choices:
                                if choice["subname"] = subname:
                                        return True
                        return False
         

class Subject():
        def __init__(self, name, capacity, preReqs):
                self.name = name
                self.capacity = capacity
                self.preReqs = preReqs
                self.enrolledStudents = [] #list of students enrolled in course.

        def enrollMany(self, students): #adds students from already sorted stack until capacity runs out.
                j = 0
                x = 0
                while(self.capacity > 0 and x < len(students) ):
                        self.enrolledStudents.append(students[j])
                        self.capacity -= 1
                        j += 1
                        x += 1

        def enroll(self, oneStudent):
                self.enrolledStudents.append(oneStudent)

        def listStudents(self):
                for x in self.enrolledStudents:
                        print x.iden


        def chooseStudents(self, stud_list):
        # subject takes students with the lowest subScore for that subject


for subject in capeSubjects:
        subject_list.append(Subject(subject.subjectName, subject.capacity,subject.prerequisiteSubject))

for student in students:
	subjects = Studied.query.filter_by(studentID = student.studentID)
	choices = Application.query.filter_by(studentID = student.studentID)
        stud_list.append(Student(student.studentID, subjects,choices))


for student in stud_list:
        print student.choices

