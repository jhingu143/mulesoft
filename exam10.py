#import the library sqlite3 bcz i use the sqlite3 function
import sqlite3

#connect the database
#create variable 'con' store the data
con=sqlite3.connect("exam.db")
print ("database connect sucessfully")

#create the table 
con.execute("create table if not exists Movies(Name text, Actor text, Actress text, Director text, Year_of_release text)")
print("table created...")

#insert the value in Movies table 
con.execute("insert into Movies(Name, Actor, Actress, Director, Year_of_release) values ('super30','Hrithik Roshan','Mrunal Thakur','Anand Kumar','2017')") 
con.execute("insert into Movies(Name, Actor, Actress, Director, Year_of_release) values ('pushpa','Allu Arjun','Rashmika Mandanna','Sukumar','2021')") 
con.execute("insert into Movies(Name, Actor, Actress, Director, Year_of_release) values ('Dilwale Dulhania Le Jayenge','Shah Rukh Khan ','Kajol ','Aditya Chopra','1995')") 

con.commit()
print("insert data successfully..")

#fetch the data using select query
data=con.execute("select * from Movies")
records = data.fetchall()
print("Fetching each row using column name")
for row in records:
    print("Name" , row[0])
    print("Actor" , row[1])
    print("Actress", row[2])
    print("Director"  ,row[3])
    print("Year_of_release",row[4])
  

print('fetch the all data successfully..')