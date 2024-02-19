from sanic import Sanic
import db as db
import cohere
co = cohere.Client('1o6DGrPw4E2APoUDerAxUOofl3K7FccJDHaOteVC')
from sanic_cors import CORS
from rasa.core.run import serve_application
ConnectionPool=db.db_Connect_thinModePool()
from model import EmployeeLeaves
app = Sanic(__name__)
CORS(app)
rasa_app = serve_application()
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
    