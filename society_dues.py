"""Simple apartment society maintenance dues ledger."""

import sqlite3


def create_connection():
    """Create an in-memory dues database and its table."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE dues (flat TEXT, month TEXT, amount INTEGER, paid INTEGER)"
    )
    return connection


def add_due(connection, flat, month, amount, history=None):
    """Record dues for a flat and append the entry to an optional history list."""
    if amount < 0:
        raise ValueError("Dues amount cannot be negative")
    connection.execute(
        "INSERT INTO dues (flat, month, amount, paid) VALUES (?, ?, ?, 0)",
        (flat, month, amount),
    )
    if history is None:
        history = []
    history.append((flat, month))
    return history


def collect(connection, flat, month):
    """Mark matching dues as paid and return the amount, or None when absent."""
    row = connection.execute(
        "SELECT amount FROM dues WHERE flat = ? AND month = ?", (flat, month)
    ).fetchone()
    if row is None:
        return None
    connection.execute(
        "UPDATE dues SET paid = 1 WHERE flat = ? AND month = ?", (flat, month)
    )
    return row[0]


def penalty(amount, multiplier=2):
    """Calculate a late fee using numeric values rather than an expression string."""
    if amount < 0 or multiplier < 0:
        raise ValueError("Amount and multiplier must be non-negative")
    return amount * multiplier


def pending(connection):
    """Return flat identifiers that have unpaid dues."""
    rows = connection.execute("SELECT flat FROM dues WHERE paid = 0").fetchall()
    return [row[0] for row in rows]


def main():
    """Run a small demonstration of the dues ledger."""
    connection = create_connection()
    add_due(connection, "A-101", "Oct", 2500)
    add_due(connection, "A-102", "Oct", 2500)
    print(collect(connection, "A-101", "Oct"))
    print(penalty(50, 2))
    print(pending(connection))
    connection.close()


if __name__ == "__main__":
    main()
