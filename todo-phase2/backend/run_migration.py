#!/usr/bin/env python3
"""
Script to run database migrations using Alembic
"""

import subprocess
import sys
import os

def run_migration():
    """Run the alembic migration to create the chat_history table"""

    # Change to the backend directory
    backend_dir = os.path.join(os.path.dirname(__file__), 'todo-phase2', 'backend')
    os.chdir(backend_dir)

    print("Running Alembic migration to create chat_history table...")

    # Run the alembic upgrade command
    try:
        result = subprocess.run([
            sys.executable, '-m', 'alembic', 'upgrade', 'head'
        ], check=True, capture_output=True, text=True)

        print("Migration completed successfully!")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error running migration: {e}")
        print(f"Error output: {e.stderr}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: Alembic not found. Please install it using 'pip install alembic'")
        sys.exit(1)

if __name__ == "__main__":
    run_migration()