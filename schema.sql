CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    topic TEXT,
    created_at TIMESTAMP
);

CREATE TABLE choices (
    id SERIAL PRIMARY KEY,
    topic_id INTEGER REFERENCES topics,
    choice TEXT
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    choice_id INTEGER REFERENCES choices,
    sent_at TIMESTAMP
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT,
    role TEXT
);