from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest
from app import create_app
from app.forms import LoginForm


app = create_app()

todos = ['Todo 1', 'Todo 2', 'Todo 3']


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner.run(tests)
    


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


@app.route('/hello', methods=['GET','POST'])
def hello():
    userIp = session.get('userIp')
    loginForm = LoginForm()
    username = session.get('username')
    context = {
        'userIp': userIp,
        'todos': todos,
        'loginForm': loginForm,
        'username': username,
    }
    if loginForm.validate_on_submit():
        username = loginForm.username.data
        session['username'] =username
        flash('Nombre de usario registrado con éxito!')

        
        return redirect(url_for('index'))

        
    return render_template('hello.html', **context)


if __name__ == '__main__':
    app.run(debug=True)