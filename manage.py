#!/usr/bin/env python
import os
import sys
from pathlib import Path

def main():
    """Main execution for Django management commands."""
    # Detect environment (default: production)
    DJANGO_ENV = os.getenv("DJANGO_ENV", "production").lower()
    
    # Set settings module based on environment
    settings_module = f"forge.settings.{DJANGO_ENV}" if DJANGO_ENV in {"development", "staging"} else "forge.settings.production"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    # Load environment variables from .env if available
    dotenv_path = Path(__file__).resolve().parent / ".env"
    if dotenv_path.exists():
        try:
            from dotenv import load_dotenv
            load_dotenv(dotenv_path)
        except ImportError:
            print("Warning: `python-dotenv` not installed. Skipping .env loading.")

    # Ensure Django is installed and handle errors gracefully
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Ensure it's installed and available on your PYTHONPATH. "
            "Activate your virtual environment if needed."
        ) from exc

    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()