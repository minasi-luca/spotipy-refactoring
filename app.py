from flask import Flask
from blueprints.auth import auth_bp
from blueprints.home import home_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'tua_chiave_segreta'

    # Registra i Blueprint
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(home_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
