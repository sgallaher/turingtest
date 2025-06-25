
# Updated forms.py
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class TuringTestForm(FlaskForm):
    q1 = TextAreaField("If I leave a slice of toast outside overnight, what might happen to it?", validators=[DataRequired()])
    q2 = TextAreaField("Why do people usually check the weather before going on a hike?", validators=[DataRequired()])
    q3 = TextAreaField("What might someone say if they accidentally step on your foot?", validators=[DataRequired()])
    q4 = TextAreaField("Tell a joke that would only make sense to someone from your country.", validators=[DataRequired()])
    q5 = TextAreaField("Make a pun involving fruit and technology.", validators=[DataRequired()])
    q6 = TextAreaField("What’s funny about this: 'I used to play piano by ear, but now I use my hands'?", validators=[DataRequired()])
    q7 = TextAreaField("Describe a moment when you felt truly proud of yourself.", validators=[DataRequired()])
    q8 = TextAreaField("What’s something small that instantly improves your mood?", validators=[DataRequired()])
    q9 = TextAreaField("What’s your favorite childhood memory?", validators=[DataRequired()])
    q10 = TextAreaField("You said earlier that you dislike seafood. But now you mention sushi nights with friends. Can you explain?", validators=[DataRequired()])
    q11 = TextAreaField("Have you ever regretted not speaking up in a situation?", validators=[DataRequired()])
    q12 = TextAreaField("What were you doing this time yesterday?", validators=[DataRequired()])
    q13 = TextAreaField("What does it feel like to walk into a quiet room where everyone suddenly stops talking?", validators=[DataRequired()])
    q14 = TextAreaField("Describe the atmosphere of a wedding in three adjectives.", validators=[DataRequired()])
    q15 = TextAreaField("What’s a typical way to say goodbye informally in your country?", validators=[DataRequired()])
    q16 = TextAreaField("Would you rather be liked or respected? Why?", validators=[DataRequired()])
    q17 = TextAreaField("Describe the smell of rain without saying 'wet'.", validators=[DataRequired()])
    q18 = TextAreaField("Is it ever right to break the rules?", validators=[DataRequired()])
    submit = SubmitField("Submit")