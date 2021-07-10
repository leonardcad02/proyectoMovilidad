#importar todo lo que este en auth
from app.models import UserData
from flask import render_template, redirect, flash, url_for, session

from app.forms import LoginForm
from . import auth
from app.firestone_service import get_user
from app.models import UserData, UserModel
from flask_login import login_user

# Guardar todas las rutas

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user_doc = get_user(username)

        if user_doc.to_dict() is not None:
            password_from_db = user_doc.to_dict()['password']

            if password == password_from_db:
                user_data = UserData(username, password)
                user = UserModel(user_data)
                login_user(user)

                flash('Bienvenido de nuevo')

                redirect(url_for('hello'))
            else:
                 flash('La información no coincide')  
        else:
            flash('El usuario no existe')      
        return redirect(url_for('index'))
    return render_template('login.html', **context)