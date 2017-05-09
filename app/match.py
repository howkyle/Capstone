from app import db
from models import *
import json



gradeDict = {"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"U":7}
CapeSubjects= Cape.query.all()
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
                                print "RESULTTT"
                		preReq = result[0].prerequisiteSubject
                		if preReq == "None":
                			c["preReqGrade"] = 1
                		else:
                                        print "PREREQ NOT EMPTY"
                                        print preReq
                                        print 'LINEEE'
                                        print self.subjects
                			for sub in self.subjects:
                                                print "IN SUBJECT LOOP"
                                                print sub["subname"]
	                			if sub["subname"] == preReq:
	                				grade =sub["grade"]
	                				c["preReqGrade"] = gradeDict[grade]

	                c["subScore"] = c["preReqGrade"]*c["priority"]+(0.5*c["preReqGrade"])
	                print c["subname"]
	                print c["subScore"]


                	self.choices.append(c)
                

stud_list = []

for student in students:
	subjects = Studied.query.filter_by(studentID = student.studentID)
        print "SUBJECT QUERY RESULT"
        print subjects[0].subjectName
	choices = Application.query.filter_by(studentID = student.studentID)
	print "CHOICES QUERY RESULT"
        print choices[0].subjectName
        stud_list.append(Student(student.studentID, subjects,choices))

        #         #self.assignedScores = {}
        #         self.selectScore = {} #determines assignment priority.

        # def makeScoreDict(self): #calculates
        #         for i, j in enumerate(self.preferences):
        #                 #self.assignedScores[self.preferences[i]] = self.scores[i]
        #                 self.selectScore[self.preferences[i]] = (self.scores[i] * 1000) + 1
        # def printInfo(self):
        # 	print(self.iden)
        # 	print(self.preferences)
        # 	print(self.scores)
        # 	print(self.selectScore)
        # 	#print(self.assignedScores)