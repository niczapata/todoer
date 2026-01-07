# Todoer

A simple Flask-based todo list application with user authentication and PostgreSQL database integration.

## Features

- User registration and login
- Create and manage todo items
- User-specific todo lists
- PostgreSQL database for data persistence
- Session-based authentication

## Requirements

- Python 3.13+
- PostgreSQL database
- Flask
- psycopg2

## Installation

1. Clone the repository:
```bash
git clone https://github.com/niczapata/todoer.git
cd todoer
```

2. Create a virtual environment:
```bash
python -m venv todoer
source todoer/bin/activate  # On Windows: todoer\Scripts\activate
```

3. Set up environment variables:
```bash
export FLASK_DATABASE_HOST=your_host
export FLASK_DATABASE_PASSWORD=your_password
export FLASK_DATABASE_USER=your_user
export FLASK_DATABASE=your_database
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Initialize the database:
```bash
flask --app todo init-db
```

6. Run the application:
```bash
flask --app todo run
```

The application will be available at `http://127.0.0.1:5000/`

## Project Structure

```
todoer/
├── todo/
│   ├── __init__.py      # Flask application factory
│   ├── db.py            # Database connection and initialization
│   ├── schema.py        # Database schema and SQL statements
│   ├── auth.py          # Authentication blueprint
│   └── templates/       # HTML templates
└── todoer/              # Virtual environment
```

## Configuration

The application uses the following environment variables:

- `FLASK_DATABASE_HOST`: PostgreSQL host
- `FLASK_DATABASE_PASSWORD`: Database password
- `FLASK_DATABASE_USER`: Database user
- `FLASK_DATABASE`: Database name

## Database Schema

The application uses two main tables:

- `user`: Stores user credentials (username, password)
- `todo`: Stores todo items (description, completion status, timestamps)

## License

MIT
