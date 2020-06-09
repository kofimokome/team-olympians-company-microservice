from flask import Flask

from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Team Olympians Task 2"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


if __name__ == '__main__':
    app.run(host ='0.0.0.0')