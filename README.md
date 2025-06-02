📰 Author-Article-Magazine Project

This project models the relationships between authors, articles, and magazines using Python object-oriented programming (OOP) and raw SQL queries. It is designed to strengthen your understanding of database relationships, SQL logic, and Python class design.

🚀 Getting Started
Option 1: Using Pipenv

pipenv install
pipenv shell
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt

🗄️ Database Setup

Using SQLite by default:
Define your schema in lib/db/schema.sql.

Set up the database:
python scripts/setup_db.py
The database file articles.db will be created with the necessary tables for authors, articles, and magazines.

🧪 Running Tests

Tests are written with pytest. To run them:
pytest
Make sure your database is set up before testing.

✅ Features
Author Create and save authors

Find authors by ID or name

Retrieve all articles by an author

Get all magazines the author contributed to

Add new articles

Get topic areas from associated magazines

Magazine
Create and save magazines

Find magazines by ID, name, or category

Retrieve all articles in a magazine

Get all contributing authors

Get titles of all articles

Find authors with more than 2 articles in the magazine

Article
Create and save articles

Find articles by various fields (ID, title, author, magazine)

