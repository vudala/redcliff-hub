from flask import Flask
app = Flask(__name__)

from api.db.connection import db_conn
db_conn.init_app(app)

from api.main import api_bp
app.register_blueprint(api_bp)

from web import pages_bp
app.register_blueprint(pages_bp)

if __name__ == '__main__':
    app.run()
    db_conn.close()