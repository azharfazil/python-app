from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')

def details():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        'hostname': socket.gethostname()
        'message': "This is working Great Now with short ID! Good Job:"
    })

@app.route('/api/v1/healthz')

def health():
    return jsonify({
        'status': 'up'
    }), 200

if __name__ == '__main__':

    app.run(host="0.0.0.0")


# '/api/vi/details'
# '/api/v1/healthz'
