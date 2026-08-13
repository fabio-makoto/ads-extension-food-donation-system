CREATE TABLE donations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    food TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    date TEXT NOT NULL
);
