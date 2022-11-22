CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    topic TEXT,
    created_at TIMESTAMP,
    user_id INTEGER
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT,
    role TEXT
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    created_at TIMESTAMP,
    created_by TEXT
);

