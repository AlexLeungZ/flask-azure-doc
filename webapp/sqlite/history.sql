PRAGMA foreign_keys = ON;

CREATE TABLE
    IF NOT EXISTS INVOICE (
        timestamp FLOAT NOT NULL,
        fileIndex TEXT NOT NULL,
        filename TEXT NOT NULL,
        filehash TEXT NOT NULL,
        fileLength INT,
        invoiceId TEXT,
        invoiceDate TEXT,
        dueDate TEXT,
        customerId TEXT,
        customerName TEXT,
        invoiceTotal TEXT,
        amountDue TEXT,
        json TEXT,
        UNIQUE (fileIndex)
    );