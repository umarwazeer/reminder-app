from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_migrate import Migrate
from models import Reminder
from app import app, db


@app.route('/reminders', methods=['GET'])
def get_RemindersComponent():
    RemindersComponent = Reminder.query.all()
    return jsonify([
        {
            'id': r.id,
            'title': r.title,
            'task': r.task,
            'description': r.description,
            'date': r.date.strftime('%Y-%m-%d'),
            'time': r.time.strftime('%H:%M') if r.time else None
        } for r in RemindersComponent
    ])
@app.route('/reminders', methods=['POST'])
def add_reminder():
    data = request.get_json()
    title = data.get('title')
    task = data.get('task')
    description = data.get('description')
    date = data.get('date')
    time = data.get('time')
    
    if not title or not task or not date:
        return jsonify({'error': 'Title, task, and date are required'}), 400
    
    try:
        datetime.strptime(date, "%Y-%m-%d")  # Validate date format
        if time:
            datetime.strptime(time, "%H:%M")  # Validate time format if provided
    except ValueError:
        return jsonify({'error': 'Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time (24-hour format)'}), 400
    
    new_reminder = Reminder(title=title, task=task, description=description, date=date, time=time)
    db.session.add(new_reminder)
    db.session.commit()
    
    return jsonify({'message': 'Reminder added successfully'}), 201


@app.route('/reminders/<int:id>', methods=['DELETE'])
def delete_reminder(id):
    reminder = Reminder.query.get_or_404(id)
    db.session.delete(reminder)
    db.session.commit()
    return jsonify({'message': 'Reminder deleted successfully!'})