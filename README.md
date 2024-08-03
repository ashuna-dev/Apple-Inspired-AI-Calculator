# 🧮 Apple-Inspired AI Calculator

## 📝 Overview
The Apple-Inspired AI Calculator is an innovative project that utilizes OpenCV and Google’s Gemini AI to solve mathematical problems of any complexity. The user can draw the math problem on the screen, and the AI model will interpret the visual input to provide a detailed solution. This project is similar to the Apple iPad calculator but leverages advanced AI technology for enhanced functionality and accuracy.

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
   - Run the following command to install the required packages:
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
   - Open your web browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to use the app.

## 🎥 Demo Video

Check out the demo video to see the Virtual AI Calculator in action:

[Watch the Demo on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7221422183175139328/)

## 🎨 Drawing Rules

To interact with the calculator, follow these drawing rules:
- ✍️ Draw math problems only when the pointer finger is up.
- 🖱️ Move around the screen by lifting two fingers.
- 🗑️ Reset/erase the canvas by lifting the thumb.
- 📤 Send the visual drawing to the AI model by lifting the little finger.

The AI model will then interpret the drawing and display a detailed solution.

## 📚 Learning Resources

To better understand the technologies used in this project, you can explore the following resources:
- **OpenCV Documentation:** [OpenCV Documentation](https://docs.opencv.org/)
- **OpenCV Detailed Video:** [OpenCV Video](https://youtu.be/oXlwWbU8l2o?si=8UFFRz7uRiHsULZr)
- **Air Canvas Setup:** [Air Canvas](https://youtu.be/T7sjrWc4QEc?si=nHRhGhyf86rPtbO3)

## 🤝 Contribution

We welcome contributions to enhance this project. Feel free to submit issues and pull requests. Your feedback and suggestions are highly appreciated!

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🙏 Acknowledgments

- Thanks to everyone who has supported this project.


