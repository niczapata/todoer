"""
Database connection and initialization module for the todo application.

This module provides functions for managing PostgreSQL database connections
within a Flask application context, including connection retrieval,
initialization, and cleanup.
"""
import psycopg2
from psycopg2.extras import RealDictCursor
import click
from flask import current_app, g
from flask.cli import with_appcontext
from .schema import instructions


def get_db():
    """
    Get or create a database connection and cursor.

    Returns a tuple of (database connection, cursor). The connection is
    stored in Flask's g object to ensure request-scoped reuse.

    Returns:
        tuple: (psycopg2 connection, cursor) for database operations
    """
    if "db" not in g:
        # Create new connection using configuration from Flask app
        g.db = psycopg2.connect(
            host=current_app.config["DATABASE_HOST"],
            user=current_app.config["DATABASE_USER"],
            password=current_app.config["DATABASE_PASSWORD"],
            dbname=current_app.config["DATABASE"],
        )
        g.c = g.db.cursor(cursor_factory=RealDictCursor)
    return g.db, g.c


def init_db():
    """
    Initialize the database by executing schema instructions.

    Executes all SQL statements defined in the schema instructions to
    create the necessary tables and structures.
    """
    db, c = get_db()
    # Execute each SQL instruction from schema
    for i in instructions:
        c.execute(i)
    db.commit()


def close_db(e=None):
    """
    Close the database connection at the end of a request.

    Args:
        e: Optional exception object passed by Flask's teardown handler
    """
    db = g.pop("db", e)
    # Only close if db is not the exception object
    if db is not e:
        db.close()


def init_app(app):
    """
    Register database functions with the Flask application.

    Registers the close_db function as a teardown handler and adds
    the init-db CLI command for database initialization.

    Args:
        app: Flask application instance
    """
    # Register close_db to be called after each request
    app.teardown_appcontext(close_db)

    # Register CLI command to initialize the database
    @app.cli.command("init-db")
    def init_db_command():
        init_db()
        click.echo("Initialized the database")
