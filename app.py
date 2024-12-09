from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Serve the input page
@app.route('/input')
def input_page():
    return render_template('input.html')

# Serve the display page
@app.route('/display')
def display_page():
    return render_template('display.html')

# Handle real-time data submission
@socketio.on('submit_data')
def handle_submit_data(data):
    print(f"Received data: {data}")
    # Broadcast the data to all connected clients
    emit('update_display', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
