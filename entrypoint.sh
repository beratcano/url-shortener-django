#!/bin/bash

set -e

# Print environment variables for debugging
printenv

# Set Django settings module
export DJANGO_SETTINGS_MODULE=url_shortener.settings

# Apply database migrations
python manage.py migrate

# Start the Django development server
python manage.py runserver 0.0.0.0:8000
