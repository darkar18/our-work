from flask import Flask, redirect, url_for, render_template, request,sessions,send_file,session
import requests
from flask_ngrok import run_with_ngrok
import requests
from PIL import Image
import json
from pyngrok import ngrok



def generate_data(n=1,seed=200):
  latent_codes = sample_codes(generator, n, latent_space_type,seed)
  # print(latent_codes)
  images = generator.easy_synthesize(latent_codes, **synthesis_kwargs)['image']
  # print(images)
  return images,latent_codes

def edit_latent(sl1,sl2,sl3,sl4,sl5):

  _,latent = generate_data(seed=686)
  latent+= boundaries['Gender'] * sl1
  latent+= boundaries['Young'] * sl2
  latent+= boundaries['Smiling'] * sl3
  latent+= boundaries['Wearing_Hat'] * sl4
  latent+= boundaries['Heavy_Makeup'] * sl5
  new_images = generator.easy_synthesize(latent, **synthesis_kwargs)['image']
  return new_images


app = Flask(__name__,template_folder="/content/interfacegan/website/templates",static_folder="/content/interfacegan/website/static")
ngrok.set_auth_token("2QAhooVNSVU2JEcbLIINLt6S4I4_52UPLbiS3iyJhXkzHTqfx")
public_url =  ngrok.connect(5000).public_url
print(f'your webapp is on: {public_url}/')
run_with_ngrok(app)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/txt',methods=[ 'POST','GET'])
def text():
    if request.method=="POST":
        text = request.form['text']
        response=requests.post
        # return render_template("imgshow.html",data=response)
        return redirect("/mkdata")

    else:   
        return render_template('index2.html')
@app.route('/drp')
def dropdown():
    return render_template('index.html')
@app.route('/edit',methods=["GET","POST"])
def edit():
  if request.method == "POST":
    gender = int(request.form['sl1'])
    age = int(request.form['sl2'])
    smile = int(request.form['sl3'])
    hat = int(request.form['sl4'])
    make_up = int(request.form['sl5'])
    image_data = edit_latent(gender,age,smile,hat,make_up)
    image_data = image_data.squeeze()
    image = Image.fromarray(image_data)

    # Convert the image to bytes
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    image_bytes.seek(0)
    # return render_template("Edit.html")
    return send_file(image_bytes, mimetype='image/png')

@app.route('/mkdata')
def getimage():
    return render_template('index3.html')

# Create a route that will return the processed data.
@app.route("/gen",methods=["POST","GET"])
def generated_data():
  image_data,latent = generate_data(seed=686)
  image_data = image_data.squeeze()
  image = Image.fromarray(image_data)

  # Convert the image to bytes
  image_bytes = io.BytesIO()
  image.save(image_bytes, format='PNG')
  image_bytes.seek(0)
  return send_file(image_bytes, mimetype='image/png')
  return "generation of data pending...."
if __name__ == '__main__':
    app.run()
