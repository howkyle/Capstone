from app import db
from app.models import *
import json


class Applicant():
        def __init__(self, student_id, subjects, choices):
                self.id = student_id
                self.choices =[]
                self.subjects =[]
                self.successCount = 0

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

                @property
                def successCount(self):
                        return self.successCount

                @successCount.setter
                def successCount(self, value):
                        self.successCount = value

                def appliedFor(self,subname):
                        # checks to see if the student applied for this subject
                        for choice in self.choices:
                                if choice["subname"] == subname:
                                        return True
                        return False

         

class Subject():
        def __init__(self, name, capacity, preReqs):
                self.name = name
                self.capacity = capacity
                self.preReqs = preReqs
                self.potentialStudents = [] #all students who applied for this course
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


        def choosePotentialStudents(self, stud_list):
        # subject takes students with the lowest subScore for that subject
                for stud in stud_list:
                        for choice in stud.choices:
                                if choice["subname"] == self.name:
                                        self.potentialStudents.append((stud,choice["subScore"]))
                                        print stud.id
                                        print choice["subScore"]
                                        print self.potentialStudents
                                        break
                print "Sorting"
                self.potentialStudents.sort(key=lambda tup: tup[1]) 
                print self.potentialStudents





gradeDict = {"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"U":7}
stud_list = []
subject_list =[]

capeSubjects= Cape.query.all()
clist = []
for subject in capeSubjects:
        clist.append(subject.subjectName)
        # adds each cape subject from the database to a list
        subject_list.append(Subject(subject.subjectName, subject.capacity,subject.prerequisiteSubject))

print clist
print "ENDDDDDD OF CLIST"
students = Student.query.all()
for student in students:
        # makes a list of student objects to be used for matching 
	subjects = Studied.query.filter_by(studentID = student.studentID)
	choices = Application.query.filter_by(studentID = student.studentID)
        stud_list.append(Applicant(student.studentID, subjects,choices))


# TESTING
for student in stud_list:
        print student.choices

for sub in subject_list:
        print sub.name
        sub.choosePotentialStudents(stud_list)





