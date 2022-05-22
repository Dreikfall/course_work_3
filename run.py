from flask import Flask, render_template
from app.posts.views import posts_blueprint
from app.api.views import api_blueprint
from app.logger import create_logger

app = Flask(__name__)

create_logger()

app.config['JSON_AS_ASCII'] = False

app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)


if __name__ == "__main__":
    app.run(debug=True)
