# Flask Reminder App

A simple reminder application built with Flask and Vue.js, allowing users to manage and schedule their tasks efficiently.

## Features

- Create, update, and delete reminders.
- Set reminders with date and time.
- View all reminders in a list format.

## Technologies Used

- **Backend**: Flask, SQLAlchemy, Flask-Migrate, Flask-CORS
- **Frontend**: Vue.js
- **Database**: MySQL

## Project Structure

```bash
flask-reminder-app/
│
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   ├── config.py
│   ├── requirements.txt
│   ├── migrations/
│   └── __init__.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── .gitignore
│   ├── babel.config.js
│   ├── package.json
│   ├── README.md
│   └── vue.config.js
│
└── README.md
