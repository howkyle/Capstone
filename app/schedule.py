from app import db
from app.models import *
import match
import json

# class Schedule(db.Model):
#     time = db.Column(db.String, primary_key = True)
#     mon = db.Column(db.String(80), db.ForeignKey('cape.subjectName'))
#     tue = db.Column(db.String(80), db.ForeignKey('cape.subjectName'))
#     wed = db.Column(db.String(80), db.ForeignKey('cape.subjectName'))
#     thu = db.Column(db.String(80), db.ForeignKey('cape.subjectName'))
#     fri = db.Column(db.String(80), db.ForeignKey('cape.subjectName'))


# All Available time slots
times = ['08:00 - Mon', '09:00 - Mon', '10:00 - Mon', '11:00 - Mon', '13:00 - Mon', '14:00 - Mon', '15:00 - Mon', 
        '08:00 - Tue', '09:00 - Tue', '10:00 - Tue', '11:00 - Tue', '13:00 - Tue', '14:00 - Tue', '15:00 - Tue', 
        '08:00 - Wed', '09:00 - Wed', '10:00 - Wed', '11:00 - Wed', '13:00 - Wed', '14:00 - Wed', '15:00 - Wed', 
        '08:00 - Thu', '09:00 - Thu', '10:00 - Thu', '11:00 - Thu', '13:00 - Thu', '14:00 - Thu', '15:00 - Thu', 
        '08:00 - Fri', '09:00 - Fri', '10:00 - Fri', '11:00 - Fri', '13:00 - Fri', '14:00 - Fri', '15:00 - Fri']

# Number of sessions of class per week        
NUM_SESSIONS = 4

# List of all subjects
subjects = []

# Records subjects with the same student(s) enrolled
clashes = {}
def initialize(subs):
    global clashes
    global subjects
    subjects = subs
    for sub in subjects:
        clashes[sub.name] = []

# Stores schedule
times_of_subjects = {'Break' : ['12:00 - Mon', '12:00 - Tue', '12:00 - Wed', '12:00 - Thu', '12:00 - Fri']}
   
class Schedule():
    def __init__(self):
        # self.time = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00']
        # self.mon = {}               # Stores all classes and times for Monday
        # self.tue = {}               # Stores all classes and times for Tuesday
        # self.wed = {}               # Stores all classes and times for Wednesday
        # self.thu = {}               # Stores all classes and times for Thursday
        # self.fri = {}               # Stores all classes and times for Friday
        self.week = {}              # Stores all classes and times for the week
        
    def find_clashes(self):               # Populates dictionary storing all subjects that a given class clashes with
        for sub1 in subjects:
            for sub2 in subjects:
                for x in range(0, len(sub1.enrolledStudents)):
                    if sub1.enrolledStudents[x] in sub2.enrolledStudents and not sub2.name in clashes[sub1.name]:
                        clashes[sub1.name].append(sub2.name)
    
    def promising(self, sub, time):               # Checks if proposed time is clashing with another class done by students
        for clash in clashes.get(sub):
            times_of_clashes = times_of_subjects.get(clash)
            if times_of_clashes is None:
                times_of_clashes = []
            if time in times_of_clashes:
                return False
        return True
    
    def get_time_for_subject(self, sub):               # Assigns a class numerous time slots throughout the week
        def helper(sub, all_times):
            def sameDay(time, all_times):
                day1 = time[8:]
                for t in all_times:
                    if day1 in t:
                        return True
                return False
                        
            for time in times:
                if self.promising(sub, time) and not time in all_times and not sameDay(time, all_times):
                    return time
                    
        all_times = []
        while (len(all_times) < NUM_SESSIONS):
            all_times.append(helper(sub, all_times))
        return all_times

    def matchtime(self):
    
        self.find_clashes()
        
        for key, value in sorted(clashes.items(), key=lambda (k,v): (v,k)):
            print "%s: %s" % (key, value)
        
        for sub in subjects:
            times_of_subjects[sub.name] = self.get_time_for_subject(sub.name)       # Checks times and stores assigned times in dictionary
            
        for key, value in sorted(times_of_subjects.items(), key=lambda (k,v): (v,k)):
            print "%s: %s" % (key, value)
            
        self.week = times_of_subjects
        return self.week
        
        
# def main():
#     Schedule().matchtime()
    
# main()