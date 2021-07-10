from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest
from app import create_app
from flask_login import login_required, current_user
from app.firestone_service import get_todos, get_users


app = create_app()

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)    

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


@app.route('/hello', methods=['GET'])
@login_required
def hello():
    userIp = session.get('userIp')
    username = current_user.id
    context = {
        'userIp': userIp,
        'todos': get_todos(user_id = username),
        'username': username,
    }      

    users = get_users()
    print(users)
    for  user in users:
        print(users)
        print("Entro")
        print(user.id)
        print(user.to_dict()['password'])  

    return render_template('hello.html', **context)


if __name__ == '__main__':
    app.run(debug=True)