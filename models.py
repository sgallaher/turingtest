from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlalchemy as sa

db = SQLAlchemy()

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(64))
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    total_duration = db.Column(db.Float)  # in seconds

    # Store answers and timings/spelling scores
    q_data = db.Column(db.JSON)  # a dict with q1 to q18, each holding: answer, duration, spelling_score, meaning_score

    verdict = db.Column(db.String(20))  # 'human', 'ai', 'unsure'
    confidence = db.Column(db.Float)    # 0.0 to 1.0

