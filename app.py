from flask import Flask , render_template , request
import cv2 as cv 
import numpy as np
from keras.models import load_model
app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():
    d={
0:'Bird-drop',
 1:'Clean',
 2:'Dusty',
 3:'Electrical-damage',
 4:'Physical-Damage',
 5:'Snow-Covered'}
    imagefile= request.files['imagefile']
    image_path = r'C:\Users\CSEGPUs-02\Downloads\codes\codes\static/'+ imagefile.filename
    imagefile.save(image_path)
    img=cv.imread(image_path)
    img=cv.resize(img,(224, 224))
    img=np.array([img])
    print(img.shape)
    loaded_model = load_model('./my_keras_model.keras')
    res=np.argmax(loaded_model.predict(img))
    # print('\n\n\\n\n',res,'\n\n\n\n')
    return render_template('index.html',prediction=d[res],path=imagefile.filename)
if __name__ == '__main__':
    app.run(port=3000)
<!DOCTYPE html>
<html>
    <head>
        <title>Tutorial</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
    </head>

    <body>
        <h1 class="text-center">Image Classifier</h1>
        <form class="p-3 text-center" action='/', method="post" enctype="multipart/form-data">
            <input class="form-control" type="file" name="imagefile" >
            <input class="btn btn-primary mt-3"type="submit" value="Predict Image" >
        </form>
        <div>
            path:{{path}}
            <img src= "{{url_for('static', filename=path)}}" >
        </div>
        <div>
        {% if prediction %}
            <p class="text-center"> Image is a {{prediction}}</p>
        {% endif %}
    </div>
    </body>
</html>


