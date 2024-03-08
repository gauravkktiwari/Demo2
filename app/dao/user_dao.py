from app.config.database import db
from app.models.user import User

def getUsers():
    return User.query.all()

def createUser(userName, userEmail):
    try:
        
        user = User(user_name = userName, user_email = userEmail)

        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        return user
    except Exception as e:
        db.session.rollback()
        print("Error: ",e)
    finally:
        if db.session.is_active:
            db.session.close()
    return None