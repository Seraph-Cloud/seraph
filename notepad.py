# CREATE NEW POST
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')
# EDIT POST
@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)
@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = Flask.get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))
# AUTHENTICATION CODE
from flask_login import LoginManager
login_manager = flask_login.LoginManager()

login_manager.login_view = "users.login"
login_manager.login_message = u"You must be logged in to view this page."
login_manager.login_message_category = "info"
login_manager.anonymous_user = 'Anonymous'
login_manager.refresh_view = "accounts.reauthenticate"
login_manager.needs_refresh_message = (
    u"To protect your account, please reauthenticate to access this page."
)
# SESSION SEC
login_manager.session_protection = "strong"
login_manager.needs_refresh_message_category = "info"
@login_manager.user_loader
# FUNCTIONS
def load_user(user_id):
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = flask_login.LoginForm()
    if form.validate_on_submit():

        login_manager.login_user(user)

        Flask.flash('Logged in successfully.')

        next = Flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return Flask.abort(400)

        return Flask.redirect(next or Flask.url_for('index'))
    return Flask.render_template('login.html', form=form)

@app.route("/settings")
@login_required
def settings():
    pass
@app.route("/logout")

@login_required
def logout():
    logout_user()
    return redirect('/')
@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return ()
@login_manager.request_loader
def load_user_from_request(request):

    # first, try to login using the api_key url arg
    api_key = request.args.get('api_key')
    if api_key:
        user = Flask.User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # next, try to login using Basic Auth
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        try:
            api_key = base64.b64decode(api_key)
        except TypeError:
            pass
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # finally, return None if both methods did not login the user
    return None
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(alternative_id=user_id).first()
def get_id(self):
    return unicode(self.alternative_id)
class CustomSessionInterface(SecureCookieSessionInterface):
    """Prevent creating session from API requests."""
    def save_session(self, *args, **kwargs):
        if g.get('login_via_header'):
            return
        return super(CustomSessionInterface, self).save_session(*args,
                                                                **kwargs)

app.session_interface = CustomSessionInterface()

@user_loaded_from_header.connect
def user_loaded_from_header(self, user=None):
    g.login_via_header = True
# RESTRICTING POSTS
#@app.route('/post')
#@login_required
#def post():
#    pass
# FOR RESTICTING ONLY CERTAIN PARTS OF THE WEBAPP
# if not current_user.is_authenticated:
#    return current_app.login_manager.unauthorized()
