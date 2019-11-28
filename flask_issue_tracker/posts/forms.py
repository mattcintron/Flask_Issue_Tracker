from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Issue Title - State [Open or Closed]', validators=[DataRequired()])
    content = TextAreaField('Issue Details', validators=[DataRequired()])
    submit = SubmitField('Submit')