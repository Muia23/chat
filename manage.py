from flask import Flask
from flask_socketio import SocketIO, send

#creating flask app

app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
