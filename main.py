from os import error
import re
from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = ['Todo 1', 'Todo 2', 'Todo 3']

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
    response.set_cookie('userIp',userIp)

    return response


@app.route('/hello')
def hello():
    userIp = request.cookies.get('userIp')
    context = {
        'userIp': userIp,
        'todos': todos,
    }
    return render_template('hello.html', **context)


if __name__ == '__main__':
    app.run(debug=True)