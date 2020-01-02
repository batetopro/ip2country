from flask import render_template, request
from app.util import ip2country, ip2int
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'Hristo',
        'ip': request.remote_addr,
        'ip_int': ip2int(request.remote_addr),
        'country': ip2country(request.remote_addr),
    }
    return render_template('index.html', title='Home', user=user)


@app.route('/country')
def country():
    return ip2country(request.remote_addr)
