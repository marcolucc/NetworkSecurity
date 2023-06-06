import flask
from flask import request
import subprocess
import os

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/ping', methods=['POST'])
def ping():
    try:
        hostname = request.json['host']
    except:
        hostname = None

    if hostname and ' ' not in hostname:
        command = 'ping -c 1 {}'.format(hostname)
        ret = None
        with open(os.devnull, 'wb') as devnull:
            try:
                ret = subprocess.run(command, shell=True,
                                     stdout=devnull, stderr=devnull, timeout=3)
            except subprocess.TimeoutExpired:
                return flask.jsonify({'status': ' The timeout expired.', 'command': command})

        return flask.jsonify({'return_code': ret.returncode,
                              'command': command, 'status': 'ok'})
    else:
        error = ' no hostname supplied' if not hostname \
            else ' hostnames can\'t have any spaces!'

        return flask.jsonify({'status': error})


if __name__ == '__main__':
    app.run(debug=True)