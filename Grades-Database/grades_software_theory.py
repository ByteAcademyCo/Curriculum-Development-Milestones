
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="BAAdmin",
  passwd="password",
  database="BADatabase"
)

mycursor = mydb.cursor()


mycursor.execute("""CREATE TABLE grades_algorithms (
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
                     
mycursor.execute("""CREATE TABLE grades_networks (
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

mycursor.execute("""CREATE TABLE grades_databases (
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
                     
mycursor.execute("""CREATE TABLE grades_testing (
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

mycursor.execute("""CREATE TABLE grades_data_management (
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

