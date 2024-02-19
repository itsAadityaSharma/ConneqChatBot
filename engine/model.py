from peewee import *
import db as db
ConnectionPool=db.db_Connect_thinModePool()
conn = ConnectionPool.acquire()
cursor = conn.cursor()

# Connect to the database
# db = SqliteDatabase('your_database.db')

class BaseModel(Model):
    class Meta:
        database = conn

# Define your model fields here
class EmployeeLeaves(BaseModel):
    legal_employer = CharField(max_length=100)
    person_number = CharField(max_length=100)
    person_name = CharField(max_length=100)
    department = CharField(max_length=100)
    grade = CharField(max_length=100)
    assignment_status = CharField(max_length=100)
    leave_type = CharField(max_length=100)
    leave_start_date = DateField()
    leave_end_date = DateField()
	


# Perform database operations
# For example, to insert a record:


ConnectionPool.release(conn)
