from app import db
import names

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


conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Accounting',30,'Principles of Accounts');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Agricultural Science',30,'Agricultural Science');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Applied Mathematics',30,'Mathematics');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Art And Design',30,'Visual Arts');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Biology',30,'Biology');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Building And Mechanical Engineering Drawing',30,'Technical Drawing');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Caribbean Studies',30,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Chemistry',30,'Chemistry');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Communication Studies',30,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Computer Science',30,'Information Technology');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Digital Media',30,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Electrical And Electronic Engineering Technology',30,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Economics',30,'Economics');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Entrepreneurship',30,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Environmental Science',30,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Financial Services Studies',30,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Food And Nutrition',30,'Food and Nutrition');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('French',30,'French');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Geography',30,'Geography');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Green Engineering',30,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('History',30,'Caribbean History');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Information Technology',30,'Information Technology');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Integrated Mathematics',30,'Mathematics');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Law',30,'Caribbean History');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Literatures In English',30,'English Literature');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Logistics And Supply Chain Operations',30,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Management Of Business',30,'Principles of Business');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Performing Arts',30,'Theatre Arts');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Physics',30,'Physics');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Physical Education And Sport',30,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Pure Mathematics',30,'Mathematics');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Sociology',30,'None');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Spanish',30,'Spanish');")
conn.execute("insert into cape (\"subjectName\",\"capacity\",\"prerequisiteSubject\") values ('Tourism',30,'None');")

# dummy data for students

subs = [('Principles of Accounts','Accounting'), ('Agricultural Science','Agricultural Science'), ('Mathematics','Applied Mathematics'), ('Visual Arts','Art And Design'), ('Biology','Biology'), ('Technical Drawing','Building And Mechanical Engineering Drawing'), ('None','Caribbean Studies'), ('Chemistry','Chemistry'), ('None','Communication Studies'), ('Information Technology','Computer Science'), ('None','Digital Media'), ('None','Electrical And Electronic Engineering Technology'), ('Economics','Economics'), ('None','Entrepreneurship'), ('None','Environmental Science'), ('None','Financial Services Studies'), ('None','Food And Nutrition'), ('French','French'), ('Geography','Geography'), ('None','Green Engineering'), ('Caribbean History','History'), ('Information Technology','Information Technology'), ('Mathematics','Integrated Mathematics'), ('Caribbean History','Law', 'Literatures In English'), ('Logistics And Supply Chain Operations'), ('Principles of Business','Management Of Business'), ('Theatre Arts','Performing Arts'), ('Physics','Physics'), ('None','Physical Education And Sport'), ('Mathematics','Pure Mathematics'), ('None','Sociology'), ('Spanish','Spanish'), ('None','Tourism')]
cape = 


for i in range(0,50):
	idnum=62000000
	fname = str(names.get_first_name())
	lname = str(names.get_first_name())
	password = "password"
	conn.execute("insert into student(\"studentID\", \"first_name\",\"last_name\",\"password\")values("+str(idnum+i)+",'"+fname+"','"+lname+"','"+password+"');")



