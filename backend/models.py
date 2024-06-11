from datetime import datetime
from app import db

class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    task = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=True)

    def __init__(self, title, task, description, date, time=None):
        self.title = title
        self.task = task
        self.description = description
        self.date = datetime.strptime(date, '%Y-%m-%d').date()
        if time:
            self.time = datetime.strptime(time, '%H:%M').time()