 
CREATE TABLE sheets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE cells (
    id SERIAL PRIMARY KEY,
    sheet_id INTEGER REFERENCES sheets(id),
    row INTEGER,
    col VARCHAR(5),
    value TEXT
);