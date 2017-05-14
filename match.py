from app import db
from app.models import *
import json


class Applicant():
        def __init__(self, student_id, subjects, choices):
                self.id = student_id
                self.successfulApplicant = False
                self.choices =[]
                self.subjects =[]
                self.successCount = 0
                self.successfulSubs  = []
                self.choicePriorityDict = {} #dictionary of subject priorities and indexes for easy finding

                for subject in subjects:
                	s = {}
                	s["subname"]= subject.subjectName
                	s["grade"] = subject.grade
                	self.subjects.append(s)

                choiceCounter = 0
                for choice in choices:
                	c = {}
                	c["priority"] = choice.subjectPriority
                        c["subname"] = choice.subjectName
                	
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
                        self.choicePriorityDict[choice.subjectPriority] = choiceCounter
                        choiceCounter= choiceCounter+1

        @property
        def successCount(self):
                return self.successCount

        @successCount.setter
        def successCount(self, value):
                self.successCount = value

        @property
        def successfulApplicant(self):
                return self.successfulApplicant

        @successfulApplicant.setter
        def successfulApplicant(self, value):
                self.successfulApplicant = value

        def addSuccessfulSubject(self,subject):
                self.successfulSubs.append(subject)
                self.successCount+=1
                

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
                self.selectedStudents = [] #students that have been offered a place in the course
                self.selectedStudentsDict = {} #dictionary of student Id and student list indexes for easy access
                self.enrolledStudents = [] #list of students enrolled in course.


        def enrollMany(self, students): #adds students from already sorted stack until capacity runs out.
                j = 0
                x = 0
                while(self.capacity > 0 and x < len(students) ):
                        if students[j][0].successCount <3 :
                                # print "Students who got "+self.name
                                # print students[j][0].id
                                self.enrolledStudents.append(students[j][0])
                                students[j][0].addSuccessfulSubject(self)
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
                for stud in stud_list:
                        for choice in stud.choices:
                                if choice["subname"] == self.name:
                                        self.potentialStudents.append((stud,choice["subScore"],choice["priority"]))
               
                # sorts the list of students by score
                self.potentialStudents.sort(key=lambda tup: tup[1]) 
                # enrolls preferred students in the course

                # if self.name == 'Art And Design':
                #         for stud in self.potentialStudents:
                #                 print stud[0].id
                #                 print stud[1]
               
                selectedCount = 0
                while len(self.selectedStudents) < self.capacity and selectedCount < len(self.potentialStudents):
                        self.selectedStudents.append(self.potentialStudents[selectedCount][0].id)
                        self.selectedStudentsDict[str(self.potentialStudents[selectedCount][0].id)]  = selectedCount
                        selectedCount = selectedCount+1
                
                # self.enrollMany(self.potentialStudents)

        def confirmMatch(self,stud, needed = True):
                if stud.id in self.selectedStudents:
                        if needed:
                                self.enrolledStudents.append(stud)
                                stud.addSuccessfulSubject(self)
                                stud.successCount = stud.successCount+1
                        else:
                                self.selectedStudents.remove(stud.id)





gradeDict = {"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"U":7}
stud_list = []
subject_list =[]
subjectDict = {} #stores subject names and their position in the list



capeSubjects= Cape.query.all()
clist = []

subCounter = 0
for subject in capeSubjects:
        clist.append(subject.subjectName)
        # adds each cape subject from the database to a list
        subject_list.append(Subject(subject.subjectName, subject.capacity,subject.prerequisiteSubject))
        subjectDict[subject.subjectName] = subCounter
        subCounter = subCounter+1

students = Student.query.all()
for student in students:
        # makes a list of student objects to be used for matching 
	subjects = Studied.query.filter_by(studentID = student.studentID)
	choices = Application.query.filter_by(studentID = student.studentID)
        stud_list.append(Applicant(student.studentID, subjects,choices))


# TESTING
# for student in stud_list:
#         print student.choices

for sub in subject_list:
        # print sub.name
        sub.chooseStudents(stud_list) 

for student in stud_list:
        successful = False
        for choice in student.choices:
                if choice["priority"] <4:
                        subject_list[subjectDict[choice["subname"]]].confirmMatch(student)

        if  student.successCount ==3:
                successful = True
                student.successfulApplicant = successful

                #check to see if unneeded subject can be removed to make space for others
                needed = False
                student.choices[student.choicePriorityDict[4]].confirmMatch(stud, needed)




x = 0
for stud in stud_list:
        print "\n\n"
        print stud.id
        for sub in stud.successfulSubs:
                print sub.name
        
        if stud.successCount <3:
                print x
                x=x+1
                print stud.id
                print "\nApplied for\n"
                for sub in stud.choices:
                        print sub['subname']

                print "\nGOT\n"
                for sub in stud.successfulSubs:
                        print sub.name

for stud in stud_list:
        if stud.successCount <3:
                print stud.id


