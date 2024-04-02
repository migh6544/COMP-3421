# first need to make sure connector is installed:
#  python3 -m pip install mysql-connector-python

import mysql.connector

# note:  look at at end of this file - mydb.commit() and mydb.close() -> do not forget
# MUST commit the changes!!!!  (if you did any inserts, deletes, updates, load data.... )

print ("Hello - starting createAndLoadSailorDB.py")

mydb = mysql.connector.connect(
  user='testuser',    # could be root, or a user you created, I created 'testuser'
  passwd='testuser',  # the password for that use
  database='test9',   # the database to connect to
  host='127.0.0.1',   # localhost
  allow_local_infile='1'  # needed so can load local files
)



print(mydb)
myc = mydb.cursor()   # myc name short for "my cursor"

# We need to reset the variable that allows loading of local files 
myc.execute('set global local_infile = 1') 

myc.execute ("show databases")  # this returns a list in myc that you can iterate over
for x in myc:
	print(x) 

myc.execute ("use test9") 

# print out which tables are in test9
myc.execute ("show tables") 
for x in myc:
	print(x) 




myc.execute("drop table if exists Reserve ;")
myc.execute("drop table if exists Sailors ;")
myc.execute("drop table if exists Boats ;")

myc.execute("""    # multi-line python comment is three double quotes
create table Sailors ( 
  sid int, 
  name varchar(20) NOT NULL, 
  age int, 
  rating float NOT NULL, 
  Primary Key (sid) ) ; 
""")


myc.execute("""
create table Boats (
  bid int,
  name varchar(20),
  ratingNeeded int,
  bcolor varchar(20),
  PRIMARY KEY (bid) ) ;
""")

myc.execute("""
create table Reserve (
  bid int,
  sid int, 
  rdate date,
  PRIMARY KEY (bid,sid,rdate),
  Foreign Key (bid) references Boats(bid),
  Foreign Key (sid) references Sailors(sid) ) ;
""")


print("Before loading Sailors:  select * from sailors where sid < 10")
myc.execute ("select * from sailors where sid < 10") ;
for x in myc:
	print(x) 


myc.execute("""
  load data local infile '/Users/leut/data_sailors' into table sailors 
  fields terminated by ',' 
  lines terminated by '\n' ; 
""")

print(myc.rowcount, " tuples were inserted")

print("After loading Sailors:  select * from sailors where sid < 10")
myc.execute ("select * from sailors where sid < 10") ;
for x in myc:
	print(x) 


myc.execute("""
load data local infile '/Users/leut/data_boats' into table boats
  fields terminated by ','
  lines terminated by '\n' ;
""")

myc.execute("""
load data local infile '/Users/leut/data_reserve' into table reserve
  fields terminated by ','
  lines terminated by '\n' ;
""")


# MUST commit the changes!!!!  (if you did any inserts, deletes, updates, load data.... )
mydb.commit()
mydb.close() 

