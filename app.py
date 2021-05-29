from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,IntegerField,BooleanField
from wtforms.validators import InputRequired,Length, AnyOf, Email

class LoginForm(FlaskForm):
   username = StringField('username',validators=[
      InputRequired(),Length(min=3,max=8),
   ])
   password = PasswordField('password',validators=[
      InputRequired(),
      AnyOf(values=['secret','password']),
   ])

   age = IntegerField('age')
   yesno = BooleanField('yesno')
   Email = StringField('email',validators=[

   ])

def create_app():
   app = Flask(__name__)
   app.config['SECRET_KEY'] = 'sadsaddsada-dcddc'

   @app.route('/',methods=['GET','POST'])
   def index():
      form = LoginForm()

      if form.validate_on_submit():
         return f'<h1>Username: {form.username.data} Password: {form.password.data} Age:{form.age.data} Yesno:{form.yesno.data} Email:{form.email.data}</h1>'

      return render_template('index.html',form=form)

   return app