from sanic import Sanic
from sanic_cors import CORS
from rasa.core.run import serve_application
app = Sanic(__name__)
CORS(app)  # This enables CORS for all origins
rasa_app = serve_application()
app.mount("/", rasa_app)
if __name__ == "__main__":
    port = 5000
    print("server is listening on"  + port)
    app.run(host="0.0.0.0", port=5000)