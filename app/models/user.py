from app.config.database import db

class User(db.Model):

    user_id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(100), nullable = False)
    user_email = db.Column(db.String(100), nullable = False, unique = True)
    is_deleted = db.Column(db.Integer, default = 0)

    def serialize(self):
        return {
            "userId" : self.user_id,
            "userName" : self.user_name,
            "userEmail" : self.user_email,
            "isDeleted" : self.is_deleted
        }