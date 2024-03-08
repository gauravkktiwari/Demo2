from flask import Flask
from .database import db
from flask_migrate import Migrate
from app.routes.user_route import user_bp

app = Flask(__name__)

app.register_blueprint(user_bp)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/demo3?charset=latin1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)
migrate  = Migrate(app, db)

#with app.app_context():
#    db.create_all()
        
@app.route("/")
def homePage():
    return "<h1>Welcome to Demo2</h2>"