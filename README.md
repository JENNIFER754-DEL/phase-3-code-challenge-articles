# Articles Code Challenge - Without SQLAlchemy

## Overview

This project models the relationships between **Authors**, **Articles**, and **Magazines** using Python and raw SQL without relying on ORMs like SQLAlchemy. It persists data in an SQLite database (`articles.db`) and supports complex querying and transaction management.

---

## Project Structure

.
├── README.md
├── articles.db # SQLite database file
├── env/ # Python virtual environment
├── lib/ # Core application code
│ ├── db/ # Database connection and schema
│ │ ├── connection.py # DB connection setup
│ │ ├── schema.py # Python wrapper or helpers for schema
│ │ └── schema.sql # SQL schema definition file
│ ├── models/ # Model classes for Author, Article, Magazine
│ │ ├── article.py
│ │ ├── author.py
│ │ └── magazine.py
│ ├── queries/ # Advanced or complex SQL queries
│ │ └── advanced_queries.py
│ ├── transaction.py # Transaction management utilities
│ └── transaction_handler.py # Possibly context manager for transactions
├── scripts/ # Utility scripts
│ └── setup_db.py # Script to create DB and seed initial data
└── tests/ # Test suite with pytest tests
├── test_advanced_queries.py
├── test_article.py
├── test_author.py
├── test_magazine.py
├── test_models.py
└── test_transcation.py


## Features

- Defines **Authors**, **Articles**, and **Magazines** models with raw SQL interactions
- Implements many-to-many relationships (Authors ↔ Magazines via Articles)
- Supports creation, querying, updating, and deletion of entities
- Contains advanced SQL queries for aggregate data and relationships
- Includes transaction management with context managers for safe DB operations
- Fully tested with `pytest`

## Setup Instructions

### 1. Clone the repository
git clone <https://github.com/JENNIFER754-DEL/phase-3-code-challenge-articles>
cd phase-3-code-challenge-articles
### 2. Activate the virtual environment
If you haven't created it yet:
python -m venv env
### 3. Install dependencies
pip install pytest
### 4. Initialize the database
#### Run the setup script to create tables and seed data:
python scripts/setup_db.py
### Running Tests
Run all tests with:
pytest

## Notes
The project uses raw SQL queries with parameterized statements to prevent SQL injection.

The SQLite database file (articles.db) persists your data.

Transaction management ensures database integrity during complex operations.

The scripts/setup_db.py script must be run first to initialize the DB schema and seed data.

## License
MIT License

