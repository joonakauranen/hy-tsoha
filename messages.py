from db import db

def add_topic(content, user):
    if len(content) == 0:
        return False
    sql = "INSERT INTO topics (topic, created_by, created_at) VALUES (:topic, :created_by, NOW())"
    db.session.execute(sql, {"topic":content, "created_by":user})
    db.session.commit()
    return True

def new_message(content, user):
    if not content or user:
        return False
    sql = "INSERT INTO messages (content, created_by, created_at) VALUES (:content, :user_id, NOW())"
    db.session.execute(sql, {"content":content, "created_by":user})
    db.session.commit()
    return True