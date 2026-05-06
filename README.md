# emotion_detector
========================================
   AI EMOTION DETECTOR - QUICK START
========================================

REQUIREMENTS:
- Python 3.8 or above
- Webcam connected

STEPS TO RUN:
--------------

STEP 1 - Install dependencies:
   pip install -r requirements.txt

STEP 2 - Run the project:
   python emotion_detector.py

STEP 3 - A webcam window will open.
   Look at the camera — your emotion will show on screen!

STEP 4 - Press 'q' to quit.

EMOTIONS DETECTED:
   happy, sad, angry, surprise, fear, disgust, neutral
<!-- 
The issue is NumPy 2.0 got installed but other packages need NumPy 1.x. Run this one fix command:
bashpip install "numpy<2" --force-reinstall
Then immediately run:
bashpython emotion_detector.py -->

NOTE:
- First run may take a minute to download AI models (needs internet)
- Make sure your webcam is connected and not used by another app
