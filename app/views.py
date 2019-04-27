"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash

import datetime

from app.forms import Register
from app.forms import Login
from app.forms import Post 

from app.models import UserProfile
from app.models import UserPost 
from app.models import UserLikes
from app.models import UserFollows

from werkzeug.utils import secure_filename
from flask import jsonify
import os


###
# Routing for your applpython3.5 -m venv venv ication.
###


# Please create all new routes and view functions above this route.
# This route is now our catch all route for our VueJS single page
# application.
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    """
    Because we use HTML5 history mode in vue-router we need to configure our
    web server to redirect all routes to index.html. Hence the additional route
    "/<path:path".

    Also we will render the initial webpage and then let VueJS take control.
    """
    return render_template('index.html')


# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages


###
# The functions below should be applicable to all Flask apps.
###

def format_date_joined(jdate):
    
    return  jdate.strftime("%B, %Y")

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
    
    

@app.route('/api/users/register', method = ['POST'])
def register():
    form = Register()
    if request.method == 'POST':
        if form.validate_on_submit():
            
            user = form.username.data
            password = form.password.data
            firstname = form.firstname.data
            lastname = form.lastname.data
            email = form.email.data
            location = form.location.data
            biography = form.biography.data
            photo = form.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            x  = datetime.datetime.now()
            date = x.strftime("%x")
            #user = UserProfile(id = id, username= user,password=password, firstname=firstname, last_name = lastname, email= email, location = location,biography=biography, joined_on = date ,photo = filename)
            user = UserProfile(username= user, password= password, first_name = firstname, last_name = lastname, emal= email, location = location, bio = biography, photo = filename)
            db.session.add(user)
            db.session.commit()
            return(redirect "/registered")


@app.route('/api/users/{user_id}/posts', method=["POST"])
def posts():
    if current_user.is_authenticated:
        return render_template('posts.html')

@app.route('/api/auth/login', method=["POST"])
def login():
    if current_user.is_authenticated:
        return render_template('posts.html')
    form = Login()
    if request.method == "POST" and form.validate_on_submit():
        # change this to actually validate the entire form submission
        # and not just one field
        username=form.username.data
        password=form.password.data
        
        user = UserProfile.query.filter_by(username=username).first()
        print(user)
        flash(user.first_name)
        
        if user is not None and check_password_hash(user.password, password ):
            print("logged")
            login_user(user)
            return redirect(url_for('posts'))


        else:
            flash('Username or Password is incorrect.', 'danger')
            flash_errors(form)
            return render_template('login.html', form=form)
        flash('Logged in successfully.', 'success')
        return render_template('posts.html')
       
    else:
        flash('Username or Password is incorrect.', 'danger')
        flash_errors(form)
        return render_template('login.html', form=form)

@app.route('/api/auth/logout', method = ['GET'] )
@login_required
def logout():
    # Logout the user and end the session
    logout_user()
    flash('You have been logged out.', 'Retry')
    return render_template('home.html')

@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))
    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
