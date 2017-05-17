from app import db
from app.models import *
import json

CAPACITY = 30
MANDATORY = ""


class Applicant():
        def __init__(self, student_id, subjects, choices):
                self.id = student_id
                self.successfulApplicant = False
                self.choices =[]
                self.subjects =[]
                self.successCount = 0
                self.successfulSubs  = []
                self.choicePriorityDict = {} #dictionary of subject priorities and names for easy finding

                for subject in subjects:
                	s = {}
                	s["subname"]= subject.subjectName
                	s["grade"] = subject.grade
                	self.subjects.append(s)

                
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
                        self.choicePriorityDict[choice.subjectPriority] = choice.subjectName
        

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
                self.successfulSubs.append(subject.name)
                self.successCount+=1
                if self.successCount ==3:
                        self.successfulApplicant = True
                

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


        # def enrollMany(self, students): #adds students from already sorted stack until capacity runs out.
        #         j = 0
        #         x = 0
        #         while(self.capacity > 0 and x < len(students) ):
        #                 if students[j][0].successCount <3 :
        #                         # print "Students who got "+self.name
        #                         # print students[j][0].id
        #                         self.enrolledStudents.append(students[j][0])
        #                         students[j][0].addSuccessfulSubject(self)
        #                         self.capacity -= 1
        #                 j += 1
        #                 x += 1

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

                # if self.name == 'Agricultural Science':
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
                # if selectedStudents == None:
                #         selectedStudents = self.selectedStudents

                if stud.id in self.selectedStudents:

                        if needed:
                                if self.capacity>0:
                                        self.enrolledStudents.append(stud.id)
                                        stud.addSuccessfulSubject(self)
                                        self.capacity = self.capacity-1
                                        # if self.name == 'Agricultural Science':
                                        #         print self.name +" capacity now "+str(self.capacity)
                                        #         print "enrolled "+stud.id
                                else:
                                        print "no more space in "+self.name
                        else:
                                # if self.name == 'Agricultural Science':
                                #         print "\nSpace opened in "+ self.name
                                #         print stud.id +" doesnt need it"
                                if len(self.potentialStudents) > len(self.selectedStudents):
                                        # if self.name == 'Agricultural Science':
                                        #         print self.potentialStudents[len(self.selectedStudents)][0].id
                                        #         print "given a second chance"
                                        #add the student next in line to a list to be used in the second round of selection
                                        self.selectedStudents.remove(stud.id)
                                        self.selectedStudents.append(self.potentialStudents[len(self.selectedStudents)+1][0].id)
                                        self.potentialStudents.remove(self.potentialStudents[len(self.selectedStudents)])
                                        # if self.name == 'Agricultural Science':
                                        #         print self.selectedStudents

                        # if stud.id == '62000055':
                        #         print stud.id
                        #         print "current subject: "
                        #         print self.name
                        #         print "achieved subjects: "
                        #         print stud.successCount
                        #         print "successful applicant: "
                        #         print stud.successfulApplicant
                        #         print "successful subjects: "
                        #         print stud.successfulSubs
                        #         print "needed:"
                        #         print needed
                        #         print "---------------------------------------------------"
                        





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
        subject_list.append(Subject(subject.subjectName, CAPACITY,subject.prerequisiteSubject))
        subjectDict[subject.subjectName] = subCounter
        subCounter = subCounter+1

students = Student.query.all()
for student in students:
        # makes a list of student objects to be used for matching 
	subjects = Studied.query.filter_by(studentID = student.studentID)
	choices = Application.query.filter_by(studentID = student.studentID)
        stud_list.append(Applicant(student.studentID, subjects,choices))


config = Config.query.filter_by(id = 1)
try:
        conf = config[0]
except:
        print "Didnt set config value"
else:
        CAPACITY = conf.classSize
        MANDATORY = conf.mandatorySubject

# TESTING
# for student in stud_list:
#         print student.choices



# MATCHING
def match(matchingRound = 1):
        if matchingRound == 1: # if its the first round allow the subjects to select their preferred students
                for sub in subject_list:
                        # print sub.name
                        sub.chooseStudents(stud_list) 

        for student in stud_list:
                successful = student.successfulApplicant
                if(not successful):
                        for choice in student.choices:
                                if choice["priority"] < 4 and choice['subname'] not in student.successfulSubs:
                                        subject_list[subjectDict[choice["subname"]]].confirmMatch(student)

                        if student.successCount<3 and matchingRound!=1:
                                print "worked once"
                                print student.id
                                subject_list[subjectDict[student.choicePriorityDict[4]]].confirmMatch(student)
                        elif  student.successCount ==3:
                                successful = True
                                student.successfulApplicant = successful

                                #check to see if unneeded subject can be removed to make space for others
                                needed = False
                                subject_list[subjectDict[student.choicePriorityDict[4]]].confirmMatch(student, needed)






def matchStudents():
match()
print "second round"
match(2)
# VIEWING RESULTS


x = 0
for stud in stud_list:
        # print "\n\n"
        # print stud.id
        # for sub in stud.successfulSubs:
        #         print sub.name
        
        if stud.successfulApplicant == False:
                print "\n\n"
                print x
                x=x+1
                print stud.id
                print "\nApplied for\n"
                for sub in stud.choices:
                        print sub['subname']

                print "\nGOT\n"
                for sub in stud.successfulSubs:
                        print sub

        for sub in stud.successfulSubs:
                success = SuccessfulApplication(studentID = stud.id,subjectName= sub)
                db.session.add(success)
        
        mandatory = SuccessfulApplication(studentID = stud.id,subjectName= MANDATORY)
        db.session.add(mandatory)
        db.session.commit()



# for stud in stud_list:
#         if stud.successCount <3:
#                 print stud.id


# for sub in subject_list:
#         print "\n"
#         print sub.name
#         print sub.capacity
#         print sub.enrolledStudents


