try:
    import MySQLdb
except:
    print("hi")
db=MySQLdb.connect("localhost","root","taran123","taran")
cursor=db.cursor()
cursor.execute("create table taran1(name varchar(50),age int,salary int")

