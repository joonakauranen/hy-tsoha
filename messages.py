from db import db

def send(content, user):
    user_id = user
    if user_id == 0:
        return False
    sql = "INSERT INTO topics (topic, user_id, created_at) VALUES (:topic, :user_id, NOW())"
    db.session.execute(sql, {"topic":content, "user_id":user_id})
    db.session.commit()
    return True