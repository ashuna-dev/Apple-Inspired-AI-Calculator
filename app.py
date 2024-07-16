from flask import Flask, render_template, Response,jsonify
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import google.generativeai as genai
from PIL import Image

app = Flask(__name__)

# Initialize the webcam to capture video
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Initialize Gemini AI
genai.configure(api_key="AIzaSyAHR1jdjWT1CF3rGoNhyRmJbEWjbi5GMMw")
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=0, detectionCon=0.75, minTrackCon=0.75)

def initialize_canvas(frame):
    return np.zeros_like(frame)

def process_hand(hand):
    lmList = hand["lmList"]
    bbox = hand["bbox"]
    center = hand['center']
    handType = hand["type"]
    fingers = detector.fingersUp(hand)
    return lmList, bbox, center, handType, fingers

def weighted_average(current, previous, alpha=0.5):
    return alpha * current + (1 - alpha) * previous

def send_to_ai(model, canvas, fingers):
    if fingers[4] == 1:
        image = Image.fromarray(canvas)
        response = model.generate_content(["solve this math problem", image])
        return response
    return None

# Initialize variables
prev_pos = None
drawing = False
points = []
smooth_points = None
response_text = None

# Initialize canvas
_, frame = cap.read()
canvas = initialize_canvas(frame)

def generate_frames():
    global prev_pos, drawing, points, smooth_points, canvas, response_text

    while True:
        success, img = cap.read()
        if not success:
            break

        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img, draw=True, flipType=True)

        if hands:
            hand = hands[0]
            lmList, bbox, center, handType, fingers = process_hand(hand)
            index_tip = lmList[8]

            if fingers[1] == 1 and fingers[2] == 0:
                current_pos = np.array([index_tip[0], index_tip[1]])
                if smooth_points is None:
                    smooth_points = current_pos
                else:
                    smooth_points = weighted_average(current_pos, smooth_points)
                smoothed_pos = tuple(smooth_points.astype(int))

                if drawing:
                    points.append(smoothed_pos)
                prev_pos = smoothed_pos
                drawing = True
            elif fingers[1] == 1 and fingers[2] == 1:
                drawing = False
                prev_pos = None
                points = []
                smooth_points = None
            elif fingers[0] == 1:
                canvas = initialize_canvas(img)
                points = []
                drawing = False
                prev_pos = None
                smooth_points = None
            elif fingers[4] == 1:
                response_text = send_to_ai(model, canvas, fingers)
                if response_text:
                    response_text = response_text.text

        if len(points) > 1 and drawing:
            cv2.polylines(canvas, [np.array(points)], isClosed=False, color=(0, 0, 255), thickness=5)

        img = cv2.addWeighted(img, 0.5, canvas, 0.5, 0)
        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    global response_text
    return render_template('index.html', response=response_text)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_response')
def get_response():
    global response_text
    return jsonify(response=response_text)

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
