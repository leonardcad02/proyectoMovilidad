from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from  wtforms.validators import DataRequired

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['SECRET_KEY'] = 'SUPER SECRETO'

bootstrap = Bootstrap(app)

todos = ['Todo 1', 'Todo 2', 'Todo 3']

class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit  = SubmitField('Enviar')


@app.errorhandler(500)

def internal_server_error(error):
    return render_template('500.html', error=error)

@app.errorhandler(404)

def not_found(error):
    return render_template('404.html', error= error)
  


@app.route('/')
def index():
    userIp = request.remote_addr
    make = redirect('/hello')
    response = make_response(make)
    session['userIp'] = userIp
    return response


@app.route('/hello')
def hello():
    userIp = session.get('userIp')
    loginForm = LoginForm()
    context = {
        'userIp': userIp,
        'todos': todos,
        'loginForm': loginForm,
    }

    return render_template('hello.html', **context)


if __name__ == '__main__':
    app.run(debug=True)