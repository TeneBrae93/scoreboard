
# Gymnastics Score Display

This is a simple server/client application for displaying gymnastics scores in real-time. 
- **Computer 1 (Input):** Used to input gymnast names and scores.
- **Computer 2 (Display):** Dynamically displays the submitted scores.

Built using **Flask** and **Flask-SocketIO**, this project demonstrates real-time communication between devices using WebSockets.

---

## Features

- Real-time score updates across devices.
- Clean and professional user interface for both input and display.
- Lightweight, built with Python and Flask.

---

## Requirements

- Python 3.7 or higher
- Flask
- Flask-SocketIO

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/TeneBrae93/scoreboard.git
   cd scoreboard
   ```

2. **Install the required Python packages:**

   ```bash
   pip install flask flask-socketio
   ```

3. **Run the Flask server:**

   ```bash
   python app.py
   ```

4. **Access the application:**

   - **Input page:** `http://<server_ip>:5000/input`
   - **Display page:** `http://<server_ip>:5000/display`

---

## Usage

### Input Computer (Computer 1)
1. Open the input page.
2. Enter the gymnast's name and score.
3. Click "Submit" to send the data to the server.

### Display Computer (Computer 2)
1. Open the display page.
2. The submitted scores will automatically update in real-time.

---

## Project Structure

```
gymnastics-score-display/
├── app.py               # Main Flask application
├── templates/
│   ├── input.html       # HTML for input page
│   ├── display.html     # HTML for display page
└── static/              # Static files (if any)
```

---

## Author
Created by Tyler Ramsbey!
