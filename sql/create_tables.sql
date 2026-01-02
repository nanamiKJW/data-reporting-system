DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY,
    timestamp TEXT NOT NULL,
    system_type TEXT NOT NULL,
    amount REAL NOT NULL,
    status TEXT NOT NULL
);
