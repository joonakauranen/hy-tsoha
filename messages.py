from db import db

def add_topic(content, user):
    if len(content) == 0:
        return False
    sql = "INSERT INTO topics (topic, created_by, created_at) VALUES (:topic, :created_by, NOW())"
    db.session.execute(sql, {"topic":content, "created_by":user})
    db.session.commit()
    return True

def new_message(content, user, topic_id):
    if len(content) == 0:
        return False
    sql = "INSERT INTO messages (content, created_by, created_at, topic_id) VALUES (:content, :created_by, NOW(), :topic_id)"
    db.session.execute(sql, {"content":content, "created_by":user, "topic_id":topic_id})
    db.session.commit()
    return True

def get_messages(top_id):
    sql = "SELECT id, content, created_at, topic_id FROM messages WHERE topic_id=:topic_id ORDER BY created_at DESC"
    result = db.session.execute(sql, {"topic_id":top_id})
    topics = result.fetchall()
    return topics

def search_messages(keyword):
    sql = "SELECT id, content, created_at, topic_id FROM messages WHERE content LIKE :content ORDER BY created_at DESC"
    result = db.session.execute(sql, {"content":keyword})
    messages = result.fetchall()
    return messages