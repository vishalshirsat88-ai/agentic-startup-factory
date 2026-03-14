
# Automated Social Media Content Generator
## Overview
This is a minimal Flask MVP for Automated Social Media Content Generator. The application generates social media content using AI-powered content generator.

## Requirements
- Python 3.x
- Flask 2.3.3
- Werkzeug 2.3.7
- gunicorn 21.2.0

## Instructions
1. Install dependencies using pip: `pip install -r requirements.txt`
2. Run the application using gunicorn: `gunicorn app:app --bind 0.0.0.0:$PORT`
3. Access the application at `http://localhost:5000` or your deployed URL
