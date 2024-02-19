import db as db
ConnectionPool=db.db_Connect_thinModePool()
from model import EmployeeLeaves



# conn = ConnectionPool.acquire()

# cursor = conn.cursor()
# cursor.execute(sql)
# result = cursor.fetchall()
# cursor.close()

# print("successful sql generation")

# ConnectionPool.release(conn)

EmployeeLeaves1 = EmployeeLeaves.select().where(EmployeeLeaves.person_number == '2033756').first()
# query = "SELECT * FROM employeeleaves"
# conn = ConnectionPool.acquire()
# cursor = conn.cursor()
# cursor.execute(query)
# result = cursor.fetchall()
# cursor.close()

print(EmployeeLeaves1)