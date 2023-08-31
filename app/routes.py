from flask import render_template, request


from app import app
from app.models import CountryRange


@app.route('/')
def index():
    if request.remote_addr == "::1":
        request.remote_addr = "127.0.0.1"

    user = {
        'ip': request.remote_addr,
        'ip_int': CountryRange.ip2int(request.remote_addr),
        'country': CountryRange.convert_ip(request.remote_addr),
    }

    return render_template('index.html', title='Home', user=user)


@app.route('/country')
def country():
    ip = request.args.get('ip', default=request.remote_addr, type=str)
    return CountryRange.convert_ip(ip)
