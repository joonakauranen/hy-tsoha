from db import db

def create_topic(content, user):
    if not content or user:
        return False
    sql = "INSERT INTO topics (topic, user_id, created_at) VALUES (:topic, :user_id, NOW())"
    db.session.execute(sql, {"topic":content, "user_id":user})
    db.session.commit()
    return True