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
    topics = get_messages(topic_id)
    return topics

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

def new_favorite(content, juser, topic_id):
    sql = "INSERT INTO favorites (content, juser, topic_id) VALUES (:content, :juser, :topic_id)"
    db.session.execute(sql, {"content":content, "juser":juser, "topic_id":topic_id})
    db.session.commit()

def new_point(created_by):
    sql = "SELECT juser, points FROM points WHERE juser=:juser"
    result = db.session.execute(sql, {"juser":created_by})
    points = result.fetchall()
    if len(points) == 0:
        new_points = 1
        sql = "INSERT INTO points (juser, points) VALUES (:juser, :points)"
        db.session.execute(sql, {"juser":created_by, "points":new_points})
        db.session.commit()

        #return True
    else:
        current_points = points[0][1]
        new_points = current_points + 1

        sql = "UPDATE points SET points=:points WHERE juser=:juser"
        db.session.execute(sql, {"juser":created_by, "points":new_points})
        db.session.commit()

        #return True

def get_favorites(juser):
    sql = "SELECT id, content, juser, topic_id FROM favorites WHERE juser=:juser"
    result = db.session.execute(sql, {"juser":juser})
    favorites = result.fetchall()
    return favorites

def get_points(juser):
    sql = "SELECT points FROM points WHERE juser=:juser"
    result = db.session.execute(sql, {"juser":juser})
    points = result.fetchall()
    return points

def get_most_messages():
    sql = "SELECT topic_id, count(*) FROM messages GROUP BY topic_id ORDER BY count(*) DESC LIMIT 1"
    result = db.session.execute(sql)
    message = result.fetchall()
    return message