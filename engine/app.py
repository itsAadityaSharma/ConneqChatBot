from sanic import Sanic
import db as db
import authJWTs as authJWTs
import cohere
co = cohere.Client('1o6DGrPw4E2APoUDerAxUOofl3K7FccJDHaOteVC')
from sanic_cors import CORS
from rasa.core.run import serve_application
ConnectionPool=db.db_Connect_thinModePool()
from model import EmployeeLeaves
app = Sanic(__name__)
CORS(app)
secret_key = "mysecretkey"
payload = {
    "EMP_ID": 1,
    "FIRST_NAME": "John",
    "LAST_NAME": "Doe",
    "DEPARTMENT": "IT",
    "REPORTING_MANAGER": "Manager1",
    "PROJECT_MANAGER": "ProjectManager1",
    "EMAIL": "john.doe@email.com",
    "DESIGNATION": "Developer",
    "CREATED_BY": "TEST_SCHEMA",
    "CREATED_ON": "27-12-23 7:40:53.058012000 PM",
    "UPDATED_BY": "TEST_SCHEMA",
    "UPDATED_ON": "27-12-23 7:40:53.058012000 PM"
}
token = authJWTs.generate_jwt(payload, secret_key)
print("JWT token:", token)
rasa_app = serve_application(auth_token=token)
app.mount("/", rasa_app)
message = 'Hello World'
response = co.chat(
	message,
	model="command",
	temperature=0.9
)
print("respones",response)
if __name__ == "__main__":
    port = 5000
    print("server is listening on"  + port)
    app.run(host="0.0.0.0", port=5000)

# employee = EmployeeLeaves.select().where(EmployeeLeaves.person_name == '2033756').first()
    