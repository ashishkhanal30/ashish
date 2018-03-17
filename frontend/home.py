from flask import render_template
from .app import frontend_app
from flask import request, redirect

@frontend_app.route('/')
def index():
    return render_template('index.html')


@frontend_app.route('/sample_page')
def sample_page():
    return render_template('sample_page.html')


@frontend_app.route('/walmart_trip')
def walmart_trip():
    print(request.args.get('desc_about'))
    data= ""
    if desc_about is None:
        print ('Desc about is null)')
        data = "No request"
    else:
        print('desc about is not null', desc_about)
        data = "User requesting some data"
        # if desc_about
    return render_template('walmarttrip.html', data=data)
    # if desc_about == 'transport':
@frontend_app.route('/login', methods=['GET', 'POST'])
def login():
    print(request.form)
    username=request.form.get('username')
    password=request.form.get('password')
    login_message=""
    if username is None:
        print('no username supplied')
        credentials_match = True

    else:
        print('yes supplied')
        if username== 'ashish' and  password=='don':
            credentials_match = True
        else:
            credentials_match = False

        if credentials_match ==True:
             print('launching')
             return redirect('/app')

        else:
            login_message="invalid"
    return render_template('one.html')