import cv2
import numpy as np
from tensorflow.keras.models import load_model
from flask import Flask, jsonify

app = Flask(__name__)
model = load_model('traffic_classifier.h5')

@app.route('/')
def hello():
## dictionary that define traffic signs rules
    classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)',      
            3:'Speed limit (50km/h)',       
            4:'Speed limit (60km/h)',      
            5:'Speed limit (70km/h)',    
            6:'Speed limit (80km/h)',      
            7:'End of speed limit (80km/h)',     
            8:'Speed limit (100km/h)',    
            9:'Speed limit (120km/h)',     
           10:'No passing',   
           11:'No passing veh over 3.5 tons',     
           12:'Right-of-way at intersection',     
           13:'Priority road',    
           14:'Yield',     
           15:'Stop',       
           16:'No vehicles',       
           17:'Veh > 3.5 tons prohibited',       
           18:'No entry',       
           19:'General caution',     
           20:'Dangerous curve left',      
           21:'Dangerous curve right',   
           22:'Double curve',      
           23:'Bumpy road',     
           24:'Slippery road',       
           25:'Road narrows on the right',  
           26:'Road work',    
           27:'Traffic signals',      
           28:'Pedestrians',     
           29:'Children crossing',     
           30:'Bicycles crossing',       
           31:'Beware of ice/snow',
           32:'Wild animals crossing',      
           33:'End speed + passing limits',      
           34:'Turn right ahead',     
           35:'Turn left ahead',       
           36:'Ahead only',      
           37:'Go straight or right',      
           38:'Go straight or left',      
           39:'Keep right',     
           40:'Keep left',      
           41:'Roundabout mandatory',     
           42:'End of no passing',      
           43:'End no passing veh > 3.5 tons' }
    
    # Use OpenCV to capture an image from the camera
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    # Convert the image to RGB format
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Resize the image to match the input size of the model
    image = cv2.resize(image, (32, 32))

    # Normalize the image
    image = image / 255.0

    # Make a prediction using the model
    prediction = model.predict(np.array([image]))

    # Get the predicted label
    label = np.argmax(prediction)

    # Return the predicted label as a JSON object
    return jsonify({'label': label})

if __name__ == '__main__':
    app.run(debug=True)
