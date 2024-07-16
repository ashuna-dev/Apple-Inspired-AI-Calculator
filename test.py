import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import google.generativeai as genai
from PIL import Image
# Initialize the webcam to capture video
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# initialize gemini
genai.configure(api_key="AIzaSyAHR1jdjWT1CF3rGoNhyRmJbEWjbi5GMMw")
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=0, detectionCon=0.75, minTrackCon=0.75)

def initialize_canvas(frame):
    return np.zeros_like(frame)

def process_hand(hand):
    lmList = hand["lmList"]  # List of 21 landmarks for the hand
    bbox = hand["bbox"]  # Bounding box around the hand (x,y,w,h coordinates)
    center = hand['center']  # Center coordinates of the hand
    handType = hand["type"]  # Type of the hand ("Left" or "Right")
    fingers = detector.fingersUp(hand)  # Count the number of fingers up
    return lmList, bbox, center, handType, fingers

def weighted_average(current, previous, alpha=0.5):
    return alpha * current + (1 - alpha) * previous

def send_to_ai(model, canvas,fingers):
    if fingers[4]==1:
        image=Image.fromarray(canvas)
        response=model.generate_content(["solve this math problem",image])
        return response
    
    return None
    

# Initialize variables
prev_pos = None
drawing = False
points = []  # Store points for drawing
smooth_points = None  # Smoothed position

# Initialize canvas
_, frame = cap.read()
canvas = initialize_canvas(frame)

# Set up window
window_name = "Image"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 1920, 1080)

while True:
    # Capture each frame from the webcam
    success, img = cap.read()
    
    if not success:
        print("Failed to capture image")
        break

    # Flip the image horizontally for a later selfie-view display
    img = cv2.flip(img, 1)
    
    hands, img = detector.findHands(img, draw=True, flipType=True)

    if hands:
        hand = hands[0]
        lmList, bbox, center, handType, fingers = process_hand(hand)
        
        # Get the positions of the index and middle finger tips
        index_tip = lmList[8]
        thumb_tip = lmList[4]
        
        # Determine drawing state based on fingers up
        if fingers[1] == 1 and fingers[2] == 0:  # Only index finger is up
            current_pos = np.array([index_tip[0], index_tip[1]])
            if smooth_points is None:
                smooth_points = current_pos
            else:
                smooth_points = weighted_average(current_pos, smooth_points)
            smoothed_pos = tuple(smooth_points.astype(int))

            if drawing:  # Only add to points if already drawing
                points.append(smoothed_pos)
            prev_pos = smoothed_pos
            drawing = True
        elif fingers[1] == 1 and fingers[2] == 1:  # Both index and middle fingers are up
            drawing = False
            prev_pos = None
            points = []  # Clear points to avoid connection
            smooth_points = None
        elif fingers[0] == 1:  # Thumb is up
            canvas = initialize_canvas(img)
            points = []
            drawing = False
            prev_pos = None
            smooth_points = None
            
        elif fingers[4]==1:
            response_text=send_to_ai(model,canvas,fingers)
            if response_text:
                print(response_text.text)

    # Draw polyline on the canvas
    if len(points) > 1 and drawing:
        cv2.polylines(canvas, [np.array(points)], isClosed=False, color=(0, 0, 255), thickness=5)

    # Combine the image and canvas
    img = cv2.addWeighted(img, 0.5, canvas, 0.5, 0)

    # Display the image in a window
    cv2.imshow(window_name, img)

    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
