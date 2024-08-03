# 🧮 Virtual AI Calculator

## 📝 Overview
The Virtual AI Calculator is an innovative project that uses OpenCV and Google's Gemini AI to solve any mathematical problem, regardless of complexity. The user can draw the math problem on the screen, and the AI model will interpret the visual input to provide a detailed solution. This project is similar to the Apple iPad calculator but leverages advanced AI technology for enhanced functionality and accuracy.

## ✨ Features
- ✍️ **Draw Math Problems:** Use your finger to draw any mathematical problem on the screen.
- 🖱️ **Move Around:** Move the pointer around the screen by lifting two fingers.
- 🗑️ **Reset Canvas:** Erase the current drawing by lifting the thumb.
- 📤 **Send to AI Model:** Send the visual drawing to the model by lifting the little finger.
- 📊 **Detailed Solutions:** The model interprets the drawing and displays a detailed solution.

## 📋 Requirements
- 🐍 **Python 3.x**
- 👁️ **OpenCV 4.8.0.74**
- ➗ **Numpy 1.23.5**
- 🖼️ **Pillow 9.3.0**
- 🤖 **Google Generative AI 0.1.0**
- 🛠️ **CVZone 1.5.6**
- 🌐 **Django 4.2**


## 🚀 Installation

1. **Obtain the Gemini API Key:**
   - Visit [AI Studio](https://aistudio.google.com) to get your Gemini API key.

2. **Install Dependencies:**
   - Use the following command to install the required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configure the API Key:**
   - Add your API key to `videoapp/view.py`.

4. **Run the Web Application:**
   - Start the web server with:
     ```bash
     python manage.py runserver
     ```

5. **Access the Web Application:**
   - Open your web browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000) to use the app.




2. Follow the drawing rules to interact with the calculator:
    - ✍️ Draw math problems with your pointer finger up.
    - 🖱️ Move around the screen with two fingers lifted.
    - 🗑️ Lift your thumb to reset/erase the canvas.
    - 📤 Lift your little finger to send the visual drawing to the AI model.

3. The AI model will interpret the drawing and display the detailed solution.

## 🎨 Drawing Rules
1. ✍️ The user can draw only when the pointer finger is up.
2. 🖱️ The user can move around the screen by lifting two fingers.
3. 🗑️ Lifting the thumb finger resets/erases the canvas.
4. 📤 The visual drawing is sent to the model when the little finger is up.

## 🤝 Contribution
We welcome contributions to make this project better. Feel free to submit issues and pull requests. Your feedback and suggestions are always welcome!

## 📚 Learning Resources

To better understand the technologies used in this project, you can explore the following resources:

- **OpenCV Documentation:** [OpenCV Documentation](https://docs.opencv.org/)
- **OpenCV detailed video:** [OpenCV Video](https://youtu.be/oXlwWbU8l2o?si=8UFFRz7uRiHsULZr)
- **Air canvas setup:** [Air canvas](https://youtu.be/T7sjrWc4QEc?si=nHRhGhyf86rPtbO3)



## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 🙏 Acknowledgments
- Thanks to everyone who has supported this project.

