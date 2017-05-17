from app import db
import names,random

db.drop_all()
db.create_all()


conn  = db.engine

conn.execute("insert into csec values('Mathematics');")
conn.execute("insert into csec values('Additional Mathematics');")
conn.execute("insert into csec values('Biology');")
conn.execute("insert into csec values('Chemistry');")
conn.execute("insert into csec values('Physics');")
conn.execute("insert into csec values('Technical Drawing');")
conn.execute("insert into csec values('French');")
conn.execute("insert into csec values('Spanish');")
conn.execute("insert into csec values('Art');")
conn.execute("insert into csec values('Agricultural Science');")
conn.execute("insert into csec values('Building Technology');")
conn.execute("insert into csec values('Caribbean History');")
conn.execute("insert into csec values('Clothing and Textiles');")
conn.execute("insert into csec values('English Language');")
conn.execute("insert into csec values('English Literature');")
conn.execute("insert into csec values('Food and Nutrition');")
conn.execute("insert into csec values('Geography');")
conn.execute("insert into csec values('Home Economics Management');")
conn.execute("insert into csec values('Human and Social Biology');")
conn.execute("insert into csec values('Music');")
conn.execute("insert into csec values('Religious Education');")
conn.execute("insert into csec values('Theatre Arts');")
conn.execute("insert into csec values('Visual Arts');")
conn.execute("insert into csec values('Principles of Accounts');")
conn.execute("insert into csec values('Principles of Business');")
conn.execute("insert into csec values('Economics');")
conn.execute("insert into csec values('Information Technology');")
conn.execute("insert into csec values('None');")


conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Accounting',10,'Principles of Accounts');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Agricultural Science',10,'Agricultural Science');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Applied Mathematics',10,'Mathematics');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Art And Design',10,'Visual Arts');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Biology',10,'Biology');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Building And Mechanical Engineering Drawing',10,'Technical Drawing');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Caribbean Studies',10,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Chemistry',10,'Chemistry');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Communication Studies',10,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Computer Science',10,'Information Technology');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Digital Media',10,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Electrical And Electronic Engineering Technology',10,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Economics',10,'Economics');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Entrepreneurship',10,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Environmental Science',10,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Financial Services Studies',10,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Food and Nutrition',10,'Food and Nutrition');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('French',10,'French');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Geography',10,'Geography');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Green Engineering',10,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('History',10,'Caribbean History');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Information Technology',10,'Information Technology');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Integrated Mathematics',10,'Mathematics');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Law',10,'Caribbean History');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Literatures In English',10,'English Literature');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Logistics And Supply Chain Operations',10,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Management Of Business',10,'Principles of Business');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Performing Arts',10,'Theatre Arts');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Physics',10,'Physics');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Physical Education And Sport',10,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Pure Mathematics',10,'Mathematics');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Sociology',10,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Spanish',10,'Spanish');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Tourism',10,'None');")


#config values
conn.execute("insert into config (\"mandatorySubject\",\"classSize\",\"matchPerformed\") values ('Communication Studies',30,False);")
# dummy data for students

# subs = [('Principles of Accounts','Accounting'), ('Agricultural Science','Agricultural Science'), ('Mathematics','Applied Mathematics'), ('Visual Arts','Art And Design'), ('Biology','Biology'), ('Technical Drawing','Building And Mechanical Engineering Drawing'), ('None','Caribbean Studies'), ('Chemistry','Chemistry'), ('None','Communication Studies'), ('Information Technology','Computer Science'), ('None','Digital Media'), ('None','Electrical And Electronic Engineering Technology'), ('Economics','Economics'), ('None','Entrepreneurship'), ('None','Environmental Science'), ('None','Financial Services Studies'), ('Food and Nutrition','Food and Nutrition'), ('French','French'), ('Geography','Geography'), ('None','Green Engineering'), ('Caribbean History','History'), ('Information Technology','Information Technology'), ('Mathematics','Integrated Mathematics'), ('Caribbean History','Law'),('English Literature', 'Literatures In English'), ('None','Logistics And Supply Chain Operations'), ('Principles of Business','Management Of Business'), ('Theatre Arts','Performing Arts'), ('Physics','Physics'), ('None','Physical Education And Sport'), ('Mathematics','Pure Mathematics'), ('None','Sociology'), ('Spanish','Spanish'), ('None','Tourism')]
subs = [('Principles of Accounts','Accounting'), ('Agricultural Science','Agricultural Science'), ('Mathematics','Applied Mathematics'), ('Visual Arts','Art And Design'), ('Biology','Biology'), ('Technical Drawing','Building And Mechanical Engineering Drawing'), ('None','Caribbean Studies'), ('Chemistry','Chemistry'), ('Information Technology','Computer Science'), ('None','Digital Media'), ('None','Electrical And Electronic Engineering Technology'), ('Economics','Economics'), ('None','Entrepreneurship'), ('None','Environmental Science'), ('None','Financial Services Studies'), ('Food and Nutrition','Food and Nutrition'), ('French','French'), ('Geography','Geography'), ('None','Green Engineering'), ('Caribbean History','History'), ('Information Technology','Information Technology'), ('Mathematics','Integrated Mathematics'), ('Caribbean History','Law'),('English Literature', 'Literatures In English'), ('None','Logistics And Supply Chain Operations'), ('Principles of Business','Management Of Business'), ('Theatre Arts','Performing Arts'), ('Physics','Physics'), ('None','Physical Education And Sport'), ('Mathematics','Pure Mathematics'), ('None','Sociology'), ('Spanish','Spanish'), ('None','Tourism')]

grades = ["I","II","III","IV","V","VI","U"]
# grades = ["I","II"]


for i in range(0,100):
	pickedCape= []
	pickedCsec =[]
	idnum=62000000+i
	fname = str(names.get_first_name())
	lname = str(names.get_last_name())
	password = "password"
	conn.execute("insert into student(\"studentID\", \"first_name\",\"last_name\",\"password\")values("+str(idnum)+",'"+fname+"','"+lname+"','"+password+"');")
	for j in range(0,4):
		sub = random.choice(subs)
		if sub[1] in pickedCape:
			while (sub[1] in pickedCape):
				sub = random.choice(subs)

		pickedCape.append(sub[1])
		if sub[0] == "None":
			pass
		elif (sub[0] not in pickedCsec):
			pickedCsec.append(sub[0])

	for j in range(0,4):
		sub = random.choice(subs)
		if (sub[0] in pickedCsec or sub[0] == 'None'):
			while (sub[0] in pickedCsec or sub[0] == 'None'):
				sub = random.choice(subs)

		pickedCsec.append(sub[0])

	# print "ID"
	# print idnum
	# print "Csec"
	# print pickedCsec
	# print "Cape"
	# print pickedCape

	for sub in pickedCsec:
		grade = random.choice(grades)
		conn.execute("insert into studied (\"studentID\",\"grade\",\"subjectName\") values('"+str(idnum)+"','"+grade+"','"+sub+"');")
	
	priority = 1
	for sub in pickedCape:
		conn.execute("insert into application (\"studentID\",\"subjectName\",\"subjectPriority\") values('"+str(idnum)+"','"+sub+"','"+str(priority)+"');")
		priority+=1



