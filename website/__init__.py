from flask import Flask, render_template, url_for
from .database import create_table_contato, create_database

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mulinhas'

    from .routes import routes
    app.register_blueprint(routes, url_prefix='/')

    try: create_database()
    except: pass
    try: create_table_contato()
    except: pass

    return app

