from flask import Flask, render_template, request, jsonify
from config import Config
from forms import TuringTestForm
from models import db, Submission
import time, datetime
from textblob import TextBlob
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

def create_tables():
    db.create_all()
migrate = Migrate(app, db)
@app.route('/', methods=['GET', 'POST'])
def index():
    form = TuringTestForm()
    if form.validate_on_submit():
        start_time = float(request.form.get('startTime', time.time()))
        total_duration = time.time() - start_time

        answers = {}
        for i in range(1, 19):
            key = f'q{i}'
            text = getattr(form, key).data
            duration = float(request.form.get(f'{key}_time', 0))
            spelling_score = float(TextBlob(text).correct().lower() == text.lower())  # crude
            meaning_score = float(len(text.strip().split()) > 3)  # dummy rule for now

            answers[key] = {
                'answer': text,
                'duration': duration,
                'spelling_score': spelling_score,
                'meaning_score': meaning_score
            }

        # Dummy verdict rule
        avg_meaning = sum(v['meaning_score'] for v in answers.values()) / 18
        verdict = 'human' if avg_meaning > 0.5 else 'ai'
        confidence = avg_meaning

        submission = Submission(
            ip_address=request.remote_addr,
            total_duration=total_duration,
            q_data=answers,
            verdict=verdict,
            confidence=confidence
        )
        db.session.add(submission)
        db.session.commit()

        return render_template('result.html', verdict=verdict, confidence=confidence)
    return render_template('index.html', form=form)

@app.route('/admin')
def admin():
    submissions = Submission.query.order_by(Submission.submitted_at.desc()).all()
    return render_template('admin.html', submissions=submissions)

if __name__ == '__main__':
    with app.app_context():
        create_tables()
    app.run(debug=True)