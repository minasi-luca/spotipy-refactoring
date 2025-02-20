from flask import Flask
from blueprints.auth import auth_bp
from blueprints.home import home_bp

app = Flask(__name__)
app.secret_key = 'chiave per session'

app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)

app.run(debug=True)