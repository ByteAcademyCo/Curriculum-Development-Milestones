
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="BAAdmin",
  passwd="password",
  database="BADatabase"
)

mycursor = mydb.cursor()


mycursor.execute("""CREATE TABLE grades_UML_diagrams (
                      stud_id   INTEGER PRIMARY KEY,
                      easy_e1   INTEGER,
                      easy_e2   INTEGER,
                      easy_e3   INTEGER,
                      easy_e4   INTEGER,
                      easy_e5   INTEGER,
                      easy_e6   INTEGER,
                      easy_e7   INTEGER,
                      easy_e8   INTEGER,
                      easy_e9   INTEGER,
                      med_e1    INTEGER,
                      med_e2    INTEGER,
                      med_e3    INTEGER,
                      med_e4    INTEGER,
                      med_e5    INTEGER,
                      med_e6    INTEGER,
                      hard_e1   INTEGER,
                      hard_e2   INTEGER,
                      hard_e3   INTEGER,
                      FOREIGN KEY   (stud_id)
                        REFERENCES  students (stud_id) 
                     );""")
                     
mycursor.execute("""CREATE TABLE grades_classes (
                      stud_id   INTEGER PRIMARY KEY,
                      easy_e1   INTEGER,
                      easy_e2   INTEGER,
                      easy_e3   INTEGER,
                      easy_e4   INTEGER,
                      easy_e5   INTEGER,
                      easy_e6   INTEGER,
                      easy_e7   INTEGER,
                      easy_e8   INTEGER,
                      easy_e9   INTEGER,
                      easy_e10  INTEGER,
                      easy_e11  INTEGER,
                      easy_e12  INTEGER,
                      easy_e13  INTEGER,
                      easy_e14  INTEGER,
                      easy_e15  INTEGER,
                      easy_e16  INTEGER,
                      easy_e17  INTEGER,
                      easy_e18  INTEGER,
                      med_e1    INTEGER,
                      med_e2    INTEGER,
                      med_e3    INTEGER,
                      med_e4    INTEGER,
                      med_e5    INTEGER,
                      med_e6    INTEGER,
                      med_e7    INTEGER,
                      med_e8    INTEGER,
                      med_e9    INTEGER,
                      med_e10   INTEGER,
                      med_e11   INTEGER,
                      med_e12   INTEGER,
                      hard_e1   INTEGER,
                      hard_e2   INTEGER,
                      hard_e3   INTEGER,
                      hard_e4   INTEGER,
                      hard_e5   INTEGER,
                      hard_e6   INTEGER,
                      FOREIGN KEY   (stud_id)
                        REFERENCES  students (stud_id) 
                     );""")

mycursor.execute("""CREATE TABLE grades_context_managers (
                      stud_id   INTEGER PRIMARY KEY,
                      easy_e1   INTEGER,
                      easy_e2   INTEGER,
                      easy_e3   INTEGER,
                      easy_e4   INTEGER,
                      easy_e5   INTEGER,
                      med_e1    INTEGER,
                      med_e2    INTEGER,
                      med_e3    INTEGER,
                      hard_e1   INTEGER,
                      hard_e2   INTEGER,
                      FOREIGN KEY   (stud_id)
                        REFERENCES  students (stud_id) 
                     );""")
                     
mycursor.execute("""CREATE TABLE grades_exceptions (
                      stud_id   INTEGER PRIMARY KEY,
                      easy_e1   INTEGER,
                      easy_e2   INTEGER,
                      easy_e3   INTEGER,
                      easy_e4   INTEGER,
                      med_e1    INTEGER,
                      med_e2    INTEGER,
                      med_e3    INTEGER,
                      hard_e1   INTEGER,
                      hard_e2   INTEGER,
                      FOREIGN KEY   (stud_id)
                        REFERENCES  students (stud_id) 
                     );""")                     

mycursor.execute("""CREATE TABLE grades_modules (
                      stud_id   INTEGER PRIMARY KEY,
                      easy_e1   INTEGER,
                      easy_e2   INTEGER,
                      easy_e3   INTEGER,
                      easy_e4   INTEGER,
                      easy_e5   INTEGER,
                      easy_e6   INTEGER,
                      easy_e7   INTEGER,
                      easy_e8   INTEGER,
                      easy_e9   INTEGER,
                      med_e1    INTEGER,
                      med_e2    INTEGER,
                      med_e3    INTEGER,
                      med_e4    INTEGER,
                      med_e5    INTEGER,
                      med_e6    INTEGER,
                      hard_e1   INTEGER,
                      hard_e2   INTEGER,
                      hard_e3   INTEGER,
                      FOREIGN KEY   (stud_id)
                        REFERENCES  students (stud_id) 
                     );""")     
