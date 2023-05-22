from flask import Flask, redirect, url_for, render_template, request,sessions
import requests
from PIL import Image
import cv2
import numpy as np
import io

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/edit')
def edit():
    return render_template('index3.html')

@app.route('/txt',methods=[ 'POST','GET'])
def text():
    if request.method=="POST":
        text = request.form['text']
        colab_url = 'https://colab.research.google.com/drive/1FC1xyBJ-manwxED5RNvvQVpp8RdMj9_T#scrollTo=Uh5Ak8_YCGQ7'
        response = requests.post(colab_url, data={'text': text})
        # return render_template("imgshow.html",data=response)
        return redirect("rimage")

    else:   
        return render_template('index2.html')

@app.route('/drp')
def dropdown():
    return render_template('index.html')

@app.route('/rimage', methods=['POST','GET'])
def receive_image():
    if 'data' in request.files:
        image_file = request.files['data']
        # Process the received image file as needed
        # ...

        # Save the image file temporarily
        image_path = 'received_image.png'
        image_file.save(image_path)

        # Open the image using PIL
        pil_image = Image.open(image_path)

        # Render the image in the HTML template
        return render_template('imgshow.html', image_file=pil_image)

    return 'No image file received'

if __name__ == '__main__':
    app.run(debug=True)